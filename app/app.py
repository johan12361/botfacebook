import flet as ft
import os

# TT archivos
from ui.windowEvents import WinEvents
from ui.config import config
from ui.login import login
from ui.listGrupos import listGrupos
from ui.publicacion import publicacion

# oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\jandedobbeleer.omp.json" | Invoke-Expression
# .\env\Scripts\activate
# flet pack .\app\app.py --icon .\Res\ico.ico --product-name "Multi Post FB" --product-version "1.2.1" --copyright "MultiPostFB.site 2024"

os.system("cls")


# TT Navegacion
def main(page: ft.Page):

    # SS configuracion de eventos de
    WinEvents(page)

    def CambioView(routa):
        page.views.clear()

        # SS pagina Login
        if routa == "/login":
            login.ejecutar(page, CambioView)
            page.update()

        # SS Config
        elif routa == "/config":
            config.ejecutar(page, CambioView)
            page.update()

        # SS pagina lista Grupos
        elif routa == "/listgrupos":
            listGrupos.ejecutar(page, CambioView)
            page.update()

        # SS pagina publicacion
        elif routa == "/publicacion":
            publicacion.ejecutar(page, CambioView)
            page.update()

        # SS Bienvenida - Config
        else:
            config.ejecutar(page, CambioView)
            page.update()

    def ViewPop(e=ft.ViewPopEvent):
        page.views.pop()
        toView: ft.View = page.views[-1]
        page.go(toView.route)

    page.on_route_change = CambioView
    page.on_view_pop = ViewPop
    page.go(page.route)

# TT Ejecutar main
ft.app(target=main)
