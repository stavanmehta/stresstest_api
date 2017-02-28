from stresstest_api.database import db
from stresstest_api.database.models import Scenario, Feature


def create_testing_scenario(data):
    title = data.get('title')
    body = data.get('body')
    feature_id = data.get('feature_id')
    feature = Feature.query.filter(Feature.id == feature_id).one()
    scenario = Scenario(title, body, feature)
    db.session.add(scenario)
    db.session.commit()


def update_scenario(scenario_id, data):
    scenario = Scenario.query.filter(Scenario.id == scenario_id).one()
    scenario.title = data.get('title')
    scenario.body = data.get('body')
    feature_id = data.get('feature_id')
    scenario.feature = Feature.query.filter(Feature.id == feature_id).one()
    db.session.add(scenario)
    db.session.commit()


def delete_scenario(scenario_id):
    scenario = Scenario.query.filter(Scenario.id == scenario_id).one()
    db.session.delete(scenario)
    db.session.commit()


def create_feature(data):
    name = data.get('name')
    feature_id = data.get('id')

    feature = Feature(name)
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
