from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Pedido


class PedidoDAO(BaseDAO):

    TABLE = "Pedido"
    COLUMNS = "id_pedido, NFe"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            pedido = Pedido()

            pedido.setIdPedido(tupla[0])
            pedido.setNfe(tupla[1])

            list_return.append(pedido)

        return list_return
