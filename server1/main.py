import requests
import time
import threading
from flask import Flask, render_template, request, jsonify

#pip freeze > requirement.txt
app = Flask(__name__)

UrlAutreServer = ""

@app.route('/')
def index():

    if UrlAutreServer == "":
        GetUrl()
    t1 = threading.Thread(target=_Send)
    t1.start()
    return 'ping'


def _Send():
    time.sleep(2)
    res = requests.get(UrlAutreServer).content
    print(res)


def _SendAddresse():
    url = 'http://127.0.0.1:8080/SetAddresses1'
    myobj = {'adr': 'http://127.0.0.1:5372'}
    x = requests.post(url, data=myobj)
    print(x)

def GetUrl():
    url = 'http://127.0.0.1:8080/getAdresses'
    myobj = {'Num': '1'}
    x = requests.post(url, data=myobj)
    global UrlAutreServer
    UrlAutreServer = x.text
    #return x


if __name__ == '__main__':
    _SendAddresse()
    app.run(debug=True, port=5372)
