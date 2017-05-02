import struct
import binascii
import math
import lzma
from bitstring import BitArray, BitStream
from bitcoin import base58
from xcp import asset_id

def sendToMany(asset, addr_amnt_tuples):
    pkdAsset = struct.pack('Q', asset)
    pkdTuples = [b''.join([addr, struct.pack('Q', amnt)]) for (addr, amnt) in addr_amnt_tuples]

    return b''.join([pkdAsset, *pkdTuples])

def addrToBytes(addr):
    return base58.decode(addr)[:-4]

def constructBaseLUT(snds):
    return list(set([addr for (asset, addr, amnt) in snds]))

def constructBaseAssets(snds):
    return list(set([asset for (asset, addr, amnt) in snds]))

def constructLUT(snds):
    baseLUT = constructBaseLUT(snds)
    lutNbits = math.ceil(math.log2(len(baseLUT)))
    return {
        "nbits": lutNbits,
        "addrs": baseLUT
    }

def compressLUT(lut):
    return b''.join([struct.pack('H', len(lut['addrs']))] +
        [
            addrToBytes(addr)
            for addr in lut['addrs']
        ])

def constructSendList(snd_asset, lut, snds):
    return [
        (lut['addrs'].index(addr), amnt)
        for (asset, addr, amnt) in snds
        if asset == snd_asset
    ]

def compressSendList(nbits, send):
    r = BitArray()
    r.append('uintle:64=%i' % asset_id(send['assetName']))
    r.append('uint:%i=%i' % (nbits, len(send['sendList'])))
    for (idx, amnt) in send['sendList']:
        r.append('uint:%i=%i' % (nbits, idx))
        r.append('uintle:64=%i' % amnt)
    return r

def constructSends(snds):
    lut = constructLUT(snds)
    assets = constructBaseAssets(snds)

    sendLists = [
        {
            "assetName": asset,
            "sendList": constructSendList(asset, lut, snds)
        }
        for asset in assets
    ]

    return {
        "lut": lut,
        "sendLists": sendLists
    }

def compressSends(mpmaSend):
    compressedLUT = compressLUT(mpmaSend['lut'])

    isends = ''.join([
        ''.join(['0b1', compressSendList(mpmaSend['lut']['nbits'], sendList).bin])
        for sendList in mpmaSend['sendLists']
    ])
    bstr = ''.join([isends, '0'])
    barr = BitArray(bstr+'0' * (8 - len(bstr) % 8))
    return b''.join([
        compressedLUT,
        barr.bytes
    ])

def lzma_compress(p):
    cmp = lzma.LZMACompressor(format=lzma.FORMAT_RAW,
        filters=[{
            "id": lzma.FILTER_LZMA1,
            "preset": 7
            }])
    f = cmp.compress(p)
    l = cmp.flush()

    return b''.join([f, l])

def mpmaSend(sends, use_lzma=False):
    mpma = constructSends(sends)
    send = compressSends(mpma)
    if use_lzma:
        send = lzma_compress(send)

    return send
