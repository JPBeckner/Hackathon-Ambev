from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Cliente


class ClienteDAO(BaseDAO):

    TABLE = "Cliente"
    COLUMNS = "id_cliente, razao_social, cnpj"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    @property
    def clientes(self):
        query = f"SELECT {self.COLUMNS} FROM {self.TABLE}"
        return self.executa_query(query)
    
    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            cliente = Cliente()
            
            cliente.setIdCliente = tupla[0]
            cliente.setRazaoSocial = tupla[1]
            cliente.setCnpj = tupla[2]
            
            list_return.append(cliente)
            
        return list_return
