from app import app # treat it like a package
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "<h1 style='color: red'> About!!!</h1>"