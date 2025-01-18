from flask import Flask

app = Flask(__name__)


@app.route("/info")
def hello():
    return "Welcome to hello world... \n"


app.run(host='0.0.0.0', port=5000)
