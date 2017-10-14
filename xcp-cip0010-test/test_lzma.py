import lzma
import struct
import binascii
from bitcoin import base58

print('Naive LZMA test')
def sendToMany(asset, addr_amnt_tuples):
    pkdAsset = struct.pack('Q', asset)
    pkdTuples = [b''.join([addr, struct.pack('Q', amnt)]) for (addr, amnt) in addr_amnt_tuples]

    return b''.join([pkdAsset, *pkdTuples])

def addrToBytes(addr):
    return base58.decode(addr)

def compress(p):
    cmp = lzma.LZMACompressor(format=lzma.FORMAT_RAW,
        filters=[{
            "id": lzma.FILTER_LZMA1,
            "preset": 9 | lzma.PRESET_EXTREME
            }])
    f = cmp.compress(p)
    l = cmp.flush()

    return b''.join([f, l])

addrSends_1 = [
    (addrToBytes('3NA8hsjfdgVkmmVS9moHmkZsVCoLxUkvvv'), 100000000),
    (addrToBytes('1AXnNzHtee19mmsi7bKAgWTpTAsTFEfos'), 25612800000)
    ]

pkt = sendToMany(1, addrSends_1)
print(len(pkt), ' bytes -> ', binascii.hexlify(pkt))
pktCmp = compress(pkt)
print(len(pktCmp), ' bytes -> ', binascii.hexlify(pktCmp))
