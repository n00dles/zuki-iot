from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter


##############################################
#### connect to DB, flaskapp #################
##############################################

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://zuki:MyPassW0rd@localhost/flaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = "SuperSecretKeySuperSecretKeySuperSecretKeySuperSecretKey"


# Flask-User settings
app.config['USER_APP_NAME'] = "Zuki"      # Shown in and email templates and page footers
app.config['USER_ENABLE_EMAIL'] = False      # Disable email authentication
app.config['USER_ENABLE_USERNAME'] = True    # Enable username authentication
app.config['USER_REQUIRE_RETYPE_PASSWORD'] = False    # Simplify register form
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

        # User authentication information. The collation='NOCASE' is required
        # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
        username = db.Column(db.String(100), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        email_confirmed_at = db.Column(db.DateTime())

        # User information
        first_name = db.Column(db.String(100), nullable=False, server_default='')
        last_name = db.Column(db.String(100), nullable=False, server_default='')


# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)


class UserOld(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique = True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean, nullable=False, server_default='1')

#db_adapter = SQLAlchemy(db, User)
#user_manager = UserManager(db_adapter, app) 



class Devices(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    devtype = db.Column(db.String(30))
    ipaddress = db.Column(db.String(15))
    hashkey = db.Column(db.String(100))
    display = db.Column(db.Boolean)

class Instances(db.Model):
    __tablename__ = "instances"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(100))
    itype = db.Column(db.String(30))
    device = db.Column(db.Integer,db.ForeignKey('devices.id'), nullable=False)
    direction = db.Column(db.String(5))
    url = db.Column(db.String(100))
    display = db.Column(db.Boolean,server_default='1' )

class Devicedata(db.Model):
    __tablename__ = "devicedata"
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.Integer,db.ForeignKey('instances.id'), nullable=False)
    data = db.Column(db.String(100))
    timestamp = db.Column(db.Integer)