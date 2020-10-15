from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password = db.Column("password", db.String, nullable=False)

    def __init__(self, first_name, last_name, email, username, plaintext_password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = plaintext_password

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "username": self.username
        }

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = generate_password_hash(plaintext_password).decode('utf8')

    @hybrid_method
    def check_password(self, plaintext_password):
        return check_password_hash(self._password, plaintext_password)

    def save(self):
        db.session.add(self)
        db.session.commit()