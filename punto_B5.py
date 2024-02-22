#Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla hasta que el usuario teclee No.

# Initialize the variable to store the user's response
flag = 0
# continua preguntando"
while flag == 0:
    print()
    respuesta = input("¿Desea continuar Si/No? ").lower()
    if respuesta == "si":
        print("Continuo entonces")
    if respuesta == "no":
        flag = True
print(f'fin de programa')
print()