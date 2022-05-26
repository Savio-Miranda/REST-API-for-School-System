from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    ocupation = db.Column(db.String(9), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    # Columns linked to other database models
    assigned_institution = db.Column(db.String(100), db.ForeignKey('institution.id'))
    assigned_class = db.Column(db.String(20), db.ForeignKey('classroom.id'))

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self):
        return f'Username: {self.username}'


class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution_name = db.Column(db.String(200), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)

    assigned_institution = db.relationship('User', backref='Institution')
    school_belonging = db.relationship('Classroom', backref='Institution')

    def __repr__(self):
        return f'Instituição: {self.institution_name}'


class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(20), unique=True, nullable=False)

    # Columns linked to other database models
    school_belonging = db.Column(db.String(100), db.ForeignKey('institution.id'))
    assigned_class = db.relationship('Institution', backref='Classroom')

    def __repr__(self):
        return f'Classe: {self.class_name}'
