import sys
path = '/home/alexandresaran96/geo-api'
if path not in sys.path:
   sys.path.append(path)
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/main', methods= ['POST'])
def home():
    data = request.get_json(silent=True)["url_nota_fiscal"]
    return data

if __name__ == '__main__':
    app.run()