c = open('chanchito.txt', 'w')

c.write('\nagregando una nueva linea al archivo chanchito')

c.close()

x = open('chanchito.txt')

print(x.read())

import os

if os.path.exists('chanchito2.txt'):
    os.remove('chanchito2.txt') #Elimina un arvhivo o carpeta que nombremos.
else:
    print ('El Archivo no existe')

#os.rmdir('') #Con el directorio se pueden eliminar carpeta.