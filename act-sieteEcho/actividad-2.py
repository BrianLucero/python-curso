pedido = {}
total = 0

print(" --- Gestor de Pedidos --- ")
nombre = input("Ingresa tu nombre : ")
nombre = nombre.capitalize()
print("Bienvenido", nombre )

condicion = "si"
while(condicion == "si"):
    producto = str(input("Agrega un producto "))
    precio = int(input("Agrega el precio "))
    pedido[producto] = precio
    total = total + precio
    condicion = str(input("seguir agregando lista si o ( no ) para salir "))
print(pedido)
print("El total es: ", total)

