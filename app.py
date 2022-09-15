#!/usr/bin/env python
from flask import Flask
from flask import render_template

app=Flask(__name__)

alumne1 = {
            "name": "Jose Angel"
        }

@app.route("/")
@app.route("/index")
def index():
  return render_template('index.html', alumne=alumne1)

@app.route("/flask")
def flask():
  return "<h1>Flask Hello World!</h1>"

if __name__== "__main__":
  app.run()

