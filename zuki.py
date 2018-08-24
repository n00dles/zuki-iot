from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

from models import *


@app.route('/')
def index():
    rt = ''
    records = Devices.query.all()
    return render_template('index.html', records = records)

@app.route('/add')
def add():

    return "Add Page"

@app.route('/home')
def home():
    return "On the home page " 



if __name__ == '__main__':
    app.run(debug=True)

