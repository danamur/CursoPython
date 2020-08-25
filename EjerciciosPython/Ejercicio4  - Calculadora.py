print("Calculadora con una sola variable")
print("=====================")
print("menu de opciones")
print("=====================\n")

print("1)Suma \n2)Resta \n3)Multiplicación \n4)División \n5)División entera \n6)Exponente \n7)Modulo o resto\n")

numeroIngresado = int(input())

if numeroIngresado == 1:
    numeroIngresado = int(input("Ingrese el primer numero para Sumar\n"))
    numeroIngresado += int(input("Ingrese el segundo numero a Sumar\n"))
    print("El resultado de la Suma es ",numeroIngresado)

elif numeroIngresado == 2:
    numeroIngresado = int(input("Ingrese el primer numero para Restar\n"))
    numeroIngresado -= int(input("Ingrese el segundo numero a Restar\n"))
    print("El resultado de la Resta es ",numeroIngresado)

elif numeroIngresado == 3:
    numeroIngresado = int(input("Ingrese el primer numero para Multiplicación\n"))
    numeroIngresado *= int(input("Ingrese el segundo numero a Multiplicación\n"))
    print("El resultado de la Multipliación es ",numeroIngresado)

elif numeroIngresado == 4:
    numeroIngresado = int(input("Ingrese el primer numero para División\n"))
    numeroIngresado /= int(input("Ingrese el segundo numero a División\n"))
    print("El resultado de la División es ",numeroIngresado)

elif numeroIngresado == 5:
    numeroIngresado = int(input("Ingrese el primer numero para División Entera\n"))
    numeroIngresado //= int(input("Ingrese el segundo numero a División Entera\n"))
    print("El resultado de la División Entera es ",numeroIngresado)

elif numeroIngresado == 6:
    numeroIngresado = int(input("Ingrese el primer numero para Exponente\n"))
    numeroIngresado **= int(input("Ingrese el segundo numero a Exponente\n"))
    print("El resultado de la Exponente es ",numeroIngresado)

elif numeroIngresado == 7:
    numeroIngresado = int(input("Ingrese el primer numero para el Modulo\n"))
    numeroIngresado %= int(input("Ingrese el segundo numero a Modulo\n"))
    print("El resultado del Modulo es ",numeroIngresado)

else:
    print("Opcion no valida")
