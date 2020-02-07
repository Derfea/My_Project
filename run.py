from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("layouts.html", title='Home')

@app.route("/Roblox")
def roblox():
    return render_template("Roblox.html", title='Roblox')

@app.route("/Robux")
def robux():
    return render_template("Robux.html", title='Robux')

@app.route("/Earn")
def earn():
    return render_template("Free_Robux.html", title='Earn')

@app.route("/Profile")
def profile():
    return render_template("Profile.html", title='Profile')

@app.route("/Get_Robux")
def get():
    return render_template("get_robux.html", title='Get_Robux')