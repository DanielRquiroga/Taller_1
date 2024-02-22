import matplotlib.pyplot as plt

# Coordenadas de los nombres
nombres = ['Gilber', 'Kevin', 'Daniel', 'Lheidy']
x_coord = [1, 2, 3, 4]
y_coord = [3, 1, 2, 4]

# Dibujar los nombres
for nombres, x, y in zip(nombres, x_coord, y_coord):
    plt.text(x, y, nombres, fontsize=12, ha='center', va='center')

# Configurar el plot
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Nombres de los integrantes del grupo')

# Mostrar el plot
plt.grid(True)
plt.show()