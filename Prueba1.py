""" Enunciado
Construya un objeto que reciba un arreglo o una matriz de dimensión N el cual contiene
números de tipo entero.

a. o.dimension -> Devuelve el número entero que define la dimensión del arreglo o
    matriz en su mayor profundidad.
b. o.straight -> Devuelve true o false según el siguiente criterio: -True: Si el arreglo o
    matriz contiene la misma cantidad de elementos en cada una de sus dimensiones
    (Matriz uniforme). -False: Caso contrario.
c. o.compute -> Devuelve el número entero resultado de la
"""
# Crear un objeto de clase que recoba una matriz de N
import numpy
import warnings
warnings.filterwarnings("ignore", category=numpy.VisibleDeprecationWarning)

class MyMatrix():
    def __init__(self, matrix):
        self.matrix = matrix

    # Definir método compute
    def compute(self):
        suma = 0
        try:
            suma = sum(self.matrix)
            longitud = len(self.matrix)
        except:
            # Recorrer el primer nivel o dimensión de la matriz
            for i in range(0,len(self.matrix),1):
                n_1 = self.matrix[i]
                try:
                    suma += sum(n_1)
                except:
                    # Recorrer el segundo nivel de la matriz
                    for j in range(0,len(n_1),1):
                        n_2 = n_1[j]
                        try:
                            suma += sum(n_2)
                        except:
                            # Recorrer el tercer nivel de la matriz
                            for k in range(0,len(n_2),1):
                                n_3 = n_2[k]
                                try:
                                    suma += n_3[k]
                                except:
                                    # Recorrer el cuarto nivel de  la matriz en caso de existir
                                    for m in range(0,len(n_3),1):
                                        n_4 = n_3[m]
                                        suma += sum(n_4)
        return suma
    
    # Definir método dimension
    def dimension(self):
        # Cambiar el typo de datos numpy.array
        self.matrix = numpy.array(self.matrix)
        # Devuelve el valor de la dimensión de la matríz.
        dimension = self.matrix.ndim
        return print(dimension)