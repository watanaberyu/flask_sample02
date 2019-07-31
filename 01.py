from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return '''
        <form action="/login" method="post">
            Password: <input type="text"><br>
            <input type='submit'>
        </form>
        '''

    if request.method == "POST":
        return "Logged in"


if __name__ == "__main__":
    app.run(debug=True)
