from flask import Flask
app = Flask(__name__)

app.debug = True



@app.route("/welcome")
def welcome_page():
    return "Welcome"

@app.route("/welcome/home")
def welcome_home_page():
    return "Welcome Home"

@app.route("/welcome/back")
def welcome_back_page():
    return "Welcome Back"


