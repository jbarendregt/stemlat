from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000))
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'))

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    opinions = db.relationship(Opinion, backref='theme')

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    opinions = db.relationship(Opinion, backref='party')
