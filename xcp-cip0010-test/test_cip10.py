from test_cip10_compress import mpmaSend
from test_cip10_decompress import mpmaSendDecode
import pprint

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
rounds = 1000
#print('CIP10 + LZMA test')
print('CIP10 without LZMA')

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(mpmaSendDecode(mpmaSend(sends)))

print('> Doing %i MPMA sends' % rounds)
for i in range(0, rounds):
    send = mpmaSend(sends)

print(len(send), ' bytes')
#print(binascii.hexlify(send))
