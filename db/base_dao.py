from .dao import DaoConnectionFactory


class BaseDAO:

    def __init__(self, conn: DaoConnectionFactory.get_connection):
        self.__conn = conn

    def executa_query(self, query: str):
        cursor = self.__conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
