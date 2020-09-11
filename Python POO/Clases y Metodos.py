print("------------------------")
print("| Ejemplo de clases |")
print("------------------------\n")

class Coche():

    #Parametros de las clase. (Propiedades de un objeto)
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    #Metodos de la clase (comportamiento de un objeto).
    def arrancar(self): #Nota 1
        self.enmarcha=True

    def estado(self): #Informa el estado del vehiculo
        if(self.enmarcha):
            return "El coche esta en marcha"

        else:
            return "EL coche esta parado"

#Instaciar un Clase.
miCoche = Coche()

print("El lago del coche es",miCoche.largoChasis)
print("El coche tiene",miCoche.ruedas, "ruedas")
miCoche.arrancar() #Llamar al metodo para cambiar el estado del vehiculo
print(miCoche.estado())

#Nota 1: el self es igual a un this de otros lenguajes de programacion pero en python es obligacion cololarlo en el primer metodo, no es implicito.  
