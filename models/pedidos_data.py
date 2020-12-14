
class Pedidos_Data:
    
    def __init__(self,
                 idPedido,
                 nomeProduto,
                 quantidadeProduto):
        self.__idPedido = idPedido
        self.__nomeProduto = nomeProduto
        self.__quantidadeProduto = quantidadeProduto
        
    def getIdPedido(self):
        return self.__idPedido
    
    def getNomeProduto(self):
        return self.__nomeProduto
    
    def getQuantidadeProduto(self):
        return self.__quantidadeProduto
        