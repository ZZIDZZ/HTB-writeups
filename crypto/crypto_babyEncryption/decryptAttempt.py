import string

f = open('msg.enc', 'r')
encrypted = f.read()
encryptArr = []
decrypted = ""

for i in range(0,len(encrypted), 2):
    try:
        hex2Num = int(encrypted[i:i+2], 16)
        encryptArr.append(hex2Num)
    except:
        encryptArr.append(i)
        
for num in encryptArr:
    for i in range(0,127):
        if ((123 * i) + 18) % 256 == num:
            decrypted+=chr(i)

print(decrypted)
