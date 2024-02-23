#Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura.
import math
temp = 40
R0 = 100.0
A = 3.9083e-3       #coeficiente Callendar-Van Dusen
B = -5.775e-7       #coeficiente Callendar-Van Dusen
C = -4.183e-12      #coeficiente Callendar-Van Dusen
R = R0 * (1 + A * temp + B * temp**2 + C * (temp - 100) * temp**3) # usando la ecuación de Callendar-Van Dusen
print()
print(f'la resistencia es aproximandamente {R:.3f} a una temperatura de {temp} grados\n')