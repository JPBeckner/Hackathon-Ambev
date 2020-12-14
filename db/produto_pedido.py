from .dao import DaoConnectionFactory
<<<<<<< Updated upstream
from .base_dao import BaseDAO


class ProdutoPedidoDAO(BaseDAO):

    def __init__(self, conn: DaoConnectionFactory.get_connection):
        super().__init__(conn)
        pass
=======
from .dao import BaseDAO
from models import ProdutoPedido
class ProdutoPedidoDAO:

   TABLE = "Produto_Pedido"
   COLUMNS = "idProduto_Pedido, id_produto, id_pedido, quantidade"

   def __init__(self, Conn: DaoConnectionFactory):
        super().__init__(Conn)
    
   def executa_query(self, sQuery: str):
      listReturn = []
      for tupla in super().executa_query(self, sQuery):
         produto_pedido = ProdutoPedido()
         
         produto_pedido.setIdPedido(tupla[0])
         produto_pedido.setIdProduto(tupla[1])
         produto_pedido.setIdPedido(tupla[2])
         produto_pedido.setQuantidade(tupla[3])
         
         listReturn.append(produto_pedido)
            
      return listReturn
>>>>>>> Stashed changes
