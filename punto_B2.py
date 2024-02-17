import numpy as np
#Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.
numeros = int(input(f'ingrse cantidad de numeros a generar\n'))
inferior = int(input(f'''ingrese rango inferior\n'''))
superior = int(input(f'ingrese rango isuperior\n'))

numero_entero_aleatorio = np.random.randint(inferior,superior + 1, size=(numeros))
print(f'''los numeros son {numero_entero_aleatorio}''')
