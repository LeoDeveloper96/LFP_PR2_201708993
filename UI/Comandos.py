from Patrones.Singleton import Singleton


@Singleton
class Comandos:

    def __init__(self, comando=None, resultados=None):
        self.comando = comando
        self.resultados = resultados

    def getComando(self):
        return self.comando

    def getResultado(self):
        return self.resultados

    def setComando(self, comando):
        self.comando = comando

    def setResultado(self, resultados):
        self.resultados = resultados
