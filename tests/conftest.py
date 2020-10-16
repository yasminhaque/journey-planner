import pytest

from app.app import create_app
from app.models import db, User
from app.schema import UserRegisterSchema


@pytest.fixture
def app():
    app = create_app("testing")
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

    yield db


@pytest.fixture
def new_user_model():
    return User(
        first_name="John",
        last_name="Smith",
        username="john.smith",
        email="john.smith@gmail.com",
        plaintext_password="password",
    )


@pytest.fixture
def new_user_register():
    return {
        "first_name": "John",
        "last_name": "Smith",
        "username": "john.smith",
        "email": "john.smith@gmail.com",
        "plaintext_password": "password"
    }


@pytest.fixture
def new_user_login():
    return {
        "username": "john.smith",
        "plaintext_password": "password123"
    }


@pytest.fixture
def user_schema():
    return UserRegisterSchema()