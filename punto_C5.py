import matplotlib.pyplot as plt

# cordenadas nombre alex
x = [1, 1, 2, 3, 1, 3, 3, 4, 4, 4, 6, 7, 7, 9, 7, 7, 9, 7, 7, 9, 10, 12, 11, 10, 12]
y = [1, 3, 6, 3, 3, 3, 1, 1, 6, 1, 1, 1, 3, 3, 3, 6, 6, 6, 1, 1, 1, 6, 3, 6, 1]

# cordenadas nombre alexa
x2 = [1, 1, 2, 3, 1, 3, 3, 4, 4, 4, 6, 7, 7, 9, 7, 7, 9, 7, 7, 9, 10, 12, 11, 10, 12, 13, 13, 14, 15, 13, 15, 15]
y2 = [1, 3, 6, 3, 3, 3, 1, 1, 6, 1, 1, 1, 3, 3, 3, 6, 6, 6, 1, 1, 1, 6, 3, 6, 1, 1, 3, 6, 3, 3, 3, 1]

## cordenadas nombre daniel
x3=[1,1,3,4,4,3,1,5,5,6,7,5,7,7,8,8,10,10,10,12,12,12]
y3=[1,6,6,5,2,1,1,1,3,6,3,3,3,1,1,6,1,6,1,1,6,1]

##cordenadas nombre kevin

x4=[1,1,1,3,1,3,4,4,6,4,4,6,4,4,6,9,8,9,10,9,11,11,11,12,12,14,14]
y4=[1,6,3,6,3,1,1,3,3,3,6,6,6,1,1,1,6,1,6,1,1,6,1,1,6,1,6]

# Grafica nombre alex
plt.plot(x, y, 'bo-')
plt.axis('equal')  # Establecer los ejes en la misma escala
plt.title('alex')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.show()

#grafica nombre alexa
plt.plot(x2, y2, 'bo-')
plt.axis('equal')  # Establecer los ejes en la misma escala
plt.title('alexa')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.show()

# Grafica nombre daniel
plt.plot(x3, y3, 'bo-')
plt.axis('equal')  # Establecer los ejes en la misma escala
plt.title('dani')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.show()

# Grafica nombre kevin
plt.plot(x4, y4, 'bo-')
plt.axis('equal')  # Establecer los ejes en la misma escala
plt.title('kevin')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.show()