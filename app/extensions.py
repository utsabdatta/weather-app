from logging.config import dictConfig
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


"""
Basic Initialization of SQLAlchemy, CSRF and logging Config
"""

db = SQLAlchemy()
csrf = CSRFProtect()

log_level = "DEBUG"
LOGFILENAME = "weatherApp.log"

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] {%(pathname)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s',
    }},
    'handlers': {'default': {
                'level': 'DEBUG',
                'formatter': 'default',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOGFILENAME,
                'maxBytes': 5000000,
                'backupCount': 10
            }},
    'root': {
        'level': log_level,
        'handlers': ['default']
    }
})
