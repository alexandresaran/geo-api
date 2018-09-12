import sys
path = '/home/yourusername/mysite'
if path not in sys.path:
   sys.path.append(path)

from flask_app import app as application
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    data = request.data
    return data

if __name__ == '__main__':
    app.run()