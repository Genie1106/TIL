from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def ping():
    return render_template('ping.html')

@app.route("/pong")
def pong():
    return render_template('pong.html')  