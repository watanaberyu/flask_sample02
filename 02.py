import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/omikuji")
def omikuji():
    results = random.choice(["大吉", "吉", "凶"])

    return render_template("omikuji.html", results=results)


@app.route("/dice")
def dice():
    results = random.choice([1, 2, 3, 4, 5, 6])
    return render_template("dice.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
