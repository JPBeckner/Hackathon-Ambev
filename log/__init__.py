import logging
from os.path import abspath, dirname
from logging.config import dictConfig

# file_path = dirname(__name__)
file_path = abspath(__name__)

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} - [{module}] - {levelname}: {message}',  # {process:d} {thread:d}
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': f'{file_path}/server.log',
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },

    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'server': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


class Logger:

    def __init__(self, name: str = 'server'):
        self.__name = name
        dictConfig(DEFAULT_LOGGING)
        self.__logger = logging.LoggerAdapter(logging.getLogger(name), extra={'server': 'teste'})
        # self.__logger.setLevel('DEBUG')
        # self.__logger.f

    @property
    def logger(self) -> logging.LoggerAdapter:
        return self.__logger
