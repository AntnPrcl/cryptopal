import base64

def hex_to_b64(hexstr):
    bin = bytearray.fromhex(hexstr)
    b64str = base64.b64encode(bin)
    return b64str