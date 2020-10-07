import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
