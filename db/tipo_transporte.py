from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import TipoTransporte
class TipoTransporteDAO(BaseDAO):

   TABLE = "Tipo_Transporte"
   COLUMNS = "id_Tipo_Transporte, tipo, descricao"

   def __init__(self, Conn: DaoConnectionFactory.get_connection):
        super().__init__(Conn)
    
   def executa_query(self, sQuery: str):
      listReturn = []
      for tupla in super().executa_query(self, sQuery):
         tTransporte = TipoTransporte()
         
         tTransporte.setIdTipoTransporte(tupla[0])
         tTransporte.setTipo(tupla[1])
         tTransporte.setDescricao(tupla[2])
         
         listReturn.append(tTransporte)
            
      return listReturn