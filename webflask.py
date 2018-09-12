from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/main')
def Request():
    data = request.data
    return data