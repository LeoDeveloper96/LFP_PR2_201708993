import re
import tkinter as tk
import webbrowser
from io import open
from tkinter import *
from tkinter import ttk, filedialog
import os


class Interfaz:

    def crearInterfaz(self):
        root = tk.Tk()
        root.geometry("1200x800")
        root.configure(background='#263D42')

        self.texto_salida = Text(root, width=100, height=40)
        self.texto_salida.grid(row=0, column=0, padx=30, pady=20)

        self.texto_entrada = Text(root, width=100, height=5)
        self.texto_entrada.grid(row=1, column=0, padx=30, pady=5)

        self.boton_enviar = Button(root, text="Enviar", command=self.enviarClick, width=20, height=2)
        self.boton_enviar.grid(row=1, column=1, pady=10)

        # creo los botones del lado derecho
        boton_frame = Frame(root,background='#263D42')
        boton_frame.grid(row=0, column=1)

        self.boton_errores = Button(boton_frame, text="Reporte de errores", command=self.analizarClick, width=20,height=2)
        self.boton_errores.grid(row=0, column=1, pady=10)

        self.boton_limpiar = Button(boton_frame, text="Limpiar log de errores", command=self.limpiarClick, width=20, height=2)
        self.boton_limpiar.grid(row=1, column=1, pady=10)

        self.boton_tokens = Button(boton_frame, text="Reporte de tokens", command=self.tokensClick,width=20, height=2)
        self.boton_tokens.grid(row=2, column=1, pady=10)

        self.boton_limpiarTokens = Button(boton_frame, text="Limpiar log de tokens", command=self.limpiarTokensClick, width=20, height=2)
        self.boton_limpiarTokens.grid(row=3, column=1, pady=10)

        self.boton_manualTecnico = Button(boton_frame, text="Manual de usuario", command=self.manualTecnicoClick, width=20,height=2)
        self.boton_manualTecnico.grid(row=4, column=1, pady=10)

        self.boton_manualUsuario = Button(boton_frame, text="Manual tecnico", command=self.manualUsuarioClick, width=20, height=2)
        self.boton_manualUsuario.grid(row=5, column=1, pady=10)

        root.mainloop()

    def analizarClick(self):
       pass
    def enviarClick(self):
        pass
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