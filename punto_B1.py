#Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el valor de corriente y voltaje.
print()

voltaje = int(input('Ingrese voltaje (V) \n')) 
corriente = int(input("Ingrese corriente (A) \n"))
potencia = voltaje*corriente

print(f''''la potencia de consumo del circuito es: {potencia} Watts\n''')