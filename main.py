# This file majorly used for receiving the end points 

from flask import Flask, render_template

app = Flask(__name__, static_folder="assets")

# URL => End Point
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/prime")
def prime():
    return "<p>Hello from Prime!</p>"

if __name__ == "__main__":
    app.run(debug=True)