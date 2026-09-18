import numpy as np

# APARTADO 1:
# Vector randomizado
v1 = np.random.random(10)
print("\nApartado 1:")
print(v1)

# APARTADO 2:
# Matriz de ceros
matrix = np.zeros((10, 10))
print("\nApartado 2:")
print(matrix)

# APARTADO 3:
# Selección de los bordes para que valgan 1
matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1
print("\nApartado 3:")
print(matrix)

# APARTADO 4:
# Crea un array con los elementos impares.
# Se haría empezando en el elemento 1 y recorriendo el array
# original (matrix) con saltos de 2 en 2.
matrix_odd = np.array(matrix[1::2, 1::2], copy=True)
print("\nApartado 4:")
print(matrix_odd)

# APARTADO 5:
# Crea un array con los elementos pares.
# Se haría empezando en el elemento 0 y recorriendo el array
# original (matrix) con saltos de 2 en 2.
matrix_even = np.array(matrix[0::2, 0::2], copy=True)
print("\nApartado 5:")
print(matrix_even)

# APARTADO 6:
# Cambia matrix[1, 2] a 3. Muestra por pantalla la segunda fila.
matrix[1, 2] = 3
print("\nApartado 6:")
print(matrix[1, :])