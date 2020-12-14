from .dao import DaoConnectionFactory
from .base_dao import BaseDAO
from models import Usuario


class UsuarioDAO(BaseDAO):

    TABLE = "Cliente"
    COLUMNS = "id_cliente, razao_social, cnpj"

    def __init__(self, conn: DaoConnectionFactory):
        super().__init__(conn)

    def clientes(self):
        query = f"SELECT {self.COLUMNS} FROM {self.TABLE}"
        return self.executa_query(query)

    def executa_query(self, query: str):
        list_return = []
        for tupla in super().executa_query(query):
            usuario = Usuario()

            usuario.setIdCliente = tupla[0]
            usuario.setRazaoSocial = tupla[1]
            usuario.setCnpj = tupla[2]

            list_return.append(usuario)

        return list_return
