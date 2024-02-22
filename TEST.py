import matplotlib.pyplot as plt
import numpy as np

def dibujar_nombre():
    # Crear un nuevo plot
    fig, ax = plt.subplots()

    # Dibujar líneas y círculos para formar el nombre
    # Ejemplo de líneas
    ax.plot([1, 2, 3, 4, 5], [2, 5, 3, 1, 4], color='blue', label='Líneas')

    # Ejemplo de círculos
    centro_circulo = (6, 3)
    radio_circulo = 1
    circulo = plt.Circle(centro_circulo, radio_circulo, color='red', fill=False, label='Círculo')
    ax.add_patch(circulo)

    # Texto con tu nombre
    ax.text(3, 6, 'Tu Nombre', fontsize=12, ha='center', va='center')

    # Configurar el aspecto del plot
    plt.title('Dibujando Mi Nombre')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
    plt.legend()

    # Ajustar límites para una mejor visualización
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)

    # Mostrar el plot
    plt.show()

# Llamar a la función para dibujar el nombre
dibujar_nombre()


# Llamar a la función para dibujar el nombre
dibujar_nombre()