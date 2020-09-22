#Realizar una multiplicacion sin utilizar el simbolo de multiplicación

a = 4
b = 8
resultado = 0

for i in range(b):
    resultado += a

print(resultado)

#Ingresar nombre y apellido e imprimirlos al reves

nombre = 'Nicolas'
apellido = 'Feliz'

concatenacion = nombre + ' ' + apellido
print(concatenacion[::-1])

#Escribir una función que encuentren el elemento menor de una lista

lista = [1,3,5,55,12,-13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)

#Escribir una funcion que devuelve el volumen de una esfera por su radio

def CalcularVolumen(r):
    return 4/ 3 * 3.14 * r **3

resultado = CalcularVolumen(6)
print(resultado)