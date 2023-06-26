def get_n_block(s,n):
    return bytes.fromhex(s[(n-1)*32:(32*n)])

ruser = 'admrn'
iuser = 'admin'
password = 'g0ld3n_b0y'
incorrect_ciphertext = "70abb61802be621bf0a4f7286858db89fef002abcf9e1e050b4d722a8d6e6e50601006c331bd79d1cbfe1e17979f030c"

b = []
for i in range(1,4):
    b.append(get_n_block(incorrect_ciphertext,i))

b0_flip = (b[0][3] ^ ord('i') ^ ord('r')).to_bytes(1,"big")
b[0] = b[0][:3] + b0_flip + b[0][4:]

new_ct = (b[0] + b[1] + b[2]).hex()
print(new_ct)