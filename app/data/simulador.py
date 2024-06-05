import time
import random

# TT archivos
from data.singeltons import Config


def SimularEspera():
    ran = random.randint(30, 50) / 10
    time.sleep(ran)


def CompprobarUrl(url: str, buscar: list[str], pocetaje: float):
    conci = 0
    for i in buscar:
        if i in url:
            conci += 1
    total = conci / len(buscar)
    if total >= pocetaje:
        return True
    else:
        return False


def Teclear(ele, texto, can, config: Config):

    # Simular escribir
    if config.simularEscritura:
        for i in texto:
            time.sleep(random.uniform(0, 0.02))
            ele.send_keys(i)
            if can():
                break
    # Enviar texto completo
    else:
        ele.send_keys(texto)
