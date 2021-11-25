from Articulos import Articulos
class Heladeras(Articulos):
    _capacidad = None

    def __init__(self, iC, nC, dC, lP, idCat,  nomArt, dArt, lArt, id, tamanio, marca,color, cap):
        Articulos.__init__(self, iC, nC, dC, lP, idCat,  nomArt, dArt, lArt, id, tamanio, marca, color)
        self._capacidad = cap

    def getCapacidad(self):
        return self._capacidad 

    def setCapacidad(self, cap):
        self._capacidad = cap
    def compro(self):
        return "heladera comprada"
    def nCom(self):
        return "heladera no comprada"
    def __str__(self):
        return "id categoria: " + str(self._idCategoria) + " | nombre categoria: " + self._nombreCategoria + " | descripcion categoria: " + self._descripcionCategoria + " | lista de productos: " + str(self._listaProductos) + " | id categoria: " + str(self._idCategoria) + " | nombre de Articulo: " + self._nomArt + " | descripcion del articulo: " + self._dArt + " | lista de articulos: " + str(self._lArticulos) + " | id: " + str(self._id) + " | tamaño: " + self._tamanio + " | marca: " + self._marca + " | color:" + self._color


    


    