from flask import Flask
from flask import make_response
app = Flask(__name__)


@app.route("/")
def index():
    response=make_response("<h1>Hello World3!</h>")
    return response


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, %s!" % name


if __name__ == "__main__":
    app.run(debug=True)
