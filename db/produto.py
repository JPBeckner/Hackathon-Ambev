from .dao import DaoConnectionFactory
from .dao import BaseDAO
class ProdutoDAO:

    def __init__(self, Conn: DaoConnectionFactory):
        super().__init__(Conn)
