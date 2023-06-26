import socketserver 
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify
from secret import FLAG

key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt_data(data):
	padded = pad(data.encode(),16,style='pkcs7')
	cipher = AES.new(key, AES.MODE_CBC,iv)
	enc = cipher.encrypt(padded)
	return enc.hex()

def decrypt_data(encryptedParams):
	cipher = AES.new(key, AES.MODE_CBC,iv)
	paddedParams = cipher.decrypt( unhexlify(encryptedParams))
	print(paddedParams)
	if b'admin&password=g0ld3n_b0y' in unpad(paddedParams,16,style='pkcs7'):
		return 1
	else:
		return 0

user = 'bdmin'
password = 'g0ld3n_b0y'
msg = 'logged_username=' + user + '&password=' + password
print(msg, len(msg))
xor = ord('a') ^ ord('b')
cipher = encrypt_data(msg)
print(cipher[:16],hex(int(cipher[16:18], 16) ^ xor)[2:], cipher[16:18], cipher[18:])
cipher = cipher[:16] + hex(int(cipher[16:18], 16) ^ xor)[2:] + cipher[18:]
print(cipher)
print(decrypt_data(cipher))