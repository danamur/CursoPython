print("==================================================")
print("*Programa para determinar si un numero par o impar")
print("==================================================")

numero = int(input("\nPor favor ingrese un numero entero:\n"))

if numero % 2 == 0:
    print("El numero " + str(numero) + " ingresado es par")
else:
    print("El numero " + str(numero) + " ingresado es impar")
