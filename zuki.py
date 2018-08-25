from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import *

###########################################
# i know the routing can be done better 
# for now it works.
###########################################

@app.route('/')
def index():
    records = db.session.query(Devices.name, Devices.desc, Devices.ipaddress, db.func.count(Instances.device).label("num")).outerjoin(Instances).group_by(Devices.id).filter(Devices.display==1)
    context = { 'menu': 'home', 'records' : records}
    return render_template('index.html', context = context)

@app.route('/adddevice')
def adddevice():
    context = { 'menu': 'adddevice'}
    return render_template('adddevice.html', context=context)

@app.route("/processdevice", methods=["POST"])
def processd():
    name = request.form['name']
    desc = request.form['desc']
    devtype = request.form['devtype']
    ipaddress = request.form['ipaddress']
    hashkey="secret"
    display = 1

    device = Devices(name=name, desc=desc, devtype=devtype, ipaddress=ipaddress, hashkey=hashkey, display=display)
    db.session.add(device)
    db.session.commit()
    records = db.session.query(Devices.name, Devices.desc, Devices.ipaddress, db.func.count(Instances.device).label("num")).outerjoin(Instances).group_by(Devices.id).filter(Devices.display==1)
    context = { 'menu': 'home', 'records' : records}
    return render_template('index.html', context = context)

@app.route("/processinstance", methods=["POST"])
def processi():
    name = request.form['name']
    desc = request.form['desc']
    itype = request.form['itype']
    device = request.form['device']
    direction = request.form['direction']
    url = request.form['url']
    
    instance = Instances(name=name, desc=desc, itype=itype, device=device, direction=direction, url=url)
    db.session.add(instance)
    db.session.commit()
    records = db.session.query(Devices.name, Devices.desc, Devices.ipaddress, db.func.count(Instances.device).label("num")).outerjoin(Instances).group_by(Devices.id).filter(Devices.display==1)
    context = { 'menu': 'home', 'records' : records}
    return render_template('index.html', context = context)

@app.route('/addinstance')
def addinstance():
    records = Devices.query.filter(Devices.display==1)
    context = { 'menu': 'addinstance', 'records' : records}
    return render_template('addinstance.html', context = context)



if __name__ == '__main__':
    app.run(debug=True)