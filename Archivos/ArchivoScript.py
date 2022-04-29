import pandas as pd
import os


class Archivo:

    dir = os.getcwd()
    # encabezado
    # Fecha,Temporada,Jornada,Equipo1,Equipo2,Goles1,Goles2

    set_datos = pd.read_csv(dir + "\\Archivos\\LaLigaBot-LFP.csv")

    def EJECUTAR_RESULTADO(self, equipo1, equipo2, intervalo):
        datos = self.set_datos.loc[(self.set_datos['Temporada'] == intervalo.lexema.replace("\n","")) & (self.set_datos['Equipo1'] == equipo1.lexema.replace("\'","")) & (self.set_datos['Equipo2'] == equipo2.lexema.replace("\'",""))]
        resultado = 'El resultado fue: ' + equipo1.lexema + ' ' + str(datos['Goles1'].values[0]) + '-' + equipo2.lexema + ' ' + str(datos['Goles2'].values[0])
        print(resultado)
        return resultado

    def EJECUTAR_JORNADA(self):
        pass

    def EJECUTAR_GOLES(self, condicion, equipo, intervalo):
        # Local es equipo1 y cuando es visitante sale como equipo2
        resultado = ''
        if condicion == 'LOCAL':
            datos = self.set_datos.loc[(self.set_datos['Temporada'] == intervalo.replace("\n", "")) & (self.set_datos['Equipo1'] == equipo.lexema.replace("\'", ""))]
            goles = sum(datos['Goles1'].values)
            resultado = 'El resultado de goles como local del ' + equipo.lexema + ' fue:  ' + str(goles)
        elif condicion == 'VISITANTE':
            datos = self.set_datos.loc[(self.set_datos['Temporada'] == intervalo.replace("\n", "")) & (
                    self.set_datos['Equipo2'] == equipo.lexema.replace("\'", ""))]
            goles = sum(datos['Goles1'].values)
            resultado = 'El resultado de goles como visitante del ' + equipo.lexema + ' fue:  ' + str(goles)
        else:
            datos1 = self.set_datos.loc[(self.set_datos['Temporada'] == intervalo.replace("\n", "")) & (
                    self.set_datos['Equipo2'] == equipo.lexema.replace("\'", ""))]

            datos2 = self.set_datos.loc[(self.set_datos['Temporada'] == intervalo.replace("\n", "")) & (self.set_datos['Equipo1'] == equipo.lexema.replace("\'", ""))]

            goles = sum(datos1['Goles1'].values)
            goles += sum(datos2['Goles1'].values)
            resultado = 'El resultado de goles totales  del ' + equipo.lexema + ' fue:  ' + str(goles)

        return resultado



    def EJECUTAR_TABLA(self):
        pass

    def EJECUTAR_PARTIDOS(self):
        pass

    def EJECUTAR_TOP(self):
        pass



