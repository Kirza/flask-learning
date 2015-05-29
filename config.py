import os


# default config
class BaseConfig(object):
    SECRET_KEY = '\xd4\x82b\xd8\xe1\x11\xf1\xaf\x1e\xf2\xf5\xb9\xe9>\x0c-cZ\x87\xcdy\x99@L'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    # print SQLALCHEMY_DATABASE_URI

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
