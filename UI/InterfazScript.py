import re
import tkinter as tk
import webbrowser
from io import open
from tkinter import *
from tkinter import ttk, filedialog
import os


from Analisis.Lexico.AnalizadorLexicoScript import AnalizadorLexico
from Analisis.Sintactico.AnalizadorSintacticoScript import AnalizadorSintactico

# Manera de pythonica de hacer un singleton
from Patrones.Singleton import Singleton
from UI.Comandos import Comandos

@Singleton
class Interfaz:

    def __init__(self):
        pass
    comandos = Comandos
    analizador_lex = AnalizadorLexico()
    contenido = ""

    # manera estilo java de implementar singleton
    # __instance__ = None
    #
    # def __new__(cls):
    #     if Interfaz.__instance__ is None:
    #         print("Nueva instancia de UI")
    #         Interfaz.__instance__ = object.__new__(cls)
    #     return Interfaz.__instance__

    def getTextoSalida(self):
        return self.texto_salida

    def setTextoSalida(self, texto):
        self.texto_salida.insert('1.0', texto)

    def crearInterfaz(self):
        root = tk.Tk()
        root.geometry("1100x500")
        root.configure(background='#263D42')
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        # creo un canvas
        canvas = Canvas(main_frame)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        # agrego un scrollbar al canvas
        scrollbar = tk.Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        #configuro el canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
        #crear otro frame dentro del canvas
        segunda_frame = Frame(canvas)

        #agregar esa  frame a una nueva ventana
        canvas.create_window((0,0), window=segunda_frame,anchor="nw")

        self.texto_salida = Text(segunda_frame, width=100, height=20)
        self.texto_salida.grid(row=0, column=0, padx=30, pady=20)

        self.texto_entrada = Text(segunda_frame, width=100, height=5)
        self.texto_entrada.grid(row=1, column=0, padx=30, pady=5)

        self.boton_enviar = Button(segunda_frame, text="Enviar", command=self.enviarClick, width=20, height=2)
        self.boton_enviar.grid(row=1, column=1, pady=10)

        # creo los botones del lado derecho
        boton_frame = Frame(segunda_frame)
        boton_frame.grid(row=0, column=1)

        self.boton_errores = Button(boton_frame, text="Reporte de errores", command=self.analizarClick, width=20, height=2)
        self.boton_errores.grid(row=0, column=1, pady=10)

        self.boton_limpiar = Button(boton_frame, text="Limpiar log de errores", command=self.limpiarClick, width=20, height=2)
        self.boton_limpiar.grid(row=1, column=1, pady=10)

        self.boton_tokens = Button(boton_frame, text="Reporte de tokens", command=self.tokensClick, width=20, height=2)
        self.boton_tokens.grid(row=2, column=1, pady=10)

        self.boton_limpiarTokens = Button(boton_frame, text="Limpiar log de tokens", command=self.limpiarTokensClick, width=20, height=2)
        self.boton_limpiarTokens.grid(row=3, column=1, pady=10)

        self.boton_manualTecnico = Button(boton_frame, text="Manual de usuario", command=self.manualTecnicoClick, width=20, height=2)
        self.boton_manualTecnico.grid(row=4, column=1, pady=10)

        self.boton_manualUsuario = Button(boton_frame, text="Manual tecnico", command=self.manualUsuarioClick, width=20, height=2)
        self.boton_manualUsuario.grid(row=5, column=1, pady=10)

        root.mainloop()

    def analizarClick(self):
        pass

    def enviarClick(self):

        # analizo sintáctica y lexicamente para ver que todo esté bien
        # si está bien entonces ejecuto el comando
        texto_enviar = self.texto_entrada.get('1.0', END)
        self.analizador_lex.analizar(texto_enviar)
        # analizo sintacticamente
        # guardo mis listas de tokens y errores
        lista_tokens = self.analizador_lex.listaTokens
        lista_errores = self.analizador_lex.listaErrores
        analizador_sin = AnalizadorSintactico(self.analizador_lex.listaTokens)
        analizador_sin.analizar()
        analizador_sin.imprimirErrores()
        # "Si no hay errores entonces ejecuto la instrucción
        if len(analizador_sin.errores) == 0:
            self.texto_salida.insert('1.0', texto_enviar + str(self.comandos.getResultado()))


    def limpiarClick(self):
        pass
    def tokensClick(self):
        pass
    def limpiarTokensClick(self):
        pass
    def manualTecnicoClick(self):
        pass
    def manualUsuarioClick(self):
        pass

    def cadenaError(self):
        cadena_temp = ""
        for error in self.analizador_lex.listaErrores:
            cadena_temp += "<tr><td>" + str(error.descripcion) + "</td><td>" + str(error.linea) + "</td><td>" + str(
                error.columna) + "</td></tr>\n"
        return cadena_temp

    def cadenaTokens(self):
        cadena_temp = ""
        for token in self.analizador_lex.listaTokens:
            cadena_temp += "<tr><td>" + str(token.lexema) + "</td><td>" + str(token.linea) + "</td><td>" + str(
                token.columna) + "</td></tr>\n"
        return cadena_temp

    def exportarReporteTokens(self):
        dir = os.getcwd()
        archivo = open(dir + "\\Modelos\\ModeloTokens.html", "r")
        modelo = archivo.read()
        archivo.close()
        pagina_resultado = open(dir + "\\Modelos\\tokens.html", "w+")
        indice = modelo.index("</table>")
        cadena = self.cadenaTokens()
        nuevo_contenido = ""
        nuevo_contenido += modelo[0:indice] + cadena[0] + modelo[indice:len(modelo)]
        indice2 = nuevo_contenido.rindex("</table>")
        nuevo_contenido = nuevo_contenido[:indice2] + cadena[1:] + nuevo_contenido[indice2:]
        pagina_resultado.write(nuevo_contenido)
        webbrowser.open_new_tab(dir + "\\Modelos\\tokens.html")

    def exportarReporteErrores(self):
        dir = os.getcwd()
        archivo = open(dir + "\\Modelos\\ModeloErrores.html", "r")
        modelo = archivo.read()
        archivo.close()
        pagina_resultado = open(dir + "\\Modelos\\errores.html", "w+")
        indice = modelo.index("</table>")
        cadena = self.cadenaError()
        nuevo_contenido = ""
        nuevo_contenido += modelo[0:indice] + cadena[0] + modelo[indice:len(modelo)]
        indice2 = nuevo_contenido.rindex("</table>")
        nuevo_contenido = nuevo_contenido[:indice2] + cadena[1:] + nuevo_contenido[indice2:]
        pagina_resultado.write(nuevo_contenido)
        webbrowser.open_new_tab(dir + "\\Modelos\\errores.html")