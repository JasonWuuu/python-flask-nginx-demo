import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)


@app.route('/')
def show_hello():
    myname = os.getenv('myname')
    return myname


if __name__ == '__main__':
    load_dotenv()
    app.run(port=8080)
