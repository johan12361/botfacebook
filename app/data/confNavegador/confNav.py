from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# TT archivos
from data.gestroDatos import CargarConfig


# .\env\Scripts\activate


# Configuracion base--
def confBase(op: Options):

    # Configuracion avanzada
    config = CargarConfig()

    if config.navOculto:
        op.add_argument("--headless=new")

    op.add_argument("--disable-web-security")
    op.add_argument("--disable-extensions")
    op.add_argument("--disable-notifications")
    op.add_argument("--ignore-certificate-errors")
    op.add_argument("--no-sanbox")
    op.add_argument("--log-level=3")
    op.add_argument("--allow-running-insecure-content")
    op.add_argument("--no-default-browser-check")
    op.add_argument("--no-first-run")
    op.add_argument("--no-proxy-server")
    op.add_argument("--disable-blink-features=AutomationControlled")

    # parametros de inicio
    exp_op = ["enable-automation", "ignore-certificate-errors", "enable-logging"]
    op.add_experimental_option("excludeSwitches", exp_op)

    # preferencias de inicio
    pref = {
        "profile.default_content_setting_values.notifications": 2,
        "intl.accept_languajes": ["es-ES", "es"],
        "credentials_enable_service": False,
    }
    op.add_experimental_option("prefs", pref)
