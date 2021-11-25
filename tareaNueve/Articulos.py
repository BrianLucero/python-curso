from Categorias import Categorias
class Articulos(Categorias):
    _id = None
    _tamanio = None
    _marca = None
    _color = None

    def __init__(self, iC, nC, dC, lP, idCat,  nomArt, dArt, lArt, id, tamanio, marca, color): 
        Categorias.__init__(self,iC,nC,dC,lP,idCat, nomArt, dArt,lArt) 
        self._id = id
        self._tamanio = tamanio
        self._marca = marca
        self._color = color

    def getIdArt(self):
        return self._id
    
    def setIdArt(self, id):
        self._id = id
    
    def getTamanio(self):
        return self._tamanio
    
    def setTamanio(self, tamanio):
        self._tamanio = tamanio

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getColor(self):
        return self._color
    
    def setColor(self, color):
        self._color = color
    

