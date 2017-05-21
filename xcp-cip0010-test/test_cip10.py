from test_cip10_compress import mpmaSend
from test_cip10_decompress import mpmaSendDecode
import pprint
#import memory_profiler
import binascii

sends = [
    ('XCP', '3NA8hsjfdgVkmmVS9moHmkZsVCoLxUkvvv', 143250000),
    ('XCP', '1LWkDHE1gJ3z4k6hiC3zpvGd11sxqr3pdh', 649398295),
    ('PEPECASH', '1AXnNzHtee19mmsi7bKAgWTpTAsTFEfos', 4565463342),
    ('PEPECASH', '1LWkDHE1gJ3z4k6hiC3zpvGd11sxqr3pdh', 37563345767423),
    ('PEPECASH', '3NA8hsjfdgVkmmVS9moHmkZsVCoLxUkvvv', 877654544),
    ('HAIRPEPE', '1AXnNzHtee19mmsi7bKAgWTpTAsTFEfos', 65),
    ('HAIRPEPE', '3NA8hsjfdgVkmmVS9moHmkZsVCoLxUkvvv', 3),
    ('HAIRPEPE', '1KS9Pw8RSofrLVtVkGHSPhTR7993siXn2m', 2),
    ('PWAPWAPWAPWA', '1LWkDHE1gJ3z4k6hiC3zpvGd11sxqr3pdh', 6),
    ('PWAPWAPWAPWA', '1AXnNzHtee19mmsi7bKAgWTpTAsTFEfos', 8)
]

#print(compressSends(constructSends(sends)))
rounds = 10
testCompress = False
testCodec = False
useLzma = True

if useLzma:
    print('CIP10 + LZMA test')
else:
    print('CIP10 without LZMA')

pp = pprint.PrettyPrinter(indent=4)

if testCodec:
    pp.pprint(mpmaSendDecode(mpmaSend(sends, use_lzma=useLzma), use_lzma=useLzma))

print(mpmaSend(sends, use_lzma=False).hex())
print(len(mpmaSend(sends, use_lzma=True)))
#preSend = mpmaSend(sends, use_lzma=useLzma)
#print(binascii.hexlify(preSend))

exit()

preSend = binascii.unhexlify('0002003403265efb94afc74fb5b0e3a3fed4ed7f1f991266e14ec7fc920f7b0333ff7eca2e5bcea67b704bbd5d708949ef4a50cd6b02ad130e306c94a808395b474af9fefbde4fd6443da9138353bf6dad8e8252e5118dc0b0d4de7f9259da61d2315e2ac5892a84c3b2bee98cb103e69fbf4a8492a1c500c68020abf048d0c599ef304dc2c4282fe7cefea9708d2227e3b8ab7d2e177fe5d9648e4afde4742dba942ab6c6599feb296a7ca479aae7cf535b94ffff6d700000')

@profile
def testMem():
    if testCompress:
        send = mpmaSend(sends, use_lzma=useLzma)

        return len(send)
    else:
        dec = mpmaSendDecode(preSend, use_lzma=useLzma)

        return len(preSend)

def testRounds():
    if testCompress:
        print('> Doing %i MPMA sends' % rounds)
        for i in range(0, rounds):
            send = mpmaSend(sends, use_lzma=useLzma)

        return len(send)
    else:
        print('> Doing %i MPMA decs' % rounds)
        for i in range(0, rounds):
            dec = mpmaSendDecode(preSend, use_lzma=useLzma)

        return len(preSend)



print(testMem(), ' bytes')
