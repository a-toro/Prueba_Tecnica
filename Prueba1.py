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
# Crear un objeto de clase que reciba una matriz de N
class MyMatrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.suma = 0
        self.profundidad_matrix = 0
        self.vector_straight = []
        self.valores_unicos = []
    
    # Los siguientes métodos se definen con funciones de recursividad.
    # Definir método compute
    def compute(self):
        # Recorre la matriz por cada uno de sus elemento
        for elemento in self.matrix:
            # Evalua si elemento es una lista
            if isinstance(elemento, list):
                # Si es una lista, asigan el elemento a la matrix y se vuelve a llamar a la misma dunción
                self.matrix = elemento
                self.compute()
            else:
                # Si no es una lista, se acumula el valor de cada uno de sus elementos
                self.suma += elemento
        return self.suma
    
    # Definir método dimension
    # Retorna en nivel de profundidad de una matriz
    def dimension(self):
        # Recorre la matríz por cada uno de sus elementos
        for elemento in self.matrix:
            # Evalua si el elemento es un número entero
            if isinstance(elemento, int):
                # Suma 1 punto y termina el ciclo
                self.profundidad_matrix += 1
                break
            # Evalua si el elemento es una liosta
            if isinstance(elemento, list):
                # Suma 1 punto
                self.profundidad_matrix += 1
                # Actualiza la matríz
                self.matrix = elemento
                # Se llama así misma
                self.dimension()
                # Retorna el valor de la profundidad de la matríz
                return self.profundidad_matrix
        return self.profundidad_matrix
    
    # Definir método straingt
    def straight(self):
        # Recorre la matriz por cada uno de sus elemento
        for elemento in self.matrix:
            # Evalua si los elementos dentro de la matriz
            # Si es verdadero almacena el la longitud de la lista en el vector_straight
            if isinstance(elemento, int):
                self.vector_straight.append(len(self.matrix))
            else:
                # De lo contrario se actualiza el valor de la self.matrix
                # Se vuelve a llamar la misma función
                self.matrix = elemento
                self.straight()
        
        # Recorre los valores almacenado en el vector_straight en el paso anterior
        for x in self.vector_straight:
            # Evalua si el elemento x se encuentra en el vector valores_unicos
            # Si no esta lo agrega.
            if x not in self.valores_unicos:
                self.valores_unicos.append(x)
        # Evalua la longitud del vector valores_unicos
        # Si es mayor a uno significa que dentro de la matriz hay un elemento con diferetes dimensión por lo que devuelkve False
        if len(self.valores_unicos)==1:
            return True
        else:
            return False


# Ejemplos de prueba
w = [[[[[1]]]]]
a = [1,2]
b = [[1,2],[2,4]] 
c = [[1,2],[2,4],[2,4]] 
d = [[[3,4],[6,5]]] 
e = [[[1, 2, 3]], [[5, 6, 7],[5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]] 
f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]

# Resultados
print("Compute: ",MyMatrix(w).compute())
print("Dimension: ",MyMatrix(w).dimension())
print("Straight: ", MyMatrix(w).straight())
print("---------------------------------------------")
print("Compute: ",MyMatrix(a).compute())
print("Dimension: ",MyMatrix(a).dimension())
print("Straight: ", MyMatrix(a).straight())
print("---------------------------------------------")
print("Compute: ",MyMatrix(b).compute())
print("Dimension: ",MyMatrix(b).dimension())
print("Straight: ", MyMatrix(c).straight())
print("---------------------------------------------")
print("Compute: ",MyMatrix(d).compute())
print("Dimension: ",MyMatrix(d).dimension())
print("Straight: ", MyMatrix(d).straight())
print("---------------------------------------------")
print("Compute: ",MyMatrix(e).compute())
print("Dimension: ",MyMatrix(e).dimension())
print("Straight: ", MyMatrix(e).straight())
print("---------------------------------------------")
print("Compute: ",MyMatrix(f).compute())
print("Dimension: ",MyMatrix(f).dimension())
print("Straight: ", MyMatrix(f).straight())