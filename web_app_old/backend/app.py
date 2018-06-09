
from flask import Flask, send_from_directory
app = Flask(__name__)

def hello():
    return "Hello World!"

@app.route("/<path:path>")
def send_js(path):
    return send_from_directory('public', path)