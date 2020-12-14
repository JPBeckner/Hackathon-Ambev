from models.pedidos_data import Pedidos_Data
from time import time
from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Cronograma

from datetime import timedelta, date

from models import Pedidos_Data

class CronogramaDAO(BaseDAO):
    
    TABLE = "Cronograma"
    COLUMNS = "id_cronograma, quantidade, data_saida, data_entrega, id_transporte, id_local_entrega, id_pedido"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)
        
    def getPrevisao(self, weekToPreview : int):
        total_sum = 0;
        older_day = date.today - timedelta(weeks=weekToPreview)
        
        sQuery = f"SELECT SUM(quantidade) FROM {self.TABLE} WHERE DATA_ENTREGA BETWEEN {older_day} AND {date.today}"
        for sum in super().executa_query(sQuery):
            total_sum += sum[0]
        
        total_sum /= (weekToPreview * 5) #Divide o total de semanas por 5 (Dias uteis) para saber a media por dia
        
        return total_sum
    
    def getCodProdQuantidade(self, dateToSearch):      
        sQuery = f"SELECT Produto.descricao, Cronograma.quantidade, Cronograma.id_pedido FROM (Cronograma INNER JOIN Produto ON Cronograma.id_produto = Produto.id_produto)"
        
        listToReturn = []
        
        for dado in super().executa_query(sQuery):
            dadoToReturn = Pedidos_Data(nomeProduto=dado[0], quantidadeProduto=dado[1], idPedido=dado[2])
            listToReturn.append(dadoToReturn)
            
        return listToReturn

    def get_cronogramas_por_data(self, data: str):
        query = f"SELECT {self.COLUMNS} FROM {self.TABLE}"
        return self.executa_query(query)

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
