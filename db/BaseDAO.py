from .dao import DaoConnectionFactory

class BaseDAO:

    def __init__(self, conn: DaoConnectionFactory):
        self.__conn = conn

    def executa_query(self, sQuery: str):
        cursor = self.__conn.cursor()
        cursor.execute(sQuery)
        return cursor.fetchall()
    