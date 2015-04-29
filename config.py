import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'KGB never sleeps'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
