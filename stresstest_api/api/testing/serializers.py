from flask_restplus import fields
from stresstest_api.api.restplus import api

testing_scenario = api.model('Testing scenario', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a testing scenario'),
    'title': fields.String(required=True, description='Scenario title'),
    'body': fields.String(required=True, description='Scenario content'),
    'sequence': fields.Integer(description='sequence inside the feature'),
    'pub_date': fields.DateTime,
    'feature_id': fields.Integer(attribute='feature.id'),
    'feature': fields.String(attribute='feature.id'),
})


testing_step = api.model('Testing step', {
    'name': fields.String(required=True, description='Step name'),
    'sequence': fields.Integer(description='step sequence'),
    'sceanrio_id': fields.Integer(attribute='scenario.id'),
    'method': fields.String(description='step sequence'),
    'params': fields.String(description='request params'),
    'headers': fields.String(description='request headers'),
    'body': fields.String(description='requst body'),
    'authorization': fields.String(description='authorization type')
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_testing_scenarios = api.inherit('Page of testing scenarios', pagination, {
    'items': fields.List(fields.Nested(testing_scenario))
})

page_of_testing_steps = api.inherit('Page of testing steps', pagination, {
    'items': fields.List(fields.Nested(testing_step))
})

feature = api.model('Feature', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a testing feature'),
    'name': fields.String(required=True, description='Feature name'),
    'description': fields.String(required=True, description='Feature descriptions')
})

feature_with_scenarios = api.inherit('Testing feature with posts', testing_scenario, {
    'scenarios': fields.List(fields.Nested(testing_scenario))
})
