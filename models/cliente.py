
class Cliente:

    def __init__(self):
        pass

    def getIdCliente(self):
        return self.__IdCliente

    def setIdCliente(self, idCliente):
        self.__IdCliente = idCliente

    def getRazaoSocial(self):
        return self.__RazaoSocial

    def setRazaoSocial(self, razaoSocial):
        self.__RazaoSocial = razaoSocial

    def getCnpj(self):
        return self.__Cnpj

    def setCnpj(self, cnpj):
        self.__Cnpj = cnpj
