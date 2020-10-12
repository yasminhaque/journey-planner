from flask import Blueprint, request
from app.models import db, User

auth = Blueprint('test_auth', __name__)


@auth.route('/login')
def login():
    return 'Login'


@auth.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    user = User(**body)
    user.save()
    return {'id': str(user.id)}, 200


@auth.route('/logout')
def logout():
    return 'Logout'