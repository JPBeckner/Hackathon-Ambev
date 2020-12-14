from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import TipoTransporte


class TipoTransporteDAO(BaseDAO):
    TABLE = "Tipo_Transporte"
    COLUMNS = "id_Tipo_Transporte, tipo, descricao"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            transporte = TipoTransporte()

            transporte.setIdTipoTransporte(tupla[0])
            transporte.setTipo(tupla[1])
            transporte.setDescricao(tupla[2])

            list_return.append(transporte)

        return list_return
