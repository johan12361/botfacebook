import os
import shutil
import pickle
import re
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# TT archivos
from data.singeltons import IdGrupo, Config, Post


def __RevisarCarpetas():
    if not os.path.exists(".\Res"):
        os.mkdir(".\Res")
    if not os.path.exists(".\Res\grupos"):
        os.mkdir(".\Res\grupos")
    if not os.path.exists(".\Res\cookies"):
        os.mkdir(".\Res\cookies")
    if not os.path.exists(".\Res\post"):
        os.mkdir(".\Res\post")


def GuardarConfig(config: Config):
    with open(".\Res\config.cfg", "wb") as data:
        pickle.dump(config, data)


def CargarConfig():
    __RevisarCarpetas()
    if os.path.isfile(".\Res\config.cfg"):
        with open(".\Res\config.cfg", "rb") as data:
            return pickle.load(data)
    else:
        return Config()


# Driver interno
def CargarDriverInterno(ruta: str):
    DriverCacheManager.find_driver
    return ChromeService(
        ChromeDriverManager(cache_manager=DriverCacheManager(ruta)).install()
    )


# TT Grupos Facebbook
def GuardarGrupo(grupo: IdGrupo):
    patron = re.compile("[\W]+")
    nombre = patron.sub("", grupo.url).replace("httpswwwfacebookcom", "")
    ruta = ".\Res\grupos\g" + nombre + ".goup"

    with open(ruta, "wb") as archivo:
        pickle.dump(grupo, archivo)


def CargarGrupo(url: str):
    patron = re.compile("[\W]+")
    nombre = patron.sub("", url).replace("httpswwwfacebookcom", "")
    ruta = ".\Res\grupos\g" + nombre + ".goup"

    if os.path.isfile(ruta):
        with open(ruta, "rb") as archivo:
            return pickle.load(archivo)

    else:
        blank = IdGrupo()
        blank.url = url
        blank.nombre = nombre
        return blank


# TT gertionar post
# Guardar
def GuardarPost(post: Post, media: bool):
    # verificar carpeta
    if not os.path.exists(".\Res\post"):
        os.mkdir(".\Res\post")
    # Guardar media
    if media == True and post.media != [] and post.media != None:
        rutamedia = ".\Res\post" + "\\" + "p-" + post.nombre + " media"
        # crear carpeta media
        if not os.path.exists(rutamedia):
            os.mkdir(rutamedia)
        # copiar media
        for i in range(len(post.media)):
            nombre = os.path.split(post.media[i])[-1]
            # Revisar si existe media anterior
            if not os.path.isfile(rutamedia + "\\" + nombre):
                shutil.copy(post.media[i], rutamedia + "\\" + nombre)
                post.media[i] = rutamedia + "\\" + nombre

    # Guardar .post
    with open(".\Res\post" + "\\" + "p-" + post.nombre + ".post", "wb") as archivo:
        pickle.dump(post, archivo)


def CargarPostGuardados() -> list[Post]:
    # verificar carpeta
    ruta = ".\Res\post"
    if not os.path.exists(ruta):
        os.mkdir(ruta)
    post: list[Post] = []
    contenido = os.listdir(ruta)
    if contenido != [] and contenido != None:
        for fichero in contenido:
            if os.path.isfile(ruta + "\\" + fichero) and fichero.endswith(".post"):
                with open(ruta + "\\" + fichero, "rb") as file:
                    fort = pickle.load(file)
                    post.append(fort)
    return post
