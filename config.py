class Config(object):
    DEBUG = False
    DATABASE_URI = 'sqlite:///default.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
