#Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.
import numpy as np

numeros = int(input(f'ingrse cantidad de numeros a generar\n'))
inferior = int(input(f'''ingrese rango inferior\n'''))
superior = int(input(f'ingrese rango isuperior\n'))
aleatorio = np.random.randint(inferior,superior + 3, size=(numeros))
print(f'''los numeros son {aleatorio}''')
