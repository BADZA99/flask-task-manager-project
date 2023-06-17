from flask import Flask,render_template
app= Flask(__name__)
error=0
data = None
@app.route('/')
def home():
    global data
    return render_template("base.html")

@app.route('/signin')
def signin():
    global data
    return render_template("signin.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/taches')
def taches():
    return render_template("taches.html")
