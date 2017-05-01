import struct
import binascii
import math
from bitstring import BitArray, ConstBitStream
from bitcoin import base58
from bitcoin.core import key
from xcp import asset_name

def addressFrom21Bytes(b):
    sha256_1 = key.hashlib.new('sha256')
    sha256_1.update(b)

    sha256_2 = key.hashlib.new('sha256')
    sha256_2.update(sha256_1.digest())

    chk = sha256_2.digest()[:4]

    return base58.encode(b''.join([b, chk]))

def decodeLUT(data):
    (numAddresses,) = struct.unpack('H', data[0:2])
    p = 2
    addressList = []
    bytesPerAddress = 21

    for i in range(0, numAddresses):
        addr_raw = data[p:p+bytesPerAddress]

        addressList.append(addressFrom21Bytes(addr_raw))
        p += bytesPerAddress

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
