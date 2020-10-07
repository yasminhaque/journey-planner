from flask import Flask


def create_app(config_name: str):

    app = Flask(__name__)

    config_module = f"app.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app