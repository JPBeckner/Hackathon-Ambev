from db import *
from flask_mysqldb import MySQL


class DaoConnectionFactory:

    _db = None

    def __init__(self, app):
        app.config['MYSQL_HOST'] = host
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = password
        app.config['MYSQL_DB'] = db_name
        app.config['MYSQL_PORT'] = port
        self._db = MySQL(app)

    @staticmethod
    def get_connection():
        return DaoConnectionFactory._db

