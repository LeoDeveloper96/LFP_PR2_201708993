import pandas as pd
import os

class Archivo:

    dir = os.getcwd()
    # encabezado
    # Fecha,Temporada,Jornada,Equipo1,Equipo2,Goles1,Goles2

    set_datos = pd.read_csv(dir + "\\Archivos\\LaLigaBot-LFP.csv")

    def EJECUTAR_RESULTADO(self, equipo1, equipo2, intervalo):
        datos = self.set_datos.loc[(self.set_datos['Temporada'] == intervalo.lexema.replace("\n","")) & (self.set_datos['Equipo1'] == equipo1.lexema.replace("\'","")) & (self.set_datos['Equipo2'] == equipo2.lexema.replace("\'",""))]
        print(datos)
        return datos

    def EJECUTAR_JORNADA(self):
        pass

    def EJECUTAR_GOLES(self):
        pass

    def EJECUTAR_TABLA(self):
        pass

    def EJECUTAR_PARTIDOS(self):
        pass

    def EJECUTAR_TOP(self):
        pass



