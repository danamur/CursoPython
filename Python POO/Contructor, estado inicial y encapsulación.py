print("------------------------")
print("| Ejemplo de clases |")
print("------------------------\n")

class Coche():

    #Ejemplo de constructor en python
    def __init__(self):
    
        #Parametros de las clase. (Propiedades de un objeto)
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4 #Ejemplo de como encapsular un parametro.
        self.enmarcha=False

    #Metodos de la clase (comportamiento de un objeto).
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El coche esta en marcha"

        else:
            return "EL coche esta parado"

    def estado(self):
        print("El coche tiene ",self.__ruedas, "ruedas. Un ancho de ",
              self.anchoChasis, " Y un largo de ", self.largoChasis)

#Instaciar un Clase.
miCoche = Coche()

miCoche.estado()
print(miCoche.arrancar(True))


print("\n------------------------------------------------")
print("| A continuación creamos el segundo objeto |")
print("------------------------------------------------\n")

miCoche2=Coche()

print(miCoche.arrancar(False))
miCoche2.estado()


