#Implemente la ecuación de carga y descarga para un circuito RC. 
#El usuario ingresa por teclado el valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω).
#Posteriormente realice en Python la gráfica.

import numpy as np
from matplotlib import pyplot as plt

x=True
while(x):
    v0=float(input('ingrese voltaje(v): '))
    R=float(input('ingrese resistencia(ohm): '))
    C=float(input('ingrese capacitancia(Faradios): '))
    tao = 5*R*C
    t = np.arange (0, 9, 0.001)
    coef= v0*(1-np.exp(-t/(R*C)))
    coef2= v0*(np.exp(-t/(R*C)))

    plt.subplot(2, 1, 1)
    plt.plot(t,coef)
    plt.title('Curva de carga ')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    #plt.show()

    plt.subplot(2, 1, 2)
    plt.plot(t,coef2)
    plt.title('Curva de descarga ')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')


    plt.tight_layout()  # Ajustar automáticamente los subgráficos para evitar solapamientos
    plt.show()
    


   



