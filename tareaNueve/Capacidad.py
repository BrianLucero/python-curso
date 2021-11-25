class Capacidad:
    __cLitros = None

    def __init__(self, cL):
        self.__cLitros = cL
    
    def getCLitros(self):
        return self.__cLitros

    def setCLitros(self, cL):
        self.__cLitros = cL
