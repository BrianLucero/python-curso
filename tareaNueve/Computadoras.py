from Articulos import Articulos
class Computadoras(Articulos):
    _mouse = None
    _teclado = None
    _memoria = None

    def __init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color, mouse, teclado, memoria):
        Articulos.__init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color)
        self._mouse = mouse
        self._teclado = teclado 
        self._memoria = memoria
    
    def getMouse(self):
        return self._mouse
    
    def setMouse(self, mouse):
        self._mouse = mouse
    
    def getTeclado(self):
        return self._teclado

    def setTeclado(self, teclado):
        self._teclado = teclado

    def getMemoria(self):
        return self._memoria
    
    def setMemoria(self, memoria):
        self._memoria = memoria
    def compro(self):
        return "computadora comprada"
    def __str__(self):
        return "id categoria: " + str(self._idCategoria) + " | nombre categoria: " + self._nombreCategoria + " | descripcion categoria: " + self._descripcionCategoria + " | lista de productos: " + str(self._listaProductos) + " | id categoria: " + str(self._idCategoria) + " | nombre de Articulo: " + self._nomArt + " | descripcion del articulo: " + self._dArt + " | lista de articulos: " + str(self._lArticulos) + " | id: " + str(self._id) + " | tamaño: " + self._tamanio + " | marca: " + self._marca + " | color :" + self._color + " | mouse: " + self._mouse + " | teclado: " + self._teclado + " | memoria: " + str(self._memoria)