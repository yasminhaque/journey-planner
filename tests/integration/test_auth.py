from app.models import User
import json


def test_register(client, database, new_user_register):
    response = client.post("/register", json=new_user_register)
    data = json.loads(response.get_data(as_text=True))
    assert new_user_register["first_name"] == (User.query.filter_by(id=1).first()).to_dict["first_name"]
    assert new_user_register["last_name"] == (User.query.filter_by(id=1).first()).to_dict["last_name"]
    assert new_user_register["username"] == (User.query.filter_by(id=1).first()).to_dict["username"]
    assert new_user_register["email"] == (User.query.filter_by(id=1).first()).to_dict["email"]
    assert int(json.loads(response.get_data())["id"]) == (User.query.filter_by(id=1).first()).to_dict["id"]
    assert response.status_code == 201


def test_login(client, database, new_user_login):
    response = client.post("/login", json=new_user_login)

