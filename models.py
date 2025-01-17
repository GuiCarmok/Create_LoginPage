from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    

