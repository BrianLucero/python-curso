from Articulos import Articulos
class Notebook(Articulos):
    _mRam = None
    _procesador = None

    def __init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color,mRam, procesador):
        Articulos.__init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color)
        self._mRam = mRam
        self._procesador = procesador

    def getMram(self):
        return self._mRam

    def setMram(self, mRam):
        self._mRam = mRam

    def getProcesador(self):
        return self._procesador
    
    def setProcesador(self, procesador):
        self._procesador = procesador
    def compro(self):
        return "notebook comprada"
    def __str__(self):
        return "id categoria: " + str(self._idCategoria) + " | nombre categoria: " + self._nombreCategoria + " | descripcion categoria: " + self._descripcionCategoria + " | lista de productos: " + str(self._listaProductos) + " | id categoria: " + str(self._idCategoria) + " | nombre de Articulo: " + self._nomArt + " | descripcion del articulo: " + self._dArt + " | lista de articulos: " + str(self._lArticulos) + " | id: " + str(self._id) + " | tamaño: " + self._tamanio + " | marca: " + self._marca + " | color :" + self._color + " | ram: " + str(self._mRam) + " | procesador: " + str(self._procesador)