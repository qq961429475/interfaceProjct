import requests

from flask import request, Flask

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return "username:%s,password:%s" % (username, password)
