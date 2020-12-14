from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import ProdutoPedido


class ProdutoPedidoDAO(BaseDAO):
    TABLE = "Produto_Pedido"
    COLUMNS = "idProduto_Pedido, id_produto, id_pedido, quantidade"

    def __init__(self, conn: DaoConnectionFactory.get_connection):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            produto_pedido = ProdutoPedido()

            produto_pedido.setIdPedido(tupla[0])
            produto_pedido.setIdProduto(tupla[1])
            produto_pedido.setIdPedido(tupla[2])
            produto_pedido.setQuantidade(tupla[3])

            list_return.append(produto_pedido)

        return list_return
