"""
    @reroes
    Ejemplo de manejo  de Excepciones
    http://docs.python.org.ar/tutorial/3/errors.html
    salida


Ingreso de datos de empleado

Ingreso su nombre :
René
Ingreso de nota 1 :
10
Ingreso de nota 2 :
2
Traceback (most recent call last):
  File "ejemplo3.py", line 13, in <module>
    promedio = int(nota1) / nota2
TypeError: unsupported operand type(s) for /: 'int' and 'str'
"""

from librerias.misexcepciones import NumeroNegativosError

print("Ingreso de datos de empleado\n")

try:
    nombre = input("Ingreso su nombre :\n")
    nota1 = input("Ingreso de nota 1 :\n")
    nota2 = input("Ingreso de nota 2 :\n")
    nota1 = int(nota1)
    nota2 = int(nota2)
    if (nota1 < 0) or (nota2 < 0):
        raise NumeroNegativosError("No se puede ingresar valor menore a cero")
    promedio = int(nota1) / int(nota2)
    print("Los datos ingresados son: \nNombre: %s\nNota1: %d \nNota2: %d\
            \nPromedio: %f" % (nombre, int(nota1), int(nota2), promedio))
except TypeError as ex:
    print("Algo paso en el programa (TypeError)\n")
    print(ex)
    print(type(ex))
except NumeroNegativosError as ex:
    print("Algo paso en el programa (NumeroNegativosError)\n")
    print(ex)
    print(type(ex))
except Exception as ex:
    print("Algo paso en el programa (Exeption)\n")
    print(ex)
    print(type(ex))
    


