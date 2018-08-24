from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

##############################################
#### connect to DB, flaskapp #################
##############################################

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://zuki:MyPassW0rd@localhost/flaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    devtype = db.Column(db.String(30))
    ipaddress = db.Column(db.String(15))

class Instances(db.Model):
    __tablename__ = "instances"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    itype = db.Column(db.String(30))
    device = db.Column(db.Integer,db.ForeignKey('devices.id'), nullable=False)
    direction = db.Column(db.String(5))
    url = db.Column(db.String(100))
