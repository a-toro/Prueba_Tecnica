""" Enunciado
Construya un objeto que reciba como parámetro un string y reconozca mediante expresiones
    regulares los siguientes criterios.
El objeto debe tener los siguientes métodos suponiendo la siguiente definición.
    s = MyArray.new(string)

A. s.operation -> Devuelve un booleano según el siguiente criterio -True: Si el texto
    recibido corresponde a una operación aritmética (+, -, /, *) matemática. -False: Si el
    texto recibido no corresponde a ninguna operación aritmética matemática o se
    encuentra mal construída.  
B. s.compute -> Devuelve el valor computado de la operación aritmética, se deben
    considerar los paréntesis '(' ')' como agrupaciones de la operación. Devuelve false en el
    caso de que la operación no pueda ser computada por paréntesis mal agrupados o en
    el caso de que s.operation sea false.
"""
import parser

class MyArray():
    # Constructor inicial
    def __init__(self, string):
        # Se convierte a str el valor ingresado en caso de que ingrese un número y no una cadena de texto.
        self.string = str(string)

    def operation(self):
        """Evalua si el string ingresado si se puede operar matematicamente, si es así
        devuelve True, de lo contrario devuelve False"""
        try:
            parser.expr(self.string).compile()
            return True
        except SyntaxError:
            return False
        except TypeError:
                return False
    # Definir método compute
    def compute(self):
        if MyArray(self.string).operation():
            expresion_matematica = parser.expr(self.string).compile()
            resultado = eval(expresion_matematica)
            return resultado
        else:
            return False  

# Ejemplos de uso
a = "2+2)"
b = "2 + 10 / 2 - 20" 
c = "(2 + 10) / 2 - 20" 
d = "(2 + 10 / 2 - 20"

# Resultados
print("Ejemplo 1: ", a)
print("El resultado del método .operation() es: ", MyArray(a).operation())
print("El resultado del método .compute() es: " , MyArray(a).compute())
print("-----------------------------------------------------------------------")
print("Ejemplo 1: ", b)
print("El resultado del método .operation() es: ", MyArray(b).operation())
print("El resultado del método .compute() es: " , MyArray(b).compute())
print("-----------------------------------------------------------------------")
print("Ejemplo 1: ", c)
print("El resultado del método .operation() es: ", MyArray(c).operation())
print("El resultado del método .compute() es: " , MyArray(c).compute())
print("-----------------------------------------------------------------------")
print("Ejemplo 1: ", d)
print("El resultado del método .operation() es: ", MyArray(d).operation())
print("El resultado del método .compute() es: " , MyArray(d).compute())
print("-----------------------------------------------------------------------")