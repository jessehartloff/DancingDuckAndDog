import datetime
import time
import os

from flask import Flask, send_from_directory, render_template, make_response, redirect, request


app = Flask(__name__)


@app.get('/')
def cse312():
    filename = 'index.html'
    resp = make_response(send_from_directory('public', filename))
    return resp


@app.get('/<path:filename>')
def send_style(filename):
    resp = make_response(send_from_directory('public', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
