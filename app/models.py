from flask_sqlalchemy import SQLAlchemy
from . import db


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(64))
    opinions = db.relationship(Opinion, backref='topic')
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'))

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme_name = db.Column(db.String(64))
    topics = db.relationship(Topic, backref='theme')

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    party_name = db.Column(db.String(64))
    opinions = db.relationship(Opinion, backref='party')
