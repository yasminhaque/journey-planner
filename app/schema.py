from app.models import User
from marshmallow import Schema, post_load
from marshmallow.validate import Length
from marshmallow.fields import Str, Email
from typing import Dict


class UserRegisterSchema(Schema):
    first_name = Str(required=True, validate=Length(min=1))
    last_name = Str(required=True, validate=Length(min=1))
    email = Email(required=True, validate=Length(min=1))
    username = Str(required=True, validate=Length(min=1, max=15))
    plaintext_password = Str(required=True, validate=Length(min=1, max=15))

    @post_load
    def create_user(self, data: Dict, **kwargs) -> User:
        return User(**data)