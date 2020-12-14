from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Produto


class ProdutoDAO(BaseDAO):

    TABLE = "Produto"
    COLUMNS = "id_produto, descricao, preco"

    def __init__(self, conn: DaoConnectionFactory.get_connection):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            produto = Produto()

            produto.setIdProduto(tupla[0])
            produto.setDescricao(tupla[1])
            produto.setPreco(tupla[2])

            list_return.append(produto)

        return list_return
