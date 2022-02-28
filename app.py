from flask import Flask, render_template, request, session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

app.run(host='0.0.0.0')