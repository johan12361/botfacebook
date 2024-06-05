import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# TT archivos
from data.simulador import SimularEspera, Teclear
from data.enums import ColorAviso
from data.singeltons import Driver as DD
from data import simulador as sim
from data.singeltons import IdGrupo
from data.gestroDatos import CargarConfig, GuardarGrupo
from data.diccionario.dicPublicacion_ui import ACPublicacion as Dic
from data.diccionario.dicWeb import PaginaGrupos as DicWeb


# //*[contains(@aria-label,'Foto/video')]
# //span[contains(div/@aria-label,'Foto/video')]
# //*[contains(@href,'www.facebook.com/help')]//*[contains(@href,'www.facebook.com/help')]
# //*[contains(text(),'Limitamos la frecuencia con la que puedes publicar')]  ---------------------------
# //span[contains(div/@aria-label,'Foto/video')]/div/div/div/div/div/div[2]
# //*[contains(div/span/div/@aria-label,'Foto/video')]/input
# //div[@role='button' and @aria-label='Publicar']
# //div[@role='dialog' and @aria-labelledby]//div[@role='button' and @aria-label='Publicar']


def Compartir(
    idGrupo: IdGrupo,
    post: str,
    imgs: list[str],
    link: str,
    aviso: list[str, ColorAviso],
    cancelar: bool,
):
    config = CargarConfig()
    dic = Dic(config.lenguaje)
    dicWeb = DicWeb(config.facebookLeng)
    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    url = idGrupo.url
    driver = DD.driver
    wait = WebDriverWait(driver, 10)
    comprobar = WebDriverWait(driver, 2)
    # Cargando grupo:
    aviso([dic.avis_Publicar[0] + url, ColorAviso.ok])
    # ir a url
    try:
        driver.get(url)
    except:
        # Error al acceder al navegador
        return "FIN-" + dic.avis_Publicar[1]

    time.sleep(2)
    # Comprobar url
    comUrl = sim.CompprobarUrl(
        url=driver.current_url, buscar=["facebook", "group"], pocetaje=0.8
    )
    if comUrl:
        # Página de grupo cargado con éxito
        aviso([dic.avis_Publicar[2], ColorAviso.ok])
    else:
        # Error al cargar página de grupo
        return dic.avis_Publicar[3]

    # SS datos grupo
    if config.datosGrupos:
        time.sleep(1)
        # Buscando datos grupo...
        aviso([dic.avis_Publicar[4], ColorAviso.ok])
        try:
            idGrupo.nombre = driver.find_element(By.XPATH, "//h1/span/a").get_attribute(
                "text"
            )
            # Título de grupo
            aviso([dic.avis_Publicar[5] + idGrupo.nombre, ColorAviso.ok])
        except:
            # No se encontró título de grupo
            aviso([dic.avis_Publicar[6], ColorAviso.precaucion])

        try:
            idGrupo.img = driver.find_element(
                By.XPATH, "//img[@data-imgperflogname='profileCoverPhoto']"
            ).get_attribute("src")
        except:
            # No se encontró portada de grupo
            aviso([dic.avis_Publicar[7], ColorAviso.precaucion])

        try:
            idGrupo.miembros = driver.find_elements(
                By.XPATH, f"//a[contains(text(),'{dicWeb.eti_miembros}')]"
            )[0].get_attribute("text")
        except:
            # No se encontró cantidad de miembros del grupo
            aviso([dic.avis_Publicar[8], ColorAviso.precaucion])

    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    # Guardando datos grupo...
    aviso([dic.avis_Publicar[9], ColorAviso.correcto])
    new = IdGrupo()
    new.url = idGrupo.url
    new.nombre = idGrupo.nombre
    new.miembros = idGrupo.miembros
    new.img = idGrupo.img
    GuardarGrupo(new)
    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    # SS Buscar caja de publicacion
    # Buscando input de publicación...
    aviso([dic.avis_Publicar[10], ColorAviso.ok])
    try:
        elemento = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//span[contains(text(),'{dicWeb.input_PublicMain}')]")
            )
        )
    except TimeoutException:
        # No se encontró input de publicación
        return dic.avis_Publicar[11]

    # centrar -scroll
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elemento)
    elemento.click()

    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    # SS Subir Archivos
    if imgs != []:
        time.sleep(1)
        # Cargando archivos...
        aviso([dic.avis_Publicar[12], ColorAviso.ok])
        try:
            elemento = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[@aria-label = '{dicWeb.bt_FotoVideo}']")
                )
            )
        except TimeoutException:
            # No se encontró botón de agregar media
            return dic.avis_Publicar[13]
        elemento.click()
        time.sleep(1)

        try:
            # Cargando archivos 2...
            aviso([dic.avis_Publicar[14], ColorAviso.ok])
            elemento = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//input[@accept ='image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv']",
                    )
                )
            )
        except TimeoutException:
            # No se encontró botón de agregar media 2
            return dic.avis_Publicar[15]

        rutas = ""
        for i in range(len(imgs)):
            new = imgs[i].replace("\n", "")
            if i < len(imgs) - 1:
                rutas = rutas + os.path.abspath(new) + "\n"
            else:
                rutas = rutas + os.path.abspath(new)

        # Cargando archivos 3...
        aviso([dic.avis_Publicar[16], ColorAviso.ok])
        elemento.send_keys(rutas)
        time.sleep(2)
        # Archivos cargados
        aviso([dic.avis_Publicar[17], ColorAviso.correcto])

    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    # SS Escribir cuerpo
    time.sleep(1)
    if cancelar():
        return dic.avis_Cancelar  # Cancelar--------------------

    # Buscando input de publicación 2...
    aviso([dic.avis_Publicar[18], ColorAviso.ok])
    try:
        elemento = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@aria-label,'{dicWeb.input_PublicDia}')]/div/div/div",
                )
            )
        )
    except TimeoutException:
        # No se encontró input de publicación 2
        return dic.avis_Publicar[19]

    elemento.click()
    # Escribiendo...
    aviso([dic.avis_Publicar[20], ColorAviso.ok])
    Teclear(ele=elemento, texto=post, can=cancelar,  config=config)

    if cancelar():
        return dic.avis_Cancelar  # Cancelar--------------------

    # TT Escribir link
    if link != "":
        time.sleep(1)
        # Pegando link:
        aviso([dic.avis_Publicar[21] + link, ColorAviso.ok])
        Teclear(ele=elemento, texto="\n", can=cancelar,config=config)
        elemento.send_keys(link)

    time.sleep(1)
    # TT Subir imagen

    SimularEspera()
    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    # TT Publicar
    # buscar boton publicar
    # Buscando botón publicar
    aviso([dic.avis_Publicar[22], ColorAviso.ok])
    try:
        elemento = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[@aria-label = '{dicWeb.bt_Publicar}']")
            )
        )
    except TimeoutException:
        # No se encontró botón de publicación
        return dic.avis_Publicar[23]
    elemento.click()

    time.sleep(1)
    if cancelar():
        # Proceso Cancelado
        return dic.avis_Cancelar  # Cancelar--------------------

    # TT Comprobar si se paso de tiempo

    # buscar advertencia
    try:
        elemento = comprobar.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{dicWeb.msg_LimitarPost}')]",
                )
            )
        )
    # no se encuentra advertencia
    except TimeoutException:
        return "-OK-"

    # no se pudo publicar
    # Publicación limitada
    return "FIN-" + dic.avis_Publicar[24]
