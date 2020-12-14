from models.transporte import Transporte
from .dao import DaoConnectionFactory
from .dao import BaseDAO
class TransporteDAO:

   TABLE = "Transporte"
   COLUMNS = "id_transporte, identificacao, id_tipo_transporte"

   def __init__(self, Conn: DaoConnectionFactory):
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
