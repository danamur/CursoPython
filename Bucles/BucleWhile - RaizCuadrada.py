import math

print("-------------------------------------------")
print("| Programa de cálculo de la raíz cuadrada |")
print("-------------------------------------------\n")

numero = int(input("Introduce un número por favor: \n"))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intento == 2:
        print("Has consumido demasiados intentos. El programa ha finalaizado")
        break;
    numero = int(input("Introduce un número por favor:\n"))
    if numero < 0:
        intento += 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es ",solucion)
