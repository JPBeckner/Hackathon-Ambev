from models import Transporte
from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
class TransporteDAO(BaseDAO):

   TABLE = "Transporte"
   COLUMNS = "id_transporte, identificacao, id_tipo_transporte"

   def __init__(self, Conn: DaoConnectionFactory.get_connection):
        super().__init__(Conn)
    
   def executa_query(self, sQuery: str):
      listReturn = []
      for tupla in super().executa_query(self, sQuery):
         transporte = Transporte()
         
         transporte.setIdTipoTransporte(tupla[0])
         transporte.setIdentificacao(tupla(1))
         transporte.setIdTipoTransporte(tupla[2])
         
         listReturn.append(transporte)
            
      return listReturn
