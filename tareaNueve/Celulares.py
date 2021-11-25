from Articulos import Articulos
class Celulares(Articulos):
    _memoria = None

    def __init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color, mem):
        Articulos.__init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color)
        self._memoria = mem

    def getMarca(self):
        return self._memoria

    def setMarca(self, mem):
        self._memoria = mem
    def compro(self):
        return "celular comprado"
    def __str__(self):
        return "id categoria: " + str(self._idCategoria) + " | nombre categoria: " + self._nombreCategoria + " | descripcion categoria: " + self._descripcionCategoria + " | lista de productos: " + str(self._listaProductos) + " | id categoria: " + str(self._idCategoria) + " | nombre de Articulo: " + self._nomArt + " | descripcion del articulo: " + self._dArt + " | lista de articulos: " + str(self._lArticulos) + " | id: " + str(self._id) + " | tamaño: " + self._tamanio + " | marca: " + self._marca + " | color: " + self._color + " | memoria: " + str(self._memoria)
