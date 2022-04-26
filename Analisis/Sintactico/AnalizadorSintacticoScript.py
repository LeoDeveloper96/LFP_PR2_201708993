class AnalizadorSintactico:

    def __init__(self, tokens: list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self, esperado, obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido, esperado)
        )

    def sacarToken(self):
        ''' Saca el primer token y lo quita de la lista'''
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        ''' Saca el primer token y lo mete de nuevo en de la lista'''
        try:
            return self.tokens[0]
        except:
            return None

    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        pass

    def RESULTADO(self):
        pass
    def JORNADA(self):
        pass
    def GOLES(self):
        pass
    def TABLA(self):
        pass
    def PARTIDOS(self):
        pass
    def TOP(self):
        pass
    def BANDERA(self):
        pass
    def BANDERAS(self):
        pass
    def CONDICION(self):
        pass