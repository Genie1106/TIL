import random
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def ping():
    return render_template('ping.html')

@app.route("/pong")
def pong():
    name = request.args['name']
    make = ['홍콩.jpg','대만.jpg','제주도.jpg','다낭.jpg','캘리포니아.jpg']
    result = random.choice(make)
    return render_template('pong.html',name_in_html = name, result = result)

@app.route("/lotto/<int:num>")
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()

    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
    bonus = lotto['bnusNo']    
    return render_template('lotto.html',w=winner,b=bonus,n=num)