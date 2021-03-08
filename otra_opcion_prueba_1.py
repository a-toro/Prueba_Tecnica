# compute
def itertar(lista):
    for elemento in lista:
        if isinstance(elemento, list):
            iterar(elemento)


class MyMatrix():
    def __init__(self,matrix):
        self.matrix = matrix
    suma = 0
    # compute
    def compute(self):
        global suma
        suma = 0
        for i in self.matrix:
            if isinstance(i, list):
                itertar(i)
            else:
                suma += i
        return suma

a = [[1,2,30],[1]]
print(MyMatrix(a).compute())