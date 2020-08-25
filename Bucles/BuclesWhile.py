edad=int(input("Introduce tu edad porfavor\n"))

intento = 0

while edad < 5 or edad > 100:
    print("Has a introducido una edad incorrecta. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad porfavor\n"))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante es", edad)
