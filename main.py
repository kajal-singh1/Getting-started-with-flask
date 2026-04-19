# This file majorly used for receiving the end points 

from flask import Flask

app = Flask(__name__)

# URL => End Point
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug=True)