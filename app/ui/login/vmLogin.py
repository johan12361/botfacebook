from selenium import webdriver
import time
import pickle
import os

# TT archivos
from data.actividad import ac_loginFacebook
from data.confNavegador import confNav
from data.enums import ColorAviso
from data.gestroDatos import CargarConfig, CargarDriverInterno
from data.singeltons import Driver as DD
from data.diccionario.dicLogin_ui import VMLogin as Dic


# up#i58Q56^V!jA
# de.fogon.a.mesa@gmail.com

# .\Res\driversWeb\chromedriver.exe


class VmLogin:
    # SS variables
    def __init__(self, aviso: list[str, ColorAviso], logLogrado: bool):

        # Config
        self.config = CargarConfig()
        # diciionario
        self.dic = Dic(self.config.lenguaje)

        self.correo: str = ""
        self.clave: str = ""
        self.usarCookies = False
        self.opNav = webdriver.ChromeOptions()
        self.webAbierta = False
        # Infladas
        self.aviso: list[str, ColorAviso] = aviso
        self.logLogrado: bool = logLogrado

    # TT UI
    def ActualizarCorreo(self, e: str):
        self.correo = e

    def ActualizarClave(self, e: str):
        self.clave = e

    def ActualizarIniciado(self, e: bool):
        self.usarCookies = e
        print(self.usarCookies)

    def BorrarCookies(self):
        # Buscando cookies en:
        self.aviso([self.dic.avis_Cookies[0] + self.config.rutaCookies, ColorAviso.ok])
        if os.path.isfile(self.config.rutaCookies):
            # Eliminando cookies...
            self.aviso([self.dic.avis_Cookies[1], ColorAviso.precaucion])
            os.remove(self.config.rutaCookies)
            # Cookies eliminadas
            self.aviso([self.dic.avis_Cookies[2], ColorAviso.correcto])
        else:
            # No hay cookies por eliminar
            self.aviso([self.dic.avis_Cookies[3], ColorAviso.precaucion])

    def ComprobarCokkies(self):
        # Buscando cookies en:
        self.aviso([self.dic.avis_Cookies[0] + self.config.rutaCookies, ColorAviso.ok])
        if os.path.isfile(self.config.rutaCookies):
            # Cookies encontradas
            self.aviso([self.dic.avis_Cookies[4], ColorAviso.ok])
            # Inicio de sesión con cookies
            self.aviso([self.dic.avis_Cookies[5], ColorAviso.correcto])
            self.usarCookies = True
        else:
            # no existe cookies guardadas
            self.aviso([self.dic.avis_Cookies[6], ColorAviso.precaucion])
            self.usarCookies = False

    def GuardarCookies(self):
        try:
            cookies = DD.driver.get_cookies()
            # Guardando cookies...
            self.aviso([self.dic.avis_Cookies[7], ColorAviso.ok])
            pickle.dump(cookies, open(self.config.rutaCookies, "wb"))
            # Cookies guardadas
            self.aviso([self.dic.avis_Cookies[8], ColorAviso.correcto])
            # Inicio de sesión correcto
            self.aviso([self.dic.avis_Cookies[9], ColorAviso.correcto])
        except:
            # Error al guardar cookies
            self.aviso([self.dic.avis_Cookies[10], ColorAviso.precaucion])
            return False
        return True

    # TT Navegacion
    def DetenerWeb(self):
        # Cerrando navegador...
        self.aviso([self.dic.avis_Web[0], ColorAviso.precaucion])
        DD.driver.quit()
        self.webAbierta = False
        # Navegador cerrado
        self.aviso([self.dic.avis_Web[1], ColorAviso.correcto])

    # Manual
    def InicioManual(self):
        confNav.confBase(self.opNav)
        # Iniciando navegador...
        self.aviso([self.dic.avis_Web[2], ColorAviso.ok])

        # slelecionar driver
        if self.config.usarWebdriver:
            # Usando webdriver externo...
            self.aviso([self.dic.avis_Web[3], ColorAviso.ok])
            if os.path.isfile(self.config.rutaWebdriver):
                # Usando webdriver:
                self.aviso(
                    [self.dic.avis_Web[4] + self.config.rutaWebdriver, ColorAviso.ok]
                )
                DD.driver = webdriver.Chrome(
                    service=self.config.rutaWebdriver, options=self.opNav
                )
            else:
                # no se encontro el driver en:
                self.aviso(
                    [
                        self.dic.avis_Web[5] + self.config.rutaWebdriver,
                        ColorAviso.precaucion,
                    ]
                )
                time.sleep(1)
                # Usando webdriver interno...
                self.aviso([self.dic.avis_Web[6], ColorAviso.ok])
                if not os.path.isdir(self.config.rutaDriverInterno + "\\" + ".wdm"):
                    # Descargando driver...
                    self.aviso([self.dic.avis_Web[7], ColorAviso.correcto])
                driver = CargarDriverInterno(self.config.rutaDriverInterno)
                DD.driver = webdriver.Chrome(options=self.opNav, service=driver)
        else:
            # Usando webdriver interno...
            self.aviso([self.dic.avis_Web[6], ColorAviso.ok])
            if not os.path.isdir(self.config.rutaDriverInterno + "\\" + ".wdm"):
                # Descargando driver...
                self.aviso([self.dic.avis_Web[7], ColorAviso.correcto])

            driver = CargarDriverInterno(self.config.rutaDriverInterno)
            DD.driver = webdriver.Chrome(options=self.opNav, service=driver)

        DD.driver.maximize_window()
        self.webAbierta = True
        # Navegador iniciado
        self.aviso([self.dic.avis_Web[8], ColorAviso.correcto])
        self.logLogrado(True)
        ac_loginFacebook.LogManual(aviso=self.aviso)

    def IniciarWeb(self):
        confNav.confBase(self.opNav)
        # Iniciando navegador...
        self.aviso([self.dic.avis_Web[2], ColorAviso.ok])

        # slelecionar driver
        if self.config.usarWebdriver:
            # Usando webdriver externo...
            self.aviso([self.dic.avis_Web[3], ColorAviso.ok])
            if os.path.isfile(self.config.rutaWebdriver):
                self.aviso(
                    # Usando webdriver:
                    [self.dic.avis_Web[4] + self.config.rutaWebdriver, ColorAviso.ok]
                )
                DD.driver = webdriver.Chrome(
                    service=self.config.rutaWebdriver, options=self.opNav
                )
            else:
                # No se encontro el driver en:
                self.aviso(
                    [
                        self.dic.avis_Web[5] + self.config.rutaWebdriver,
                        ColorAviso.precaucion,
                    ]
                )
                time.sleep(1)
                # Usando webdriver interno...
                self.aviso([self.dic.avis_Web[6], ColorAviso.ok])
                driver = CargarDriverInterno(self.config.rutaDriverInterno)
            DD.driver = webdriver.Chrome(options=self.opNav, service=driver)
        else:
            # Usando webdriver interno...
            self.aviso([self.dic.avis_Web[6], ColorAviso.ok])
            driver = CargarDriverInterno(self.config.rutaDriverInterno)
            DD.driver = webdriver.Chrome(options=self.opNav, service=driver)

        DD.driver.maximize_window()
        self.webAbierta = True
        # Navegador iniciado"
        self.aviso([self.dic.avis_Web[8], ColorAviso.correcto])
        if self.usarCookies == False:
            ac_loginFacebook.login(
                correo=self.correo,
                clave=self.clave,
                aviso=self.aviso,
                logLogrado=self.logLogrado,
            )
        else:
            ac_loginFacebook.IraPerfil(
                aviso=self.aviso,
                logLogrado=self.logLogrado,
            )
