from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from models import *


@app.route('/')
def index():

    records = Devices.query.filter(Devices.display==1)
    context = { 'menu': 'home', 'records' : records}
    return render_template('index.html', context = context)

@app.route('/adddevice')
def adddevice():
    context = { 'menu': 'adddevice'}
    return render_template('adddevice.html', context=context)


@app.route('/addinstance')
def addinstance():
    records = Devices.query.filter(Devices.display==1)
    context = { 'menu': 'addinstance', 'records' : records}
    return render_template('addinstance.html', context = context)






if __name__ == '__main__':
    app.run(debug=True)

