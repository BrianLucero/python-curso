codigos = [143,568,991,321]
val = [("Disco rígido SSD",5000), ("Mouse inalámbrico",800), ("Teclado bluetooth",1000), ("Memoria 8GB",5000)]
dic = dict(zip(codigos, val))

pedido = []

print(" --- Gestor de Pedidos --- ")
nombre = input("Ingresa tu nombre : ")
nombre = nombre.capitalize()
print("Bienvenido", nombre )
cod = list(dic.keys())

print("Lista de codigo")
for i in range(len(codigos)):
     print(codigos[i])
existeC = int(input( "Ingrese el codigo  o  ( -1 ) Para salir "))
while(existeC != -1):
     if(existeC not in cod):
          print("----------")
          print("El codigo no existe")
          print("----------")
     else:
          datosAInsertar = dic.get(existeC)
          pedido.append(datosAInsertar)
          print("----------")
          print("Producto cargado con éxito")
          print("----------")
          for i in range(len(codigos)):
              print(codigos[i])
     existeC = int(input( "Ingrese el codigo o  ( -1 ) Para salir "))
     
print("Tu pedido consiste de: ")

for elemento in pedido:
    print("Nombre del producto: ", elemento[0], " | Precio: ", elemento[1])
cod = list(dic.keys()) 




