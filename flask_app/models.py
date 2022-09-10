from datetime import datetime
from flask_app import db, login_manager
from flask_login import UserMixin 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# using SQLAlchemy.Database
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    # one to many rel below 
    posts = db.relationship('Record', backref='author', lazy=True) 
    
    def __repr__(self) -> str:
        return f"User('{self.first_name}', '{self.last_name}' '{self.email}', '{self.image_file}')"

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Post('[self.title]', '{self.date_posted}')"

# using SQL Database 
# from flask_app.config.mysqlconnection import connectToMySQL
# import re 
# from flask import flash 
    # class User:
    #     db = 'login_reg'
    #     def __init__(self, data):
    #         self.id = data['id']
    #         self.first_name = data['first_name']
    #         self.last_name = data['last_name']
    #         self.email = data['email']
    #         self.password = data['password']
    #         self.created_at = data['created_at']
    #         self.updated_at  =data['updated_at']