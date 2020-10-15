from app.models import User
import json


def test_signup(client, database, new_user):
    response = client.post("/signup", json=new_user)
    data = json.loads(response.get_data(as_text=True))
    assert new_user["first_name"] == (User.query.filter_by(id=1).first()).to_dict["first_name"]
    assert new_user["last_name"] == (User.query.filter_by(id=1).first()).to_dict["last_name"]
    assert new_user["username"] == (User.query.filter_by(id=1).first()).to_dict["username"]
    assert new_user["email"] == (User.query.filter_by(id=1).first()).to_dict["email"]
    assert int(json.loads(response.get_data())["id"]) == (User.query.filter_by(id=1).first()).to_dict["id"]
    assert response.status_code == 201
