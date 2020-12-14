from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Produto
class ProdutoDAO(BaseDAO):

   TABLE = "Produto"
   COLUMNS = "id_produto, descricao, preco"

   def __init__(self, Conn: DaoConnectionFactory.get_connection):
        super().__init__(Conn)
    
   def executa_query(self, sQuery: str):
      listReturn = []
      for tupla in super().executa_query(self, sQuery):
         produto = Produto()
         
         produto.setIdPedido(tupla[0])
         produto.setDescricao(tupla[1])
         produto.setPreco(tupla[2])
         
         listReturn.append(produto)
            
      return listReturn
