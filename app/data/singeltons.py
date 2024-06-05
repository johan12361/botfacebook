from selenium import webdriver


class Config:
    
    tiempobloqueo = 20
    #otros
    lenguaje = "EN"
    facebookLeng = "EN"
    

    # general
    datosGrupos = True
    esperaEntreGrupos = 15  # segundos
    reintentarPots = False
    tiempoEsperaReintento = 20  # minitus
    simularEscritura = True

    # web
    usarWebdriver = False
    rutaWebdriver = "-Ruta/Path-"
    navOculto = False
    guardarCookies = True
    modoInconigto = False

    # Rutas
    ruta = ".\Res\config.cfg"
    rutaCookies = ".\Res\cookies\FaceBook.cookies"
    rutaGrupos = ".\Res\grupos\GruposFaceBook.txt"
    rutaDriverInterno = ".\Res"


class Driver(object):
    __instance = None
    driver: webdriver.Chrome = None

    def __new__(cls):
        if Driver.__instance is None:
            print("Driver creado")
            Driver.__instance = object.__new__(cls)
        return Driver.__instance


class Info(object):
    __instance = None

    nombre = "Multi Post FB"
    version = "1.2.1"
    fecha = "05-2024"

    def __new__(cls):
        if Info.__instance is None:
            print("Info creado")
            Info.__instance = object.__new__(cls)
        return Info.__instance


# TT Clases


class IdGrupo:
    url = ""
    nombre = ""
    img = "https://www.facebook.com/favicon.ico"
    miembros = "miembros n/a"
    selec = True
    estado = ""
    # Publicando... - se esta publicando
    # publicado - se publico
    # pendiente - no se pudo publicar


class Post:

    nombre = ""
    post = ""
    link = ""
    media: list[str] = []
    grupos: list[IdGrupo] = []
    postProgramado = False
    fechaPost = None
    horaPost = None
