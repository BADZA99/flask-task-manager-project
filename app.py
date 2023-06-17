from flask import Flask,render_template

from routes import *


if __name__== "__main__":
    app.run(port=5000,debug=True)