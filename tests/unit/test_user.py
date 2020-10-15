import pytest
from marshmallow import ValidationError


def test_new_user_model(new_user_model):
    assert new_user_model.email == "john.smith@gmail.com"
    assert new_user_model.password != "password"
    assert new_user_model.check_password("password")
    assert new_user_model.first_name == "John"
    assert new_user_model.last_name == "Smith"


def test_empty_dict(user_schema):
    with pytest.raises(ValidationError):
        user_schema.load({})


def test_invalid_keys(user_schema):
    with pytest.raises(ValidationError):
        user_schema.load({
            "name": "Beth",
            "surname": "Bob"
        })


def test_password_length(user_schema, new_user):
    user = new_user["plaintext_password"] = "reallyreallyreallylongpassword"
    with pytest.raises(ValidationError):
        user_schema.load(user)
