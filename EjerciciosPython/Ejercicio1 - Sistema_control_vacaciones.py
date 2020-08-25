print("==================================")
print("Ejercicio 1 | Dias de vacaciones")
print("==================================")

nombre = input("¿Cual es tu Nombre?\n")

print("\nIngresa la clave de tu departamento")

claveDepartamento = int(input("\n1)Atencion al cliente. \n2)Logistica. \n3)Gerencia \n"))

print("\nIngresa la cantidad de años de servicios")

tiempoContrato = int(input("\n1)Menos de 2 años de servicios. \n2)Menos de 7 años de servicio. \n3)Mas de 7 años de servicios.\n"))

if claveDepartamento == 1:
    if tiempoContrato == 1:
        print("\n" + nombre + " tienes 6 días de vacaciones.")
    elif tiempoContrato == 2:
        print("\n" + nombre + " tienes 14 días de vacaciones.")
    elif tiempoContrato == 3:
        print("\n" + nombre + " tienes 20 días de vacaciones.")
    else:
        print("Opcion no valida.")

elif claveDepartamento == 2:
    if tiempoContrato == 1:
        print("\n" + nombre + " tienes 7 días de vacaciones.")
    elif tiempoContrato == 2:
        print("\n" + nombre + " tienes 15 días de vacaciones.")
    elif tiempoContrato == 3:
        print("\n" + nombre + " tienes 22 días de vacaciones.")
    else:
        print("Opcion no valida.")

elif claveDepartamento == 3:
    if tiempoContrato == 1:
        print("\n" + nombre + " tienes 10 días de vacaciones.")
    elif tiempoContrato == 2:
        print("\n" + nombre + " tienes 20 días de vacaciones.")
    elif tiempoContrato == 3:
        print("\n" + nombre + " tienes 30 días de vacaciones.")
    else:
        print("Opcion no valida.")

else:
    print("Opción no valida.")
