from models import Transporte
from .dao import DaoConnectionFactory
from .base_dao import BaseDAO


class TransporteDAO(BaseDAO):

    TABLE = "Transporte"
    COLUMNS = "id_transporte, identificacao, id_tipo_transporte"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            transporte = Transporte()

            transporte.setIdTipoTransporte(tupla[0])
            transporte.setIdentificacao(tupla(1))
            transporte.setIdTipoTransporte(tupla[2])

            list_return.append(transporte)

        return list_return
