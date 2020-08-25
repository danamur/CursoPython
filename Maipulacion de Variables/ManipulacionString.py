print("mi primera manipulacion de String en Python")
mensaje = "Hola"
mensaje += " "
mensaje += "Daniel"
print(mensaje)

print(" ")

print("Otra forma de concatenar String en Python")
saludo = "Hola"
espacio = " "
nombre = "Daniel"
print(saludo + espacio + nombre)

print(" ")

print("Concatenacion de String + Numeros")
numeroUno = 4
numeroDos = 6
resultado = numeroUno + numeroDos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print(" ")

print("Metodo find")
mensaje = "Hola Daniel"
buscarSubcadena = mensaje.find("Daniel")
print(buscarSubcadena)

print(" ")

print("Extraccion en python")
mensaje = "Hola Daniel"
extraerSubcadena = mensaje [1:8]
print(extraerSubcadena)

print(" ")

print("Comparacion en Python")
mensajeUno = "Hola"
mensajeDos = "Hola"
print (mensajeUno == mensajeDos)
