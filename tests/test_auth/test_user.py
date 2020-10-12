from app.models import User
import json


def test_signup(app, database):
    db = database
    response = app.test_client().post(
        "/signup",
        json={
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'john.smith',
            'email': 'john.smith@gmail.com',
            'password': 'password'
        }
    )
    data = json.loads(response.get_data(as_text=True))
    assert data["id"] == str(User.query.filter_by(id=1).first().to_dict()["id"])
    assert response.status_code == 200
