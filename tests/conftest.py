import pytest

from app.app import create_app
from app.models import db


@pytest.fixture
def app():
    app = create_app("testing")

    return app


@pytest.fixture()
def database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

    yield db