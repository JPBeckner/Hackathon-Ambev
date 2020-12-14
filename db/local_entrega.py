from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import LocalEntrega


class LocalEntregaDAO(BaseDAO):

    TABLE = "Local_Enterga"
    COLUMNS = "id_local_entrega, codigo, descricao, endereco, id_cliente"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            local = LocalEntrega()

            local.setIdLocalEntrega(tupla[0])
            local.setCodigo(tupla[1])
            local.setDescricao(tupla[2])
            local.setEndereco(tupla[3])
            local.setIdCliente(tupla[4])

            list_return.append(local)

        return list_return
