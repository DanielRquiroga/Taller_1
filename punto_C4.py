import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dibujar_vector(x, y, z):
    # Creo una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibujo el vector desde el origen hasta las coordenadas dadas
    ax.quiver(0, 0, 0, x, y, z, color='r', label='Vector')

    # Configurar etiquetas de ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Configurar límites de los ejes
    ax.set_xlim([0, max(x, 10)])
    ax.set_ylim([0, max(y, 10)])
    ax.set_zlim([0, max(z, 10)])

    # Mostrar leyenda
    ax.legend()

    # Mostrar la figura
    plt.show()

def main():
    # Solicitar al usuario las coordenadas del vector
    print()
    x = float(input("Ingrese la coordenada X del vector: "))
    y = float(input("Ingrese la coordenada Y del vector: "))
    z = float(input("Ingrese la coordenada Z del vector: "))

    # Llamar a la función para dibujar el vector
    dibujar_vector(x, y, z)

main()