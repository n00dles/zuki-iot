from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_key'

##############################################
#### connect to DB, flaskapp #################
##############################################

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

