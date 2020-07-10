from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello, World! <a href="/status">Статус</a>'


@app.route("/status")
def status():
    return {
        'status': 'OK',
        'name': 'ErmMsg',
        'time': datetime.now()
    }


app.run()
