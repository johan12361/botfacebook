# TT view Config
class Config:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Iniciar
        # info
        self.autor = ""
        self.version = ""
        self.fechaProduccion = ""
        self.btInfo = ""
        self.titIdioma = ""
        self.titIdiomaFacebook = ""
        self.msjDonacion = ""
        self.btContinuar = ""
        self.msgCambioLeng = ""

        # mensaje espera para leer
        self.msjEspera = ""

        # SS Español
        if lenguaje == "ES":
            self.autor = "Desarrollado por: Johan S Chavez"
            self.version = "Version"
            self.fechaProduccion = "Fecha de produccion: "
            self.btInfo = "Información"
            self.titIdioma = "Idioma de app"
            self.titIdiomaFacebook = "Idioma de Facebook"
            self.msjDonacion = "El proyecto busca ser gratuito y seguir actualizándose en el futuro. Si deseas apoyar el proyecto puedes hacerlo mediante Patreon o PayPal"
            self.btContinuar = "CONTINUAR"
            self.msgCambioLeng = "Cierra e inicia de nuevo"
            # mensaje espera para leer
            self.msjEspera = "Tómate un momento para leer...\nIniciando en "

        # SS Ingles
        elif lenguaje == "EN":
            self.autor = "Developed by: Johan S Chavez"
            self.version = "Version"
            self.fechaProduccion = "Date of production: "
            self.btInfo = "Information"
            self.titIdioma = "App language"
            self.titIdiomaFacebook = "Facebook language"
            self.msjDonacion = "The Multi Post FB is free. If you want to support the project you can do so through Patreon or PayPal"
            self.btContinuar = "NEXT"
            self.msgCambioLeng = "Close and start again"
            # mensaje espera para leer
            self.msjEspera = "Take a moment to read...\nStarting in "


# TT ventana salir
class VentanaSalir:
    def __init__(self, lenguaje: str) -> None:
        self.msjDonacion = ""
        self.titConfirmar = ""
        self.msjConfirmacion = ""
        self.btSI = ""
        self.btNO = ""

        # SS Español
        if lenguaje == "ES":
            self.msjDonacion = "El proyecto busca ser gratuito y seguir actualizándose en el futuro. Si deseas apoyar el proyecto puedes hacerlo mediante Patreon o PayPal"
            self.titConfirmar = "Confirmar"
            self.msjConfirmacion = "¿Esta seguro de cerrar la Multi Post FB? Todos los procesos se cancelarán"
            self.btSI = "Si"
            self.btNO = "No"

        # SS Ingles
        elif lenguaje == "EN":
            self.msjDonacion = "The Multi Post FB is free. If you want to support the project you can do so through Patreon or PayPal"
            self.titConfirmar = "Confirm"
            self.msjConfirmacion = "Are you sure about closing Multi Post FB? All processes will be canceled"
            self.btSI = "Yes"
            self.btNO = "No"
