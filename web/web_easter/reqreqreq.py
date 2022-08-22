import requests

host = "http://167.71.139.140:31491/"
for i in range(30):
    resp = requests.get(host+"message/3")
    print(resp.text)
