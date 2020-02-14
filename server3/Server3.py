import requests
import time
import threading
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

URL1 = ""
URL2 = ""

@app.route('/')
def index():
    return 'Si tu vois ce message tu dois avoir une vie très ennuyante...'


@app.route('/SetAddresses1', methods=['GET', 'POST'])
def setAdresses1():
    if request.method == 'POST':
        adr = request.form.get('adr')
        global URL1
        URL1 = adr
        print("URL 1 :"+URL1)
        print("URL 2 :" + URL2)
        return URL1
    return 'Adresse non valide'


@app.route('/SetAddresses2', methods=['GET', 'POST'])
def setAdresses2():
    if request.method == 'POST':
        adr = request.form.get('adr')
        global URL2
        URL2 = adr
        print("URL 1 :"+URL1)
        print("URL 2 :" + URL2)
    return 'Adresse non valide'


@app.route('/getAdresses', methods=['GET', 'POST'])
def getAddresses():
    if request.method == 'POST':
        Num = request.form.get('Num')
        print(Num)
        if Num == "2":
            print("\n URL2 : "+URL2)
            return URL1
        if Num == "1":
            print("\n URL1 : "+URL1)
            return URL2

    return 'Parametre incorrectes'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
