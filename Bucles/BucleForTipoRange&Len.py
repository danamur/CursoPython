print("------------------------")
print("| Bucle For tipo Range |")
print("------------------------\n")

for i in range(5,20,3):
    print(f"valor de la variable {i}")

print("\n------------------------")
print("| Bucle For tipo len |")
print("------------------------\n")

valido=False

email=input("Introduce tu email:\n")

for i in range(len(email)):

    if email[i] == "@":
        valido = True

if valido:
    print("email es correcto")
else:
    print("email no valido")
