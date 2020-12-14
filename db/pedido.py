from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Pedido
class PedidoDAO(BaseDAO):
    
   TABLE = "Pedido"
   COLUMNS = "id_pedido, NFe"

   def __init__(self, Conn: DaoConnectionFactory.get_connection):
        super().__init__(Conn)
    
   def executa_query(self, sQuery: str):
      listReturn = []
      for tupla in super().executa_query(self, sQuery):
         pedido = Pedido()
         
         pedido.setIdPedido(pedido[0])
         pedido.setNfe(pedido[1])
         
         listReturn.append(pedido)
            
      return listReturn
