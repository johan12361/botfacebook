from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# TT archivos
from data.enums import ColorAviso
from data.singeltons import Driver as DD
from data.singeltons import IdGrupo
from data.gestroDatos import CargarConfig
from data.gestroDatos import GuardarGrupo
from data.diccionario.dicListaGrupos_ui import ACListaGrupos as Dic
from data.diccionario.dicWeb import PaginaGrupos as DicWeb


def RecopilarDatos(idGrupo: IdGrupo, aviso: list[str, ColorAviso]):

    config = CargarConfig()
    dic = Dic(config.lenguaje)
    dicWeb = DicWeb(config.facebookLeng)

    driver = DD.driver
    url = idGrupo.url
    wait = WebDriverWait(driver, 10)
    # Cargando grupo:
    aviso([dic.avis_ObtenerDatos[0] + url, ColorAviso.ok])
    # ir a url
    try:
        driver.get(url)
    except:
        # Error al acceder al navegador
        return "FIN-" + dic.avis_ObtenerDatos[1]

    # esperando a que carge
    # Cargando página...
    aviso([dic.avis_ObtenerDatos[2], ColorAviso.ok])
    try:
        elemento = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span/a")))
    except TimeoutException:
        # Página tardó demasiado en responder
        return dic.avis_ObtenerDatos[3]

    # Buscando datos grupo...
    aviso([dic.avis_ObtenerDatos[4], ColorAviso.ok])
    try:
        idGrupo.nombre = driver.find_element(By.XPATH, "//h1/span/a").get_attribute(
            "text"
        )
        # Título de grupo:
        aviso([dic.avis_ObtenerDatos[5] + idGrupo.nombre, ColorAviso.ok])
    except:
        # No se encontró título de grupo
        aviso([dic.avis_ObtenerDatos[6], ColorAviso.precaucion])

    try:
        idGrupo.img = driver.find_element(
            By.XPATH, "//img[@data-imgperflogname='profileCoverPhoto']"
        ).get_attribute("src")
    except:
        # No se encontró portada de grupo
        aviso([dic.avis_ObtenerDatos[7], ColorAviso.precaucion])

    try:
        idGrupo.miembros = driver.find_elements(
            By.XPATH, f"//a[contains(text(),'{dicWeb.eti_miembros}')]"
        )[0].get_attribute("text")
    except:
        # No se encontró cantidad de miembros del grupo
        aviso([dic.avis_ObtenerDatos[8], ColorAviso.precaucion])
    # Guardando datos grupo
    aviso([dic.avis_ObtenerDatos[9], ColorAviso.correcto])
    GuardarGrupo(idGrupo)
