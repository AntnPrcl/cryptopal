def xor_str(str1, str2):
    str1_bin = bytearray(str1, 'utf-8')
    str2_bin = bytearray(str2, 'utf-8')

    xored = bytearray()
    index=0
    hexstr = ""
    for b1, b2 in zip(str1_bin, str2_bin):
        hexstr += (hex(b1 ^ b2))
        
        print(hexstr)
        index = index + 1 

    return xored.hex()