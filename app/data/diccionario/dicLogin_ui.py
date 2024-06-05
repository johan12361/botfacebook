# TT view Login
class Login:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Login
        self.titIniciarSesion = ""
        self.labelTexFielCorreo = ""
        self.labelTexFielClave = ""
        self.CheckUsarCookies = ""
        self.CheckUsarCookies_Tool = ""
        self.btBorrarCookies_Tool = ""
        self.btIniciar = ""
        self.btDetener = ""
        self.btIniciarManual_Tool = ""
        self.btContinuar = ""
        self.titVantanaProgreso = ""
        self.webAbierta = ""

        # SS Español
        if lenguaje == "ES":
            self.titIniciarSesion = "Iniciar sesión Facebook"
            self.labelTexFielCorreo = "Correo"
            self.labelTexFielClave = "Contraseña"
            self.CheckUsarCookies = "Usar cookies"
            self.CheckUsarCookies_Tool = "Se guardarán cookies para iniciar sesión"
            self.btBorrarCookies_Tool = "Borrar cookies"
            self.btIniciar = "Iniciar"
            self.btDetener = "Detener"
            self.btIniciarManual_Tool = "Iniciar manualmente"
            self.btContinuar = "CONTINUAR"
            self.titVantanaProgreso = "Progreso"
            self.webAbierta = "Web Abierta"

        # SS Ingles
        if lenguaje == "EN":
            self.titIniciarSesion = "Login Facebook"
            self.labelTexFielCorreo = "Email"
            self.labelTexFielClave = "Password"
            self.CheckUsarCookies = "Save cookies"
            self.CheckUsarCookies_Tool = "Cookies will be saved to log in"
            self.btBorrarCookies_Tool = "Delete cookies"
            self.btIniciar = "Login"
            self.btDetener = "Stop"
            self.btIniciarManual_Tool = "Start manually"
            self.btContinuar = "NEXT"
            self.titVantanaProgreso = "Progress"
            self.webAbierta = "Web Online"


# TT View Model
class VMLogin:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Login
        self.avis_Cookies = []
        self.avis_Web = []

        # SS Español
        if lenguaje == "ES":
            # COOKIES 10
            self.avis_Cookies.append("Buscando cookies en: ")  # 0
            self.avis_Cookies.append("Eliminando cookies...")  # 1
            self.avis_Cookies.append("Cookies eliminadas")  # 2
            self.avis_Cookies.append("No hay cookies por eliminar")  # 3
            self.avis_Cookies.append("Cookies encontradas")  # 4
            self.avis_Cookies.append("Inicio de sesión con cookies")  # 5
            self.avis_Cookies.append("No existe cookies guardadas")  # 6
            self.avis_Cookies.append("Guardando cookies...")  # 7
            self.avis_Cookies.append("Cookies guardadas")  # 8
            self.avis_Cookies.append("Inicio de sesión correcto")  # 9
            self.avis_Cookies.append("Error al guardar cookies")  # 10

            # WEB - NAVEGADOR 8
            self.avis_Web.append("Cerrando navegador...")  # 0
            self.avis_Web.append("Navegador cerrado")  # 1
            self.avis_Web.append("Iniciando navegador...")  # 2
            self.avis_Web.append("Usando webdriver externo...")  # 3
            self.avis_Web.append("Usando webdriver: ")  # 4
            self.avis_Web.append("No se encontro el driver en: ")  # 5
            self.avis_Web.append("Usando webdriver interno...")  # 6
            self.avis_Web.append("Descargando driver...")  # 7
            self.avis_Web.append("Navegador iniciado")  # 8

        # SS Ingles
        if lenguaje == "EN":
            # COOKIES 10
            self.avis_Cookies.append("Searching for cookies in: ")  # 0
            self.avis_Cookies.append("Deleting cookies...")  # 1
            self.avis_Cookies.append("Cookies deleted")  # 2
            self.avis_Cookies.append("There are no cookies to delete")  # 3
            self.avis_Cookies.append("Cookies found")  # 4
            self.avis_Cookies.append("Login with cookies")  # 5
            self.avis_Cookies.append("There are no cookies saved")  # 6
            self.avis_Cookies.append("Saving cookies...")  # 7
            self.avis_Cookies.append("Saved cookies")  # 8
            self.avis_Cookies.append("Successful login")  # 9
            self.avis_Cookies.append("Error saving cookies")  # 10

            # WEB - NAVEGADOR 8
            self.avis_Web.append("Closing browser...")  # 0
            self.avis_Web.append("Browser closed")  # 1
            self.avis_Web.append("Starting browser...")  # 2
            self.avis_Web.append("Using external webdriver...")  # 3
            self.avis_Web.append("Using webdriver: ")  # 4
            self.avis_Web.append("The driver was not found in: ")  # 5
            self.avis_Web.append("Using internal webdriver...")  # 6
            self.avis_Web.append("Downloading driver...")  # 7
            self.avis_Web.append("Browser started")  # 8


# TT AC Login
class ACLogin:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Login
        self.avis_IrPerfil = []
        self.avis_LoginAuro = []
        self.avis_LoginManual = []

        # SS Español
        if lenguaje == "ES":
            # IR A PERFIL CON COOKIES 13 ES
            self.avis_IrPerfil.append("Buscando cookies...")  # 0
            self.avis_IrPerfil.append("Cookies encontradas")  # 1
            self.avis_IrPerfil.append("Cargando pagina: ")  # 2
            self.avis_IrPerfil.append("Cargando cookies")  # 3
            self.avis_IrPerfil.append("Cookies cargadas")  # 4
            self.avis_IrPerfil.append("No se encontraron cookies")  # 5
            self.avis_IrPerfil.append("Inicia sesión con datos de cuenta")  # 6
            self.avis_IrPerfil.append("Cargando perfil...")  # 7
            self.avis_IrPerfil.append("Perfil cargado con éxito")  # 8
            self.avis_IrPerfil.append("Error al cargar perfil")  # 9
            self.avis_IrPerfil.append("Guardando cookies...")  # 10
            self.avis_IrPerfil.append("Cookies guardadas")  # 11
            self.avis_IrPerfil.append("Inicio de sesión correcto")  # 12
            self.avis_IrPerfil.append("Presione continuar")  # 13

            # INICIAR AUTOMATICAMENTE 19 ES
            self.avis_LoginAuro.append("Buscando cookies anteriores")  # 0
            self.avis_LoginAuro.append("Se eliminaron las cookies anteriores")  # 1
            self.avis_LoginAuro.append("Cargando página: ")  # 2
            self.avis_LoginAuro.append("Página cargada")  # 3
            self.avis_LoginAuro.append("Buscando input de correo")  # 4
            self.avis_LoginAuro.append("No se encontró input de correo")  # 5
            self.avis_LoginAuro.append("Escribiendo correo...")  # 6
            self.avis_LoginAuro.append("Correo escrito con éxito")  # 7
            self.avis_LoginAuro.append("Buscando input de contraseña")  # 8
            self.avis_LoginAuro.append("No se encontró input de contraseña")  # 9
            self.avis_LoginAuro.append("Escribiendo contraseña...")  # 10
            self.avis_LoginAuro.append("Contraseña escrita con éxito")  # 11
            self.avis_LoginAuro.append("Buscando botón de inicio de sesión")  # 12
            self.avis_LoginAuro.append("No se encontró botón de inicio de sesión")  # 13
            self.avis_LoginAuro.append("Botón de inicio de sesión presionado")  # 14
            self.avis_LoginAuro.append("Cargando perfil...")  # 15
            self.avis_LoginAuro.append("Perfil cargado con éxito")  # 16
            self.avis_LoginAuro.append("Error al cargar página de perfil")  # 17
            self.avis_LoginAuro.append("Inicio de sesión correcto")  # 18
            self.avis_LoginAuro.append("Presione continuar")  # 19

            # INICIAR MANUALMENTE 3 ES
            self.avis_LoginManual.append("Cargando página: ")  # 0
            self.avis_LoginManual.append("Página cargada")  # 1
            self.avis_LoginManual.append(
                "Presiona continuar cuando la sesión esté abierta"
            )  # 2

        # SS Ingles
        if lenguaje == "EN":
            # IR A PERFIL CON COOKIES 13 EN
            self.avis_IrPerfil.append("Looking for cookies...")  # 0
            self.avis_IrPerfil.append("Cookies found")  # 1
            self.avis_IrPerfil.append("Loading page: ")  # 2
            self.avis_IrPerfil.append("Loading cookies")  # 3
            self.avis_IrPerfil.append("Cookies loaded")  # 4
            self.avis_IrPerfil.append("No cookies found")  # 5
            self.avis_IrPerfil.append("Log in with account details")  # 6
            self.avis_IrPerfil.append("Loading profile...")  # 7
            self.avis_IrPerfil.append("Profile uploaded successfully")  # 8
            self.avis_IrPerfil.append("Error loading profile")  # 9
            self.avis_IrPerfil.append("Saving cookies...")  # 10
            self.avis_IrPerfil.append("Saved cookies")  # 11
            self.avis_IrPerfil.append("Successful login")  # 12
            self.avis_IrPerfil.append("Press next")  # 13

            # INICIAR AUTOMATICAMENTE 19 ES
            self.avis_LoginAuro.append("Searching for previous cookies")  # 0
            self.avis_LoginAuro.append("Previous cookies have been deleted")  # 1
            self.avis_LoginAuro.append("Loading page: ")  # 2
            self.avis_LoginAuro.append("Page loaded")  # 3
            self.avis_LoginAuro.append("Searching for email input")  # 4
            self.avis_LoginAuro.append("No email entry found")  # 5
            self.avis_LoginAuro.append("Writing email...")  # 6
            self.avis_LoginAuro.append("Mail written successfully")  # 7
            self.avis_LoginAuro.append("Searching for password input")  # 8
            self.avis_LoginAuro.append("No password entry found")  # 9
            self.avis_LoginAuro.append("Entering password...")  # 10
            self.avis_LoginAuro.append("Password typed successfully")  # 11
            self.avis_LoginAuro.append("Searching login button")  # 12
            self.avis_LoginAuro.append("No login button found")  # 13
            self.avis_LoginAuro.append("Login button pressed")  # 14
            self.avis_LoginAuro.append("Loading profile...")  # 15
            self.avis_LoginAuro.append("Profile uploaded successfully")  # 16
            self.avis_LoginAuro.append("Error loading profile page")  # 17
            self.avis_LoginAuro.append("Successful login")  # 18
            self.avis_LoginAuro.append("Press next")  # 19

            # INICIAR MANUALMENTE 3 ES
            self.avis_LoginManual.append("Loading page: ")  # 0
            self.avis_LoginManual.append("Page loaded")  # 1
            self.avis_LoginManual.append("Press next when logged in")  # 2
