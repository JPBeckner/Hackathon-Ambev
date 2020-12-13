import logging
from os.path import abspath, dirname

# file_path = dirname(__name__)
file_path = abspath(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filename': f'{file_path}/server.log'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{file_path}/server.log',
        }
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

        self.__logger = logging.LoggerAdapter(logging.getLogger(self.__name), extra={'server': 'teste'})

    @property
    def logger(self) -> logging.LoggerAdapter:
        return self.__logger
