from Analisis.Lexico.TokenScript import Token
from Analisis.Lexico.ErrorScript import Error
from prettytable import PrettyTable
import re


class AnalizadorLexico:

    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = "A"
        self.i = 0

    def buscarCaracter(self, caracter, inicio):
        contador = 0
        for token in self.listaTokens:
            if re.sub("\"", "", token.lexema).lower() == caracter and contador >= inicio:
                break
            contador += 1
        return contador

    def existeValor(self, dato):
        existe = False
        for item in self.listaTokens:
            if re.sub("\"", "", item.lexema.lower()) == dato.lower():
                existe = True
                break
        return existe

    def agregar_token(self, caracter, token, linea, columna):
        self.listaTokens.append(Token(caracter, token, linea, columna))
        self.buffer = ''

    def agregar_error(self, caracter, linea, columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))

    def estadoA(self, caracter):
        if caracter.isalpha():
            self.buffer += caracter
            self.columna += 1
            self.estado = "E"
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
            self.estado = "B"
        elif caracter == '-':
            self.buffer += caracter
            self.columna += 1
            self.estado = "F"
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t', ' ']:
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.buffer = ''
            self.columna += 1

    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []
        # recorrer caracter por caracter
        self.i = 0
        while self.i < len(cadena):
            if self.estado == "A":
                self.estadoA(cadena[self.i])
            elif self.estado == "B":
                self.estadoB(cadena[self.i])
            elif self.estado == "C":
                self.estadoC(cadena[self.i])
            elif self.estado == "D":
                self.estadoD(cadena[self.i])
            elif self.estado == "E":
                self.estadoE(cadena[self.i])
            elif self.estado == "F":
                self.estadoF(cadena[self.i])
            elif self.estado == "G":
                self.estadoG(cadena[self.i])
            elif self.estado == "H":
                self.estadoH(cadena[self.i])
            elif self.estado == "I":
                self.estadoI(cadena[self.i])
            elif self.estado == "J":
                self.estadoJ(cadena[self.i])
            elif self.estado == "K":
                self.estadoK(cadena[self.i])
            self.i += 1
        self.impErrores()
        self.impTokens()

    def estadoB(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        else:
            if caracter == '-':
                self.buffer += caracter
                self.estado = "C"
                self.i -= 1
            else:
                self.agregar_error(self.buffer, self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
                self.buffer = ''

    def estadoC(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.estado = "D"
            self.i = -1
        else:
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.estado = "A"
            self.i -= 1
            self.buffer = ''

    def estadoD(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        else:
            self.buffer += caracter
            self.agregar_token(self.buffer, 'Intervalo', self.linea, self.columna)
            self.estado = "A"
            self.i -= 1

    #Reviso si es una palabra reservada, un identificador, o un nombre de archivo
    def estadoE(self, caracter):
        if re.match("[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ_-]+",caracter):
            self.buffer += caracter
            self.columna += 1
        else:
            if re.search("RESULTADO|VS|TEMPORADA|JORNADA|GOLES|LOCAL|VISITANTE|TOTAL|TABLA|PARTIDOS|TOP|SUPERIOR|INFERIOR",
                         self.buffer.lower()):
                self.agregar_token(self.buffer, 'Reservada', self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
                self.buffer = ''
            elif re.match("[a-zA-ZáéíóúÁÉÍÓÚñÑ]+", self.buffer):
                self.agregar_token(self.buffer, 'Nombre equipo', self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
                self.buffer = ''
            elif re.search("[a-zA-Z0-9_-]+", self.buffer):
                self.agregar_token(self.buffer, 'Nombre archivo', self.linea, self.columna)
                self.estado = "A"
                self.i -= 1
                self.buffer = ''
            else:
                self.estado = "A"
                self.agregar_error(self.buffer, self.linea, self.columna)
                self.i -= 1
                self.buffer = ''

    def estadoF(self, caracter):
        if caracter == "f":
            self.buffer += caracter
            self.columna += 1
            self.estado = "G"
        elif caracter == "n":
            self.buffer += caracter
            self.columna += 1
            self.estado = "H"
        elif caracter == "j":
            self.buffer += caracter
            self.columna += 1
            self.estado = "I"
        else:
            self.estado = "A"
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.i -= 1
            self.buffer = ''


    def estadoG(self, caracter):
        self.agregar_token(self.buffer, 'Bandera -f', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoH(self, caracter):
        self.agregar_token(self.buffer, 'Bandera -n', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoI(self, caracter):
        if caracter == "i":
            self.buffer += caracter
            self.columna += 1
            self.estado = "J"
        elif caracter == "f":
            self.buffer += caracter
            self.columna += 1
            self.estado = "K"
        else:
            self.estado = "A"
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.i -= 1
            self.buffer = ''

    def estadoJ(self, caracter):
        self.agregar_token(self.buffer, 'Bandera -n', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"

    def estadoK(self, caracter):
        self.agregar_token(self.buffer, 'Bandera -n', self.linea, self.columna)
        self.i -= 1
        self.estado = "A"


    # imprimeTokens
    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarData())
        print(x)

    # imprimeErrores
    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores) == 0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
            print(x)



