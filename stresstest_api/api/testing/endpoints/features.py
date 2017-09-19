import logging

from flask import request
from flask_restplus import Resource
from stresstest_api.api.testing.business import create_feature, delete_feature, update_feature
from stresstest_api.api.testing.serializers import feature, feature_with_scenarios
from stresstest_api.api.restplus import api
from stresstest_api.database.models import Feature

log = logging.getLogger(__name__)

ns = api.namespace('features', description='Operations related to testing features')


@ns.route('/')
class FeatureCollection(Resource):

    @api.marshal_list_with(feature)
    def get(self):
        """
        Returns list of testing features.
        """
        features = Feature.query.all()
        return features

    @api.response(201, 'Feature successfully created.')
    @api.expect(feature)
    def post(self):
        """
        Creates a new testing feature.
        """
        data = request.json
        create_feature(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Feature not found.')
class FeatureItem(Resource):

    @api.marshal_with(feature_with_scenarios)
    def get(self, id):
        """
        Returns a feature with a list of posts.
        """
        return Feature.query.filter(Feature.id == id).one()

    @api.expect(feature)
    @api.response(204, 'Feature successfully updated.')
    def put(self, id):
        """
        Updates a testing feature.

        Use this method to change the name of a testing feature.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Feature Name"
        }
        ```

        * Specify the ID of the feature to modify in the request URL path.
        """
        data = request.json
        update_feature(id, data)
        return None, 204

    @api.response(204, 'Feature successfully deleted.')
    def delete(self, id):
        """
        Deletes testing feature.
        """
        delete_feature(id)
        return None, 204
