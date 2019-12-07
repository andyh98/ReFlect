from ReFlect import app, db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db.create_all()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) #auto increment is default
    name = db.Column(db.String(100))
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def is_active(self):
            return True

    def get_id(self):
        return self.id

    def is_anonymous(self):
        return False

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password_candidate):
        return check_password_hash(self.password, password_candidate)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.register_date}')"

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True) #auto increment is default
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    prompt = db.Column(db.Text)
    

    def __repr__(self):
        return f"Post('{self.title}','{self.create_date}')"