print("Sistema para cualcular el promerdio de un alumno")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")
matematicas = float(input(nombre + " ¿Cual es tu calificacion en matematicas?: "))
quimica = float(input(nombre + " ¿Cual es tu calificacion en quimica?: "))
lenguaje = float(input(nombre + "¿Cual es tu calificacion en biologia?: "))

promedio = (matematicas + quimica + lenguaje) / 3

if promedio >= 4.0:
    print('Felicidades ' + nombre + '! "Aprovaste" con un promedio de: ', promedio)                    

print("Fin.")
