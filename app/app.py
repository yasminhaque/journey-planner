from flask import Flask


def create_app(config_name: str):

    app = Flask(__name__)

    config_module = f"app.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    from app.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth import auth
    from app.home import home
    app.register_blueprint(auth)
    app.register_blueprint(home)

    return app