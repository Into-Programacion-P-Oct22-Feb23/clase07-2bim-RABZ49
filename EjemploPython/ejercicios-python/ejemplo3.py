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
print("Ingreso de datos de empleado\n")

nombre = input("Ingreso su nombre :\n")
nota1 = input("Ingreso de nota 1 :\n")  # str
# nota2 = input("Ingreso de nota 2 :\n")
nota2 = int(input("Ingreso de nota 2 :\n"))
nota1 = int(nota1)  # int
# nota2 = int(nota2)
promedio = nota1 / nota2  # int/int

print("Los datos ingresados son: \nNombre: %s\nNota1: %d \nNota2: %d\
        \nPromedio: %.1f" % (nombre, nota1, nota2, promedio))


