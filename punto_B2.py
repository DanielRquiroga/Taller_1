import numpy as np
#Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.
numeros = int(input('Ingrse la cantidad de numero que desea: /n'))
inferior = int(input('ingrese rango inferior\n'))
superior = int(input('ingrese rango isuperior\n'))

numero_entero_aleatorio = np.random.randint(inferior,superior + 1, size=(numeros))
print(f'los numeros son {numero_entero_aleatorio}')