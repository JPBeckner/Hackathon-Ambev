from .dao import DaoConnectionFactory
from .dao import BaseDAO
from models import Cliente
class ClienteDAO(BaseDAO):

    TABLE = "Cliente"
    COLUMNS = "id_cliente, razao_social, cnpj"

    def __init__(self, Conn: DaoConnectionFactory):
        super().__init__(Conn)
    
    def executa_query(self, sQuery: str):
        listReturn = []
        for tupla in super().executa_query(self, sQuery):
            cliente = Cliente()
            
            cliente.setIdCliente = tupla[0]
            cliente.setRazaoSocial = tupla[1]
            cliente.setCnpj = tupla[2]
            
            listReturn.append(cliente)
            
        return listReturn
        
