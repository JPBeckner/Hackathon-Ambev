
class Usuario:

    def __init__(self):
        __IdUsuario = ""
        __username = ""
        __password = ""
        __create_time = ""
        __idColaborador = ""
    
    def getIdUsuario(self):
        return self.__IdUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
        
    def getUsername(self):
        return self.__username
    
    def setUsername(self, username):
        self.__username = username
        
    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password
        
    def getCreateTime(self):
        return self.__create_time
    
    def setCreateTime(self, createTime):
        self.__create_time = createTime
        
    def getIdColaborador(self):
        return self.__IdColaborador
    
    def setIdColaborador(self, idColaborador):
        self.__IdColaborador = idColaborador