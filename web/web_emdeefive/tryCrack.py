import requests
import hashlib


host = "http://138.68.131.63:31985/"
r = requests.get(host)


# r2 = requests.get(host, json={"hash": "testString"})
answer = r.text
calonHash = answer.split('\n')[5][66:86]
hashed = hashlib.md5(calonHash.encode('utf-8')).hexdigest()
sessid = str(r.cookies)[37:63]
print (sessid)

# print(answer+"\n")
print(calonHash+"\n")
print(hashed)

r = requests.post(host, json={"hash": hashed}, data={"hash": hashed}, cookies=r.cookies)
print(r.text)
print(r.headers)
# print(r2.text+"\n")
# print(r2.headers)