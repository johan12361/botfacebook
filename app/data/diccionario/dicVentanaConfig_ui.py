# TT view Config
class VentanaConfig:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Iniciar
        # dialogo
        self.titDialo = ""
        self.btGuardar = ""
        # Iconos Carrucel
        self.toolIcoGeneral = ""
        self.toolIcoWeb = ""
        # General
        self.g_DatosGrupos = ""
        self.g_EsperaGrupos = ""
        self.g_ReintetarPost = ""
        self.g_ReintentarCada = ""
        # Web
        self.w_UsarWebExterno = ""
        self.w_RutaWebDriver = ""
        self.w_OcultarNavegador = ""
        self.w_OcultarNavegadorTool = ""

        # SS Español
        if lenguaje == "ES":
            # dialogo
            self.titDialo = "Opciones"
            self.btGuardar = "Guardar"
            # Iconos Carrucel
            self.toolIcoGeneral = "General"
            self.toolIcoWeb = "Navegador"
            # General
            self.g_DatosGrupos = "Descargar datos de páginas"
            self.g_EsperaGrupos = "Espera entre publicaciones"
            self.g_ReintetarPost = "Reintentar publicar"
            self.g_ReintentarCada = "➜ Reintentar cada"
            # Web
            self.w_UsarWebExterno = "Usar WebDriver Externo"
            self.w_RutaWebDriver = "➜ Ruta WebDriver"
            self.w_OcultarNavegador = "⚠️ Ocultar navegador"
            self.w_OcultarNavegadorTool = "Para activar esta opción es necesario tener la sesión iniciada con cookies previamente"
           
           
        # SS Ingles
        if lenguaje == "EN":
            # dialogo
            self.titDialo = "Options"
            self.btGuardar = "Save"
            # Iconos Carrucel
            self.toolIcoGeneral = "General"
            self.toolIcoWeb = "Browser"
            # General
            self.g_DatosGrupos = "Download page data"
            self.g_EsperaGrupos = "Wait between posts"
            self.g_ReintetarPost = "Retry publishing"
            self.g_ReintentarCada = "➜ Retry every"
            # Web
            self.w_UsarWebExterno = "Use External WebDriver"
            self.w_RutaWebDriver = "➜ WebDriver path"
            self.w_OcultarNavegador = "⚠️ Hide browser"
            self.w_OcultarNavegadorTool = "To activate this option it is necessary to have previously logged in with cookies" 
