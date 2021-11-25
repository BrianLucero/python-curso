from Sector import Sector
class Categorias(Sector):
    _idCategoria = None
    _nomArt = None
    _dArt = None
    _lArticulos = None

    def __init__(self, iC, nC, dC, lP, idCat, nomArt, dArt, lArt):
        Sector.__init__(self,iC,nC,dC,lP)
        self._idCategoria = idCat
        self._nomArt = nomArt
        self._dArt = dArt
        self._lArticulos = lArt

    def getIdCategoria(self):
        return self._idCategoria
    
    def setIdCategoria(self, idCat):
        self._idCategoria = idCat

    def getNomArt(self):
        return self._nomArt
    
    def setNomArt(self, nomArt):
        self._nomArt = nomArt

    def getDArt(self):
        return self._dArt

    def setDArt(self, dArt):
        self._dArt = dArt

    def getLAriculos(self):
        return self._lArticulos
    
    def setLProductos(self, lArt):
        self._lArticulos = lArt
    
    

    





