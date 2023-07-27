import os


"""
Setup of Config Files - Database Details, Secret Key, etc
"""

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'_jhhjvhfyy67:gu7t7gggh'

    try:
        POSTGRES_HOST = os.environ['POSTGRES_HOST']
        POSTGRES_USER = os.environ['POSTGRES_USER']
        POSTGRES_PORT = os.environ['POSTGRES_PORT']
        POSTGRES_DB = os.environ['POSTGRES_DB']
        POSTGRES_PASSWORD = os.environ['PGPASSWORD']

        SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"\
            or 'sqlite:///' + os.path.join(basedir, '../weatherApp.db')
    except:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../weatherApp.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
