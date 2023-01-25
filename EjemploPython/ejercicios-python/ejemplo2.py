"""
    @reroes
    Ejemplo de manejo  de Excepciones
    http://docs.python.org.ar/tutorial/3/errors.html
    salida

Ingreso de datos de empleado

Ingreso su nombre :
René
Traceback (most recent call last):
  File "ejemplo2.py", line 16, in <module>
    print("Los datos ingresados son %s %s" % (nombre, apellido))
NameError: name 'apellido' is not defined
"""
print("Ingreso de datos de empleado\n")

nombre = input("Ingreso su nombre :\n")
# apellido = input("Ingres su apellido: \t")
print("Los datos ingresados son %s %s" % (nombre, apellido))


