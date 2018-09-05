from flask import Flask, render_template, request,json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
import string, random, datetime, time
from models import *
from security import * 


###########################################
# i know the routing can be done better 
# for now it works.
###########################################

## string of 64 random ascii chars
app_salt = 'ms7kmVj9svyy5dERCdcJ57zKFpgE29YGoUHiQMR3eEIuhB493XhYiPcjRLxbcCls' 

@app.route('/')
def index():
    records = db.session.query(Devices.name, Instances.id, Devices.desc, Devices.ipaddress, db.func.count(Instances.device).label("num")).outerjoin(Instances).group_by(Devices.id).filter(Devices.display==1)
    instances = Instances.query.all()
    context = { 'menu': 'home', 'records' : records, 'instances': instances}
    return render_template('index.html', context = context)

@app.route('/getinstance/<id>')
def getinstance(id):
    print("getting ID " + str(id))
    current_value = Devicedata.query.filter(Devicedata.device==str(id)).order_by(Devicedata.timestamp.desc()).first()
    print(current_value.data)
    return "<h1>" + str(current_value.data) + "&deg;c</h1><br/><time>"+time.strftime("%H:%M:%S", time.gmtime(current_value.timestamp))+"</time>"
    pass

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
    hashkey=hashkey(20)
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

@app.route("/adddata", methods=['POST', 'GET'])
def addd():
    if request.form.get('data',None):
        print(request.form.get('data'))
        device = request.form['device']
        hashkey = request.form['hashkey']
        datai = request.form['datai']
        data = request.form['data']
        timestamp = int(time.time())
        dev = db.session.query(Devices).filter(Devices.hashkey == hashkey, Devices.id == device).first()
        if dev is None:
            return "auth error"
        dev = db.session.query(Instances).filter(Instances.id == datai).first()
        if dev is None:
            return "instance error"
        devicedata = Devicedata(device=datai, data=data, timestamp=timestamp) 
        db.session.add(devicedata)
        db.session.commit()
    else:
        return "No data"
    return 'ok'


@app.route("/viewdata")
def viewdata():
    records = Devicedata.query.all()
    context = { 'menu': 'home', 'records' : records}
    return render_template('viewdata.html', context = context)

@app.route('/addinstance')
def addinstance():
    records = Devices.query.all()
    context = { 'menu': 'addinstance', 'records' : records}
    return render_template('addinstance.html', context = context)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')