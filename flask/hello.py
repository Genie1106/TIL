from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/python")
def python():
    return "python is funny!"

@app.route("/dictionary/<string:word>")
def dictionary(word):
    my_dict={
        "apple":"사과",
        "banana":"바나나",
        "pear":"배",
        "watermelon":"수박"
        }

    result = my_dict.get(word,"나만의 단어장에 없는 단어")
    return f"{word}은(는) {result}입니다."

