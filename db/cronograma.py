from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Cronograma


class CronogramaDAO(BaseDAO):
    
    TABLE = "Cronograma"
    COLUMNS = "id_cronograma, quantidade, data_saida, data_entrega, id_transporte, id_local_entrega, id_pedido"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            cron = Cronograma()
            
            cron.setIdCronograma(tupla[0])
            cron.setQuantidade(tupla[1])
            cron.setDataSaida(tupla[2])
            cron.setDataEntrega(tupla[3])
            cron.setIdTransporte(tupla[4])
            cron.setIdLocalEntrega(tupla[5])
            cron.setIdPedido(tupla[6])
            
            list_return.append(cron)
            
        return list_return
