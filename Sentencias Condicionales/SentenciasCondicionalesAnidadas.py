print("============")
print("Conversor")
print("============ \n")

print("Menu de opciones \n")

print("Presione 1 para convertir de numero a palabras.")
print("Presione 2 para convertir de de palabras numero. \n")

opcion = int(input("¿Cual es tu opción deseada?: "))

if opcion == 1:
    print("\n Conversor de numero a palabras. \n")
    
    opcionUno = int(input("¿Cual es el numero que sea converitr a palabras?: "))

    if opcionUno == 1:
        print("El numero es 'Uno'")

    elif opcionUno == 2:
        print("El numero es 'Dos'")

    elif opcionUno == 3:
        print("El numero es 'Tres'")

    elif opcionUno == 4:
        print("El numero es 'Cuatro'")

    else:
        print("Opcion aun no valida")
    
elif opcion == 2:
    print("\n Conversor de palabras a numeros \n")

    opcionDos = input("Escribe en palabras el numero que quieres convertir a palabras: ")
    
    if opcionDos == "uno" or opcionDos == "Uno" or opcionDos == "UNO":
        print("El numero es '1'")

    elif opcionDos == "dos" or opcionDos == "Dos" or opcionDos == "DOS":
        print("El numero es '2'")

    elif opcionDos == "tres" or opcionDos == "Tres" or opcionDos == "TRES":
        print("El numero es '3'")

    elif opcionDos == "cuatro" or opcionDos == "Cuatro" or opcionDos == "CUATRO":
        print("El numero es '4'")

    else:
        print("Opcion aun no valida")

else:
    print("Opcion no disponible")
