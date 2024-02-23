#Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.
import numpy as np
from matplotlib import pyplot as plt

temp = np.arange (-200, 200.5, 0.5)       #ingreso de temperatura numpy.arange genera un conjunto de números entre un valor de inicio y uno final
R0 = 100.0
A = 3.9083e-3       #coeficiente Callendar-Van Dusen
B = -5.775e-7       #coeficiente Callendar-Van Dusen
C = -4.183e-12      #coeficiente Callendar-Van Dusen
R = R0 * (1 + A * temp + B * temp**2 + C * (temp - 100) * temp**3) # usando la ecuación de Callendar-Van Dusen 
plt.title ('Comportamiento sensor PT100')
plt.ylabel('Resistencia Ω')
plt.xlabel('Temperatura °C')
plt.plot(temp,R)
plt.grid(True)
plt.show()
