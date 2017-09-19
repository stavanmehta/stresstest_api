# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from stresstest_api.database import db


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Feature %r>' % self.name

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    feature_id = db.Column(db.Integer, db.ForeignKey('feature.id'))
    feature = db.relationship('Feature', backref=db.backref('scenarios', lazy='dynamic'))

    # steps = db.relationship('Steps', backref=db.backref('scenarios', lazy='dynamic'))

    def __init__(self, title, body, feature, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.feature = feature
        # self.steps = steps

    def __repr__(self):
        return '<Scenario %r>' % self.title


# class Step(db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     sceanrio_id = db.Column(db.Integer, db.ForeignKey('scenario.id'))
#
#     name = db.Column(db.String(40))
#     sequence = db.Column(db.Integer)
#     step_request = db.Column(db.Integer, db.ForeignKey('steprequest.id'))
#     step_validations = db.relationship('StepValidations', backref=db.backref('step', lazy='dynamic'))
#
#
#     def __init__(self, id, scenario_id, name, sequence, step_request, step_validations):
#         self.id = id
#         self.sceanrio_id = scenario_id
#         self.name = name
#         self.sequence = sequence
#         self.step_request = step_request
#         self.step_validations = step_validations
#
#     def __repr__(self):
#         return '<Step %r>' % self.id
#
# class StepRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     step_id = db.Column(db.Integer, db.ForeignKey('step.id'))
#     request_method = db.Column(db.String(10))
#     request_url = db.Column(db.String(100))
#     request_params = db.Column(db.String(100))
#     request_headers = db.Column(db.String(100))
#     request_data = db.Column(db.String(100))
#
#
#     def __init__(self, id, step_id, request_method, request_url, request_params, request_headers, request_data):
#         self.id = id
#         self.step_id = step_id
#         self.request_method = request_method
#         self.request_url = request_url
#         self.request_params = request_params
#         self.request_headers = request_headers
#         self.request_data = request_data
#
#     def __repr__(self):
#         return '<Step Request %r>' % self.id
#
# class StepValidation(db.Model):
#     id = db.Column(db.Integer, primary_key=True, unique=True)
#     step_id = db.Column(db.Integer, db.ForeignKey('step.id'))
#     validation_type = db.Column(db.String(80))
#     validation_format = db.Column(db.String(80))
#     assertion = db.Column(db.String(20))
#     assertion_data = db.Column(db.String(100))
#
#     def __init__(self, id, step_id, validation_type, validation_format, assertion, assertion_data):
#         self.id = id
#         self.step_id = step_id
#         self.validation_type = validation_type
#         self.validation_format = validation_format
#         self.assertion = assertion
#         self.assertion_data = assertion_data
#
#     def __repr__(self):
#         return '<Step Validation %r>' % self.id