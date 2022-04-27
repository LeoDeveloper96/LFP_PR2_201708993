class AnalizadorSintactico:

    def __init__(self, tokens: list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self, esperado, obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido, esperado)
        )

    def sacarToken(self):
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        try:
            return self.tokens[0]
        except:
            return None

    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        # Observar el primer elemento para
        # decidir a donde ir
        temporal = self.observarToken()
        if temporal is None:
            self.agregarError("reservada_RESULTADO | reservada_JORNADA | reservada_GOLES | reservada_TABLA| "
                              "reservada_PARTIDOS|reservada_TOP ", "EOF")
        elif temporal.tipo == 'reservada_RESULTADO':
            self.RESULTADO()
        elif temporal.tipo == 'reservada_JORNADA':
            self.JORNADA()
        elif temporal.tipo == 'reservada_GOLES':
            self.GOLES()
        elif temporal.tipo == 'reservada_TABLA':
            self.TABLA()
        elif temporal.tipo == 'reservada_PARTIDOS':
            self.PARTIDOS()
        elif temporal.tipo == 'reservada_TOP':
            self.TOP()
        else:
            self.agregarError("reservada_RESULTADO | reservada_JORNADA | reservada_GOLES | reservada_TABLA| "
                              "reservada_PARTIDOS | reservada_TOP ", temporal.tipo)

    def RESULTADO(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_RESULTADO':
            # Sacar otro token --- se espera nombre del equipo
            token = self.sacarToken()
            if token is None:
                self.agregarError("Equipo", "EOF")
                return
            elif token.tipo == "Equipo":
                # Sacar otro token --- se espera VS
                token = self.sacarToken()
                if token is None:
                    self.agregarError("VS", "EOF")
                    return
                elif token.tipo == "VS":
                    # Sacar otro token --- se espera Nombre equipo
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("Equipo", "EOF")
                        return
                    elif token.tipo == "Equipo":
                        # Sacar otro token --- se espera Temporada
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("reservada_TEMPORADA", "EOF")
                            return
                        elif token.tipo == "reservada_TEMPORADA":
                            # Sacar otro token --- se espera Intervalo <YYYY-YYYY>
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("Intervalo", "EOF")
                                return
                            elif token.tipo == "Intervalo":
                                # Llamo a mi funcionalidad
                                pass
                            else:
                                self.agregarError("Intervalo", token.tipo)
                        else:
                            self.agregarError("reservada_TEMPORADA", token.tipo)
                    else:
                        self.agregarError("Equipo", token.tipo)
                else:
                    self.agregarError("VS", token.tipo)
            else:
                self.agregarError("Equipo", token.tipo)
        else:
            self.agregarError("reservada_RESULTADO", "EOF")

    def JORNADA(self):
        # Producción
        #JORNADA ::= pr_jornada numero pr_temporada intervalo BANDERA
        bandera = None
        token = self.sacarToken()
        if token.tipo == 'reservada_JORNADA':
            # Sacar otro token --- se espera nombre un numero
            token = self.sacarToken()
            if token is None:
                self.agregarError("Numero", "EOF")
                return
            elif token.tipo == "Numero":
                # Sacar otro token --- se espera nombre  pr_temporada
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_TEMPORADA", "EOF")
                    return
                elif token.tipo == "reservada_TEMPORADA":
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("Intervalo", "EOF")
                        return
                    elif token.tipo == "Intervalo":
                        #aqui viene la bandera
                        bandera = self.BANDERAT()
                        if bandera is None:
                            # ejecuto mi funcionalidad
                            # uso el nombre de archivo por defecto
                            pass
                        else:
                            # ejecuto mi funcionalidad
                            # uso el nombre del archivo proporcionado
                            pass
                    else:
                        self.agregarError("Intervalo", token.tipo)
                else:
                    self.agregarError("reservada_TEMPORADA", token.tipo)
            else:
                self.agregarError("Numero", token.tipo)
        else:
            self.agregarError("reservada_JORNADA", "EOF")

    def GOLES(self):
        condicion = None
        token = self.sacarToken()
        if token.tipo == 'reservada_GOLES':
            # Sacar otro token --- se espera nombre una condicion para el equipo
            condicion = self.CONDICIONEQUIPO()
            if condicion is None:
                return
            # Sacar otro token --- se espera nombre  pr_temporada
            token = self.sacarToken()
            if token is None:
                self.agregarError("reservada_TEMPORADA", "EOF")
                return
            elif token.tipo == "reservada_TEMPORADA":
                # Sacar otro token --- se espera nombre  intervalo
                token = self.sacarToken()
                if token is None:
                    self.agregarError("Intervalo", "EOF")
                    return
                elif token.tipo == "Intervalo":
                    # aqui viene la bandera
                    bandera = self.BANDERAT()
                    if bandera is None:
                        # ejecuto mi funcionalidad
                        # uso el nombre de archivo por defecto
                        pass
                    else:
                        # ejecuto mi funcionalidad
                        # uso el nombre del archivo proporcionado
                        pass
        else:
            self.agregarError("reservada_GOLES", "EOF")

    def TABLA(self):
        # TABLA ::= pr_tabla pr_temporada intervalo BANDERA
        bandera = None
        token = self.sacarToken()
        if token.tipo == 'reservada_TABLA':
            # Sacar otro token --- se espera pr_temporada
            token = self.sacarToken()
            if token is None:
                self.agregarError("reservada_TEMPORADA", "EOF")
                return
            elif token.tipo == "reservada_TEMPORADA":
                # Sacar otro token --- se espera nombre  intervalo
                token = self.sacarToken()
                if token is None:
                    self.agregarError("Intervalo", "EOF")
                    return
                elif token.tipo == "Intervalo":
                    # aqui viene la bandera
                    bandera = self.BANDERAT()
                    if bandera is None:
                        # ejecuto mi funcionalidad
                        # uso el nombre de archivo por defecto
                        pass
                    else:
                        # ejecuto mi funcionalidad
                        # uso el nombre del archivo proporcionado
                        pass
        else:
            self.agregarError("reservada_TABLA", "EOF")

    def PARTIDOS(self):
        # PARTIDOS ::= pr_PARTIDOS equipo pr_temporada intervalo BANDERAS
        banderas = None
        token = self.sacarToken()
        if token.tipo == 'reservada_PARTIDOS':
            # Sacar otro token --- se espera nombre del equipo
            token = self.sacarToken()
            if token is None:
                self.agregarError("Equipo", "EOF")
                return
            elif token.tipo == "Equipo":
                # Sacar otro token --- se espera pr_temporada
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_TEMPORADA", "EOF")
                    return
                elif token.tipo == "reservada_TEMPORADA":
                    # Sacar otro token --- se espera nombre  intervalo
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("Intervalo", "EOF")
                        return
                    elif token.tipo == "Intervalo":
                        # aqui viene la bandera
                        banderas = self.BANDERAS()
                        if banderas is None:
                            # ejecuto mi funcionalidad
                            # uso el nombre de archivo por defecto
                            pass
                        else:
                            # ejecuto mi funcionalidad
                            # uso el nombre del archivo proporcionado
                            pass
        else:
            self.agregarError("reservada_PARTIDOS", "EOF")

    def TOP(self):

        # TOP ::= pr_TOP CONDICION pr_temporada intervalo BANDERATOP
        banderas = None
        token = self.sacarToken()
        if token.tipo == 'reservada_Top':
            # Sacar otro token --- se espera una condicion
            condicion = self.CONDICION()
            if condicion is None:
                return
            # Sacar otro token --- se espera nombre  pr_temporada
            token = self.sacarToken()
            if token is None:
                self.agregarError("reservada_TEMPORADA", "EOF")
                return
            elif token.tipo == "reservada_TEMPORADA":
                # Sacar otro token --- se espera nombre  intervalo
                token = self.sacarToken()
                if token is None:
                    self.agregarError("Intervalo", "EOF")
                    return
                elif token.tipo == "Intervalo":
                    # aqui viene la bandera
                    bandera = self.BANDERAT()
                    if bandera is None:
                        # ejecuto mi funcionalidad
                        # uso el nombre de archivo por defecto
                        pass
                    else:
                        # ejecuto mi funcionalidad
                        # uso el nombre del archivo proporcionado
                        pass

        else:
            self.agregarError("reservada_TOP", "EOF")

    def BANDERAT(self):
        # Producción
        # BANDERA ::= pr_-f archivo | epsilon
        lista = []
        token = self.observarToken()
        if token is None:
            return
        if token.tipo == 'bandera_-f':
            # saco el nombre del archivo
            token = self.observarToken()
            lista.append(token)
            if token is None:
                self.agregarError("Archivo", "EOF")
                return
            elif token.tipo == "Archivo":
                lista.append(token)
                return lista
            else:
                self.agregarError("Archivo", "EOF")
        else:
            self.agregarError("bandera_-f", "EOF")

    def BANDERATOP(self):
        # Producción
        # BANDERA ::= pr_-f archivo | epsilon
        lista = []
        token = self.observarToken()
        if token is None:
            return
        if token.tipo == 'bandera_-n':
            # saco el nombre del archivo
            token = self.observarToken()
            lista.append(token)
            if token is None:
                self.agregarError("Archivo", "EOF")
                return
            elif token.tipo == "Archivo":
                lista.append(token)
                return lista
            else:
                self.agregarError("Archivo", "EOF")

    def BANDERAS(self):
        # Producción
        # BANDERAS' ::= bandera _-f archivo | bandera _-ji número | bandera _-jf número| épsilon BANDERAS
        pass

    def CONDICIONEQUIPO(self):
        # Producción
        # CONDICIONEQUIPO ::= LOCAL | VISITANTE | TOTAL

        token = self.sacarToken()
        # Si no viene un token retornamos None para
        # Causar que no se ejecute el comando
        if token is None:
            self.agregarError("LOCAL | VISITANTE | TOTAL", "EOF")
            return
        if token.tipo == 'reservada_LOCAL':
            return token.lexema
        elif token.tipo == 'reservada_VISITANTE':
            return token.lexema
        elif token.tipo == 'reservada_TOTAL':
            return token.lexema
        else:
            self.agregarError("LOCAL | VISITANTE | TOTAL", token.tipo)

    def CONDICION(self):
        # Producción
        # CONDICION ::= SUPERIOR | INFERIOR

        token = self.sacarToken()
        # Si no viene un token retornamos None para
        # Causar que no se ejecute el comando
        if token is None:
            self.agregarError("SUPERIOR | INFERIOR", "EOF")
            return
        if token.tipo == 'reservada_SUPERIOR':
            return token.lexema
        elif token.tipo == 'reservada_INFERIOR':
            return token.lexema
        else:
            self.agregarError("SUPERIOR | INFERIOR, EOF", token.tipo)
