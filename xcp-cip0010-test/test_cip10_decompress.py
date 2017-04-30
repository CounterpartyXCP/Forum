import struct
import binascii
import math
from bitstring import BitArray, ConstBitStream
from bitcoin import base58
from xcp import asset_name

def decodeLUT(data):
    (numAddresses,) = struct.unpack('H', data[0:2])
    p = 2
    addressList = []
    for i in range(0, numAddresses):
        addr_raw = data[p:p+25]
        addressList.append(base58.encode(addr_raw))
        p += 25

    lutNbits = math.ceil(math.log2(numAddresses))

    return addressList, lutNbits, data[p:]

def decodeSendList(stream, nbits, lut):
    asset_id = stream.read('uintle:64')
    numRecipients = stream.read('uint:%i' % nbits)
    sendList = []

    for i in range(0, numRecipients):
        addr = lut[stream.read('uint:%i' % nbits)]
        amount = stream.read('uintle:64')
        sendList.append((addr, amount))

    asset = asset_name(asset_id)

    return asset, sendList

def decodeSends(data, nbits, lut):
    stream = ConstBitStream(data)
    sends = {}

    while stream.read('bool'):
        asset, sendList = decodeSendList(stream, nbits, lut)
        sends[asset] = sendList

    return sends

def lzma_decompress(data):
    raise 'LZMA decompress not implemented'

def mpmaSendDecode(data, use_lzma=False):
    if use_lzma:
        data = lzma_decompress(data)

    lut, nbits, remain = decodeLUT(data)
    sends = decodeSends(remain, nbits, lut)

    return sends
