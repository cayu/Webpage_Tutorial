#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    greetings = "Hello World"
    return render_template("home.html", greetings=greetings)


if __name__ == "__main__":
    app.directory='./'
    app.run(host='0.0.0.0', port=50000,debug=True)
