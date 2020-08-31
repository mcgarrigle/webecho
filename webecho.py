#!/usr/bin/env python3

from flask import Flask
from flask import request

app = Flask(__name__)

def dump(d):
    a = [ f"{k}: {v}" for (k, v) in d.items() ]
    return "<br>".join(a)

@app.route('/')
def hello_world():
    r = str(dict(request.headers)) + "<br>" + str(dict(request.args))
    r = dump(dict(request.headers)) + "<br><hr>" + dump(dict(request.args))
    return r

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
