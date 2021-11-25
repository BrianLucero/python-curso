from Sector import Sector
from Categorias import Categorias
from Articulos import Articulos
from Notebook import Notebook
from Computadoras import Computadoras
from SmartTV import SmartTY
from Heladeras import Heladeras
from Capacidad import Capacidad
from Celulares import Celulares
cap = Capacidad("300 litros")

heladera = Heladeras(1, "tienda electrodomesticos", "electrodomesticos", 55, 2, "Heladera", "heladera congelador gris grande", 3, 555, "grande", "LG","gris", cap)
print(heladera)
print("capacidad: ", cap.getCLitros())
print(heladera.getNomArt())
print(heladera.nCom())
print("------------------------------------------------------------------------------------------------------------------------------------------")

computadora = Computadoras(5, "tienda electrodomesticos", "electrodomesticos", 8, 4, "Computadoras", "computadora de escritorio negra", 5, 90, "mediano", "lenovo","negro", "mouse inalambrico ", "teclado inalambrico", "16 GB")
print(computadora)
print(computadora.getNomArt())
print(computadora.compro())
print("------------------------------------------------------------------------------------------------------------------------------------------")

notebook = Notebook(7, "tienda electrodomesticos", "electrodomesticos", 77, 54, "notebook", "notebook negra", 25, 590, "mediano", "HP","negro", "8 GB", "intel i7")
print(notebook)
print(notebook.getColor())
print(notebook.compro())
print("------------------------------------------------------------------------------------------------------------------------------------------")

celu = Celulares(99, "tienda electrodomesticos", "electrodomesticos", 20, 504, "celular", "celular grande gris", 105, 51, "grande", "Huawei","gris", "32 GB")
print(celu)
print(celu.getDescripcionCategoria())
print(celu.compro())
print("------------------------------------------------------------------------------------------------------------------------------------------")

tv = SmartTY(14, "tienda electrodomesticos", "electrodomesticos", 71, 104, "samart tv", "smart tv grande", 200, 65, "grande", "Sony","negro", "32 pulgadas")
print(tv)
print(tv.getTamanio())
print(tv.compro())
