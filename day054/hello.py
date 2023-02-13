from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route("/newpage")
def new_page():
    return "This is a new page created by me."

if __name__ == "__main__":
    app.run()