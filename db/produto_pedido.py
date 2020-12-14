from .dao import DaoConnectionFactory
from .base_dao import BaseDAO


class ProdutoPedidoDAO(BaseDAO):

    def __init__(self, conn: DaoConnectionFactory.get_connection):
        super().__init__(conn)
        pass
