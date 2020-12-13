from .dao import DaoConnectionFactory
from .dao import BaseDAO
from models import Cronograma
class CronogramaDAO:
    
    TABLE = "Cronograma"
    COLUMNS = "id_cronograma, quantidade, data_saida, data_entrega, id_transporte, id_local_entrega, id_pedido"

    def __init__(self, Conn: DaoConnectionFactory):
        super().__init__(Conn)
    
    def executa_query(self, sQuery: str):
        listReturn = []
        for tupla in super().executa_query(self, sQuery):
            cron = Cronograma()
            
            cron.setIdCronograma(tupla[0])
            cron.setQuantidade(tupla[1])
            cron.setDataSaida(tupla[2])
            cron.setDataEntrega(tupla[3])
            cron.setIdTransporte(tupla[4])
            cron.setIdLocalEntrega(tupla[5])
            cron.setIdPedido(tupla[6])
            
            listReturn.append(cron)
            
        return listReturn
