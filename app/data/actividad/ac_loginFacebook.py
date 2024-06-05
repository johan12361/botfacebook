from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import os

# TT archivos
from data.enums import ColorAviso
from data.gestroDatos import CargarConfig
from data import simulador as sim
from data.singeltons import Driver as DD
from data.diccionario.dicLogin_ui import ACLogin as Dic


# SS Ir a perfil con cookies
def IraPerfil(aviso: list[str, ColorAviso], logLogrado: bool):

    driver = DD.driver
    config = CargarConfig()
    dic = Dic(config.lenguaje)

    urlPerfil = "https://www.facebook.com/profile/"
    urlRobot = "https://www.facebook.com/robots.txt"

    # TT Cargar cookies

    # Buscando cookies...
    aviso([dic.avis_IrPerfil[0], ColorAviso.ok])
    # TT Cargar cookies
    if os.path.isfile(config.rutaCookies):
        # Cookies encontradas
        aviso([dic.avis_IrPerfil[1], ColorAviso.ok])
        cookies = pickle.load(open(config.rutaCookies, "rb"))
        # Cargando pagina:
        aviso([dic.avis_IrPerfil[2] + urlRobot, ColorAviso.ok])
        driver.get(urlRobot)
        time.sleep(1)
        # Cargando cookies
        aviso([dic.avis_IrPerfil[3], ColorAviso.ok])
        for cookie in cookies:
            driver.add_cookie(cookie)
        # Cookies cargadas
        aviso([dic.avis_IrPerfil[4], ColorAviso.correcto])
        cookies
    else:
        # No se encontraron cookies
        aviso([dic.avis_IrPerfil[5], ColorAviso.error])
        # Inicia sesión con datos de cuenta
        aviso([dic.avis_IrPerfil[6], ColorAviso.precaucion])
        return

    time.sleep(2)
    # Cargando perfil...
    aviso([dic.avis_IrPerfil[7], ColorAviso.ok])
    driver.get(urlPerfil)
    time.sleep(2)
    print(driver.current_url)
    # Comprobar si se cargo el perfil
    comUrl = sim.CompprobarUrl(
        url=driver.current_url, buscar=["profile", "id="], pocetaje=0.8
    )

    if comUrl:
        # Perfil cargado con éxito
        aviso([dic.avis_IrPerfil[8], ColorAviso.correcto])
    else:
        # Error al cargar perfil
        aviso([dic.avis_IrPerfil[9], ColorAviso.error])
        return

    # guardar Cookies
    cookies = driver.get_cookies()
    # Guardando cookies...
    aviso([dic.avis_IrPerfil[10], ColorAviso.ok])
    pickle.dump(cookies, open(config.rutaCookies, "wb"))
    # Cookies guardadas
    aviso([dic.avis_IrPerfil[11], ColorAviso.ok])
    # Inicio de sesión correcto
    aviso([dic.avis_IrPerfil[12], ColorAviso.correcto])
    # Presione continuar
    aviso([dic.avis_IrPerfil[13], ColorAviso.correcto])
    logLogrado(True)


# SS Hacer Login auromatico
def login(correo: str, clave: str, aviso: list[str, ColorAviso], logLogrado: bool):

    driver = DD.driver
    config = CargarConfig()
    dic = Dic(config.lenguaje)

    # TT Datos
    urlLog = "https://www.facebook.com/login/"
    urlPerfil = "https://www.facebook.com/profile/"
    wait = WebDriverWait(driver, 10)

    # TT Borrar Cookies
    # Buscando cookies anteriores
    aviso([dic.avis_LoginAuro[0], ColorAviso.ok])
    if os.path.isfile(config.rutaCookies):
        os.remove(config.rutaCookies)
        # Se eliminaron los cookies anteriores para nuevo inicio de sesión
        aviso(
            [
                dic.avis_LoginAuro[1],
                ColorAviso.precaucion,
            ]
        )

    # SS Iniciar opracions
    time.sleep(2)
    # Iniciar pagina
    # Cargando página:
    aviso([dic.avis_LoginAuro[2] + urlLog, ColorAviso.ok])
    driver.get(urlLog)
    # Página cargada
    aviso([dic.avis_LoginAuro[3], ColorAviso.ok])

    # esperar base
    time.sleep(2)

    # introducir correo
    # Buscando input de correo
    aviso([dic.avis_LoginAuro[4], ColorAviso.ok])
    try:
        elemento = wait.until(EC.presence_of_element_located((By.ID, "email")))
    except TimeoutException:
        # No se encontró input de correo
        aviso([dic.avis_LoginAuro[5], ColorAviso.error])
        return
    elemento.click()
    # Escribiendo correo...
    aviso([dic.avis_LoginAuro[6], ColorAviso.ok])
    sim.Teclear(ele=elemento, texto=correo)
    # Correo escrito con éxito
    aviso([dic.avis_LoginAuro[7], ColorAviso.ok])

    # introducir contraseña
    # Buscando input de contraseña
    aviso([dic.avis_LoginAuro[8], ColorAviso.ok])
    try:
        elemento = wait.until(EC.presence_of_element_located((By.ID, "pass")))
    except TimeoutException:
        # No se encontró input de contraseña
        aviso([dic.avis_LoginAuro[9], ColorAviso.error])
        return
    elemento.click()
    # Escribiendo contraseña...
    aviso([dic.avis_LoginAuro[10], ColorAviso.ok])
    sim.Teclear(ele=elemento, texto=clave)
    # Contraseña escrita con éxito
    aviso([dic.avis_LoginAuro[11], ColorAviso.ok])

    # bt login
    # Buscando botón de inicio de sesión
    aviso([dic.avis_LoginAuro[12], ColorAviso.ok])
    try:
        elemento = wait.until(EC.presence_of_element_located((By.ID, "loginbutton")))
    except TimeoutException:
        # No se encontró botón de inicio de sesión
        aviso([dic.avis_LoginAuro[13], ColorAviso.error])
        return
    elemento.click()
    # Botón de inicio de sesión presionado
    aviso([dic.avis_LoginAuro[14], ColorAviso.ok])

    # TT Comprobar casos
    # ir a perfil
    time.sleep(3)
    # Cargando perfil...
    aviso([dic.avis_LoginAuro[15], ColorAviso.ok])
    driver.get(urlPerfil)
    print(driver.current_url)
    # Comprobar si se cargo el perfil
    comUrl = sim.CompprobarUrl(
        url=driver.current_url, buscar=["profile", "id="], pocetaje=0.8
    )

    if comUrl:
        # Perfil cargado con éxito
        aviso([dic.avis_LoginAuro[16], ColorAviso.ok])
    else:
        # Error al cargar página de perfil
        aviso([dic.avis_LoginAuro[17], ColorAviso.error])
        return

    # Inicio de sesión correcto
    aviso([dic.avis_LoginAuro[18], ColorAviso.correcto])
    # Presione continuar
    aviso([dic.avis_LoginAuro[19], ColorAviso.correcto])
    logLogrado(True)


# SS Login manual
def LogManual(aviso: list[str, ColorAviso]):

    config = CargarConfig()
    dic = Dic(config.lenguaje)

    time.sleep(2)

    driver = DD.driver
    # TT Datos
    urlLog = "https://www.facebook.com/login/"

    # Iniciar pagina
    # Cargando página:
    aviso([dic.avis_LoginManual[0] + urlLog, ColorAviso.ok])
    driver.get(urlLog)
    # Página cargada
    aviso([dic.avis_LoginManual[1], ColorAviso.ok])
    # esperar base
    time.sleep(2)
    # Presiona continuar cuando la sesión esté abierta
    aviso([dic.avis_LoginManual[2], ColorAviso.correcto])
