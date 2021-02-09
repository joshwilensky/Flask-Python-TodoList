import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class ProductionConfig(Config):
    MYSQL_DB = os.environ.get('DATABASE.URL')
    DEBUG = False

class DevelopmentConfig(Config):
    MYSQL_DB = 'py_todolist'
