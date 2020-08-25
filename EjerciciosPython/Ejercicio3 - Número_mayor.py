print("=========================================================================")
print("Programa para determinar cual es el número mas grande entre tres numeros")
print("=========================================================================")

numeroUno = int(input("\nIngresa el primer número:\n"))
numeroDos = int(input("Ingresa el segundo número:\n"))
numeroTres = int(input("Ingresa el tercer número:\n"))

if numeroUno > numeroDos and numeroUno > numeroTres:
    print("El numero ",str(numeroUno), "es el número más grande de los tres")
else:
    if numeroUno > numeroTres:
        print("El numero ",str(numeroDos), "es el número más grande de los tres")
    else:
        print("El numero ",str(numero), "es el número más grande de los tres")
