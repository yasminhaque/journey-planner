from flask import Blueprint, request
from app.models import User
from app.schema import UserSchema
from marshmallow import ValidationError

user_schema = UserSchema()

auth = Blueprint('unit', __name__)


@auth.route('/login')
def login():
    return 'Login'


@auth.route('/signup', methods=['POST'])
def signup():
    try:
        user = user_schema.load(request.json)
    except ValidationError as error:
        return error.messages, 422

    if user is None:
        return {"message": "No input data provided or input data provided not in the correct json format"}, 400

    if User.query.filter_by(email=user.email).first():
        return {"message": "User already exists with this email"}
    else:
        user.save()
        return {"message": "Created new user.", "id": str(user.id)}, 201


@auth.route('/logout')
def logout():
    return 'Logout'