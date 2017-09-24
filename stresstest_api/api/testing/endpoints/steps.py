import logging

from flask import request
from flask_restplus import Resource
from stresstest_api.api.testing.business import create_scenario, update_scenario, delete_scenario, create_step, \
    update_step, delete_step
from stresstest_api.api.testing.serializers import testing_scenario, page_of_testing_scenarios, testing_step, page_of_testing_steps
from stresstest_api.api.testing.parsers import pagination_arguments
from stresstest_api.api.restplus import api
from stresstest_api.database.models import Step

log = logging.getLogger(__name__)

ns = api.namespace('steps', description='Operations related to testing steps')


@ns.route('/')
class StepsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_testing_steps)
    def get(self):
        """
        Returns list of testing step.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 20)

        step_query = Step.query
        steps_page = step_query.paginate(page, per_page, error_out=False)

        return steps_page

    @api.response(201, 'Step successfully added.')
    @api.expect(testing_step)
    def post(self):
        """
        Creates a new testing step.
        """
        data = request.json
        create_step(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Step not found.')
class StepItem(Resource):

    @api.marshal_with(testing_step)
    def get(self, id):
        """
        Returns a testing step.
        """
        return Step.query.filter(Step.id == id).one()

    @api.expect(testing_step)
    @api.response(204, 'Step successfully updated.')
    def put(self, id):
        """
        Updates a testing step.
        """
        data = request.json
        update_step(id, data)
        return None, 204

    @api.response(204, 'Scenario successfully deleted.')
    def delete(self, id):
        """
        Deletes testing step.
        """
        delete_step(id)
        return None, 204
