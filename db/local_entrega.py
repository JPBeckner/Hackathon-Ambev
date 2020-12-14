from .dao import DaoConnectionFactory
from .BaseDAO import BaseDAO
from models import LocalEntrega
class LocalEntregaDAO:

   TABLE = "Local_Enterga"
   COLUMNS = "id_local_entrega, codigo, descricao, endereco, id_cliente"

   def __init__(self, Conn: DaoConnectionFactory):
        super().__init__(Conn)
    
   def executa_query(self, sQuery: str):
      listReturn = []
      for tupla in super().executa_query(self, sQuery):
         local = LocalEntrega()
         
         local.setIdLocalEntrega(tupla[0])
         local.setCodigo(tupla[1])
         local.setDescricao(tupla[2])
         local.setEndereco(tupla[3])
         local.setIdCliente(tupla[4])
         
         listReturn.append(local)
            
      return listReturn
