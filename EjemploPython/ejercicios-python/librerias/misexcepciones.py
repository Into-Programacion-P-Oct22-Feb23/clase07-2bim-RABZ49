class Error(Exception):
    """Clase base para excepciones en el módulo."""
    pass

class NumeroNegativosError(Error):
    """Excepción lanzada por errores en las entradas.

    Atributos:
        expresion -- expresión de entrada en la que ocurre el error
    """

    def __init__(self, expresion):
        self.expresion = expresion

class TamanioDatosPersonalesError(Error):
    """Excepción lanzada para el tamaño de cadenas.

    Atributos:
        expresion -- expresión de entrada en la que ocurre el error
    """

    def __init__(self, expresion):
        self.expresion = expresion
