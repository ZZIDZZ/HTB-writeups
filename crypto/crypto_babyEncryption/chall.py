import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append(((123 * char) + 18) % 256)
    return bytes(ct)

# enc = ((123*dec) + 18) % 256
# 

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()


