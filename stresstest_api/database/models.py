# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from stresstest_api.database import db


class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    feature_id = db.Column(db.Integer, db.ForeignKey('feature.id'))
    feature = db.relationship('Feature', backref=db.backref('scenarios', lazy='dynamic'))

    def __init__(self, title, body, feature, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.feature = feature

    def __repr__(self):
        return '<Scenario %r>' % self.title


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Feature %r>' % self.name
