import flet as ft
import time
import sys
# TT archivos
from data.singeltons import Info
from data.singeltons import Driver as DD
from data.gestroDatos import CargarConfig
from data.diccionario.dicConfig_ui import VentanaSalir as Dic


def WinEvents(page: ft.Page):
   
    config = CargarConfig()
    print(config.lenguaje)
    dic = Dic(lenguaje=config.lenguaje)

    # TT Dialogo salir
    def CerrarApp(val: bool):
        # cerrar
        if val:
            page.disabled = True
            page.update()
            # cerrar web driver
            if DD.driver != None:
                try:
                    print("Cerrando navegador")
                    DD.driver.quit()
                except:
                    pass
            print("Cerrando...")
            page.window_destroy()
            sys.exit()
        # cancelar
        else:
            diaCerrar.open = False
            page.update()


    # SS Contoles
    diaCerrar = ft.AlertDialog(
        modal=True,
        title=ft.Text(dic.titConfirmar),
        actions_padding=20,
        title_padding=20,
        content_padding=10,
        content=ft.Column(
            spacing=20,
            width=300,
            height=200,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value=dic.msjDonacion,
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.AMBER,
                ),
                # Donar
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            text="PATREON",
                            bgcolor="#f76754",
                            icon_color=ft.colors.BLUE,
                            color=ft.colors.WHITE,
                            elevation=10,
                            width=120,
                            on_click=lambda _: ft.Page.launch_url(
                                self=page, url="https://www.patreon.com/MultiPostFB"
                            ),
                        ),
                        ft.ElevatedButton(
                            text="PAYPAL",
                            bgcolor="#d08900",
                            icon_color=ft.colors.BLUE,
                            color=ft.colors.WHITE,
                            elevation=10,
                            width=120,
                            on_click=lambda _: ft.Page.launch_url(
                                self=page,
                                url="https://www.paypal.com/donate/?hosted_button_id=7WSA9TWLBC66U",
                            ),
                        ),
                    ],
                ),
                ft.Text(
                    value=dic.msjConfirmacion,
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
        actions=[
            ft.ElevatedButton(
                on_click=lambda _: CerrarApp(True), disabled=True, bgcolor=ft.colors.RED
            ),
            ft.ElevatedButton(dic.btNO, on_click=lambda _: CerrarApp(False)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # SS Eventos
    def Events(e):
        # TT Cerrar
        if e.data == "close":
            page.dialog = diaCerrar
            diaCerrar.open = True
            diaCerrar.actions[0].disabled = True
            page.update()
            for i in range(5):
                if page.dialog.open == False:
                    break
                diaCerrar.actions[0].text = dic.btSI + " (" + str(5 - i) + ")"
                page.update()
                time.sleep(1)
            diaCerrar.actions[0].text = dic.btSI 
            diaCerrar.actions[0].disabled = False
            page.update()

    # SS Confi ventana
    page.title = Info.nombre + " - " + Info.version
    page.window_height = 720
    page.window_width = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_always_on_top = True
    page.theme_mode = ft.ThemeMode.DARK
    page.window_prevent_close = True
    page.on_window_event = Events
