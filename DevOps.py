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

@app.route('/update')
def update():
    return "We will update the program."

"""
A test.
"""

@app.route('/divide')
def devide():
    return "This is a divide function."


@app.route('/reduce')
def reduce():
    b = 1 - 1
    return "add a new reduce funtion."
"""
This is a test
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
