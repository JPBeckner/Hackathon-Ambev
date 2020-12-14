

class Session:
    
    def __init__(self):
        __IdSession = ""
        __timestamp = ""
        __IdUser = ""
    
    def getIdSession(self):
        return self.__IdSession
    
    def setIdSession(self, IdSession):
        self.__IdSession = IdSession
        
    def gettimestamp(self):
        return self.__timestamp
    
    def settimestamp(self, timestamp):
        self.__timestamp = timestamp
        
    def getIdUser(self):
        return self.__IdUser
    
    def setIdUser(self, IdUser):
        self.__IdUser = IdUser