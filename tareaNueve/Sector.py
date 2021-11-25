#                                                         https://github.com/BrianLucero/Python.git
class Sector:
    _idCategoria = None
    _nombreCategoria = None
    _descripcionCategoria = None
    _listaProductos = None

    def __init__(self, iC, nC, dC, lP):
        self._idCategoria = iC
        self._nombreCategoria = nC
        self._descripcionCategoria = dC
        self._listaProductos = lP
    
    def getIdCategoria(self):
        return self._idCategoria 

    def setIdCategoria(self,idCategoria):
        self._idCategoria = idCategoria
    
    def getNombreCategoria(self):
        return self._nombreCategoria
    
    def setNombreCategoria(self,nombreCategoria):
        self._nombreCategoria = nombreCategoria

    def getDescripcionCategoria(self):
        return self._descripcionCategoria
    
    def setDescripcionCategoria(self,descripcionCategoria):
        self._descripcionCategoria = descripcionCategoria
    
    def getListaProductos(self):
        return self._listaProductos

    def setListaProductos(self,listaProductos):
        self._listaProducto = listaProductos
    def compro(self):
        return "Estoy comprando ... "
    def nCom(self):
        return "no comprada"

    

    

