
# Get n-th block from ciphertext hex string
def get_n_block(s,n):
    return bytes.fromhex(s[(n-1)*32:(32*n)])

# MAIN
# Target host
# BLOCKS -> b"logged_username=",b"admin&password=g",b"0ld3n_b0y"+b"\x07"*7

real_username,incorrect_username,password = "admin","bdmin","g0ld3n_b0y" # Username starts where second block starts; Usernames differ only by first character

# Ciphertext for fake username
incorrect_ciphertext = "70abb61802be621bf0a4f7286858db89835a8dec98e562b8b71b849f5a6a3f315a894010b99f61cd85c14bb58191d5b6"

# Flip 1st byte of block 2 by flipping 1st byte of b1 to get a correct ciphertext
b1 = get_n_block(incorrect_ciphertext,1)
b2 = get_n_block(incorrect_ciphertext,2)
b3 = get_n_block(incorrect_ciphertext,3)
print(b1, b2, b3)

b1_new = []
flipped_byte = (b1[0] ^ ord(real_username[0]) ^ ord(incorrect_username[0])).to_bytes(1,"big")
b1_new = flipped_byte + b1[1:]

correct_ciphertext = (bytes(b1_new) + b2 + b3).hex()
print(correct_ciphertext)