from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from stresstest_api.database.models import Scenario, Feature  # noqa
    db.drop_all()
    db.create_all()