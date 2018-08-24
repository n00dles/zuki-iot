from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from models import *


@app.route('/')
def index():
    records = Devices.query.filter(Devices.display==1)
    return render_template('index.html', records = records)

@app.route('/add')
def add():

    return "Add Page"




if __name__ == '__main__':
    app.run(debug=True)

