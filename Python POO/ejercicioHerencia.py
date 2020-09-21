class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya


    def saludo(self):
        print("Hola, soy un", self.tipo, "y mi sonido es el", self.onomatopeya)

class Gato(Animal):

    tipo = 'Gato'


class Perro(Animal):

    tipo = "Perro"

class Canario(Animal):

    tipo = "Canario"

gato = Gato('Juanin', 'Maullido')
gato.saludo()

perro = Perro('Cachupin', 'Ladrido')
perro.saludo()

canario = Canario('Piolin', 'Silvido')
canario.saludo()