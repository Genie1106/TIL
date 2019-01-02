from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

@app.route("/ssafy")
def ssafy():
    return "This is SSAFY!"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'Welcome! {name}'
        
@app.route("/cube/<int:num>")
def cube(num):
    cube = num**3
    return f'{num}의 세제곱은 {cube}입니다.'   

@app.route("/lunch/<int:person>")
def lunch(person):
    menu = ['미더덕된장찌개','쫄면순두부찌개','투움바파스타','옛날짬뽕']
    order = random.sample(menu,person)
    return str(order)     

@app.route("/html")
def html():
    multiline_string = '''
        <h1>이것은 h1입니다</h1>
        <p>이것은 p입니다</p>
    '''
    return multiline_string

@app.route("/html_file")
def html_file():
    return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html',name = name)

@app.route("/fake_naver")
def fake_naver():
    return render_template("fake_naver.html")
