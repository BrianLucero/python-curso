from Articulos import Articulos
class SmartTY(Articulos):
    _pulgadas = None

    def __init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, marca,color, pulgadas):
        Articulos.__init__(self, iC, nC, dC, lP, idCat, nomCat, Dcat, lProd, idArt, tamanio, color, marca)
        self._pulgadas = pulgadas
   
    def getPulgadas(self):
        return self._pulgadas

    def setPulgadas(self, pulgadas):
        self._pulgadas = pulgadas
    def compro(self):
        return "smart tv comprada"
    def __str__(self):
        return "id categoria: " + str(self._idCategoria) + " | nombre categoria: " + self._nombreCategoria + " | descripcion categoria: " + self._descripcionCategoria + " | lista de productos: " + str(self._listaProductos) + " | id categoria: " + str(self._idCategoria) + " | nombre de Articulo: " + self._nomArt + " | descripcion del articulo: " + self._dArt + " | lista de articulos: " + str(self._lArticulos) + " | id: " + str(self._id) + " | tamaño: " + self._tamanio + " | marca: " + self._marca + " | color: " + self._color + " | pulgadas: " + str(self._pulgadas)

