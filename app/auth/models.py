# coding=utf-8
from app import db
from datetime import datetime



class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'Agora_Market_Users'
    __table_args__ = {'useexisting': True}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    username = db.Column(db.Text)
    password_hash = db.Column(db.Text)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow())
    email = db.Column(db.Text)
    wallet_pin = db.Column(db.Text)
    profileimage = db.Column(db.Text)
    stringuserdir = db.Column(db.Text)
    bio = db.Column(db.TEXT)
    country = db.Column(db.Text)
    currency = db.Column(db.INTEGER)
    vendor_account = db.Column(db.INTEGER)
    selling_from = db.Column(db.Text)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow())
    admin = db.Column(db.INTEGER)
    admin_role = db.Column(db.INTEGER)
    dispute = db.Column(db.INTEGER)
    fails = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    vacation = db.Column(db.INTEGER)
    shopping_timer = db.Column(db.DATETIME)
    lasttraded_timer = db.Column(db.DATETIME)
    shard = db.Column(db.INTEGER)
    protosuser = db.Column(db.INTEGER)


db.create_all()
db.session.commit()