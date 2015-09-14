__author__ = 'Robert'
from app import db

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64), unique=True)
    last_name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(256), unique=True)
    street_address = db.Column(db.String(256))
    city = db.Column(db.String(64))
    state = db.Column(db.String(32))
    zipcode = db.Column(db.String(16))

    def __repr__(self):
        return 'User: {} {}'.format(self.first_name, self.last_name)
