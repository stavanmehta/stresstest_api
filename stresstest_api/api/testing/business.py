from stresstest_api.database import db
from stresstest_api.database.models import Scenario, Feature #Step, StepRequest, StepValidation


def create_scenario(data):
    title = data.get('title')
    body = data.get('body')
    feature_id = data.get('feature_id')
    sequence = data.get('sequence')
    feature = Feature.query.filter(Feature.id == feature_id).one()
    scenario = Scenario(title, body, feature, sequence)
    db.session.add(scenario)
    db.session.commit()


def update_scenario(scenario_id, data):
    scenario = Scenario.query.filter(Scenario.id == scenario_id).one()
    scenario.title = data.get('title')
    scenario.body = data.get('body')
    feature_id = data.get('feature_id')
    scenario.sequence = data.get('sequence')
    scenario.feature = Feature.query.filter(Feature.id == feature_id).one()
    db.session.add(scenario)
    db.session.commit()


def delete_scenario(scenario_id):
    scenario = Scenario.query.filter(Scenario.id == scenario_id).one()
    db.session.delete(scenario)
    db.session.commit()

def create_feature(data):
    name = data.get('name')
    description = data.get('description')
    feature_id = data.get('id')

    feature = Feature(name, description)
    if feature_id:
        feature.id = feature_id

    db.session.add(feature)
    db.session.commit()

def update_feature(feature_id, data):
    feature = Feature.query.filter(Feature.id == feature_id).one()
    feature.name = data.get('name')
    db.session.add(feature)
    db.session.commit()


def delete_feature(feature_id):
    feature = Feature.query.filter(Feature.id == feature_id).one()
    db.session.delete(feature)
    db.session.commit()


#
# def create_step(data):
#     id = data.get('id')
#     sceanrio_id = data.get('sceanrio_id')
#     sceanrio = Scenario.query.filter(Scenario.id == sceanrio_id).one()
#
#     name = data.get('name')
#     sequence = data.get('sequence')
#     step_request = data.get('step_request')
#
#     step_validations = data.get('step_validations')
#
#
#     title = data.get('title')
#     body = data.get('body')
#     feature_id = data.get('feature_id')
#     feature = Feature.query.filter(Feature.id == feature_id).one()
#     step = Step(id, sceanrio, name, sequence, step_request, step_validations)
#     db.session.add(step)
#     db.session.commit()
#
#
# def update_step(step_id, data):
#     step = Step.query.filter(Step.id == step_id).one()
#     step.title = data.get('title')
#     step.body = data.get('body')
#     feature_id = data.get('feature_id')
#     step.feature = Feature.query.filter(Feature.id == feature_id).one()
#     db.session.add(step)
#     db.session.commit()
#
#
# def delete_step(step_id):
#     step = Step.query.filter(Step.id == step_id).one()
#     db.session.delete(step)
#     db.session.commit()
