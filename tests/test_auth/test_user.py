from app.models import User


def test_create_user(database):
    email = "john.smith@gmail.com"
    user = User(
        first_name="John",
        last_name="Smith",
        username="john.smith",
        email="john.smith@gmail.com"
    )
    database.session.add(user)
    database.session.commit()

    user = User.query.first()

    assert user.email == email