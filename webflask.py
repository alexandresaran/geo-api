import sys
path = '/home/alexandresaran96/geo-api'
if path not in sys.path:
   sys.path.append(path)
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/main')
def home():
    data = request.data
    return data

if __name__ == '__main__':
    app.run()