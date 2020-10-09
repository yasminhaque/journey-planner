import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    USER = os.environ["POSTGRES_USER"]
    PASSWORD = os.environ["POSTGRES_PASSWORD"]
    HOSTNAME = os.environ["POSTGRES_HOSTNAME"]
    PORT = os.environ["POSTGRES_PORT"]
    DATABASE = os.environ["APPLICATION_DB"]
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
