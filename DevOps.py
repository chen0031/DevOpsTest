"""
This is a sample code.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/test')
def test():
    return "This is a DevOps test"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9999)