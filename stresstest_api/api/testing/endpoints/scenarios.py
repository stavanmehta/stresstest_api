import logging

from flask import request
from flask_restplus import Resource
from stresstest_api.api.testing.business import create_testing_scenario, update_scenario, delete_scenario
from stresstest_api.api.testing.serializers import testing_scenario, page_of_testing_scenarios
from stresstest_api.api.testing.parsers import pagination_arguments
from stresstest_api.api.restplus import api
from stresstest_api.database.models import Scenario

log = logging.getLogger(__name__)

ns = api.namespace('testing/scenarios', description='Operations related to testing scenarios')


@ns.route('/')
class ScenariosCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_testing_scenarios)
    def get(self):
        """
        Returns list of testing scenarios.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        scenarios_query = Scenario.query
        scenarios_page = scenarios_query.paginate(page, per_page, error_out=False)

        return scenarios_page

    @api.expect(testing_scenario)
    def scenario(self):
        """
        Creates a new testing scenario.
        """
        create_testing_scenario(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Scenario not found.')
class ScenarioItem(Resource):

    @api.marshal_with(testing_scenario)
    def get(self, id):
        """
        Returns a testing scenario.
        """
        return Scenario.query.filter(Scenario.id == id).one()

    @api.expect(testing_scenario)
    @api.response(204, 'Scenario successfully updated.')
    def put(self, id):
        """
        Updates a testing scenario.
        """
        data = request.json
        update_scenario(id, data)
        return None, 204

    @api.response(204, 'Scenario successfully deleted.')
    def delete(self, id):
        """
        Deletes testing scenario.
        """
        delete_scenario(id)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class ScenariosArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_testing_scenarios)
    def get(self, year, month=None, day=None):
        """
        Returns list of testing scenarios from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        scenarios_query = Scenario.query.filter(Scenario.pub_date >= start_date).filter(Scenario.pub_date <= end_date)

        scenarios_page = scenarios_query.paginate(page, per_page, error_out=False)

        return scenarios_page
