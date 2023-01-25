"""
    @reroes
    Ejemplo de manejo  de Excepciones
    http://docs.python.org.ar/tutorial/3/errors.html
    salida

    Traceback (most recent call last):
      File "ejemplo1.py", line 10, in <module>
        resultado = valor/valor2
    ZeroDivisionError: division by zero
"""

valor = 10
valor2 = 0

resultado = valor/valor2
print("El resultado es " % resultado)


