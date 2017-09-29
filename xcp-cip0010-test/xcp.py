def asset_name(assetid):
    if assetid == 1:
        return 'XCP'
    name = ''
    while assetid > 0:
        name += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[assetid % 26]
        assetid //= 26
    return name[::-1]

def asset_id(asset):
    if (asset == 'BTC'):
        return 0
    elif (asset == 'XCP'):
        return 1
    else:
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = 0
        for c in asset:
            n *= 26
            n += chars.index(c)

        return n
