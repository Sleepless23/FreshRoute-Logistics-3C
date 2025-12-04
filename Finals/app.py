from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "DevNetPackageGroup"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/form', methods=['GET', 'POST'])
def packageform():
    return render_template("packageform.html")

@app.route('/report')
def packagereports():
    return render_template("packagereports.html")

@app.route('/route')
def packageroute():
    return render_template("packageroute.html")

if __name__ == '__main__':
    app.run(debug=True) 