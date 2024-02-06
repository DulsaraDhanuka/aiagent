from flask import Flask

app = Flask(__name__)

@app.route("/generate")
def generate():
    return "Hello World"

