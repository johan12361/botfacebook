import flet as ft
import time

# TT archivos
from ui.ventanaConfig import VentanaConfig
from data.gestroDatos import CargarConfig, GuardarConfig
from data.singeltons import Info
from data.diccionario.dicConfig_ui import Config as Dic


# SS IniciarF
def ejecutar(page: ft.Page, cambio: str):

    config = CargarConfig()
    dic = Dic(config.lenguaje)
    vConfig = VentanaConfig(page=page, cof=config, tView="config")

    # TT Funciones
    # tiempo de bloqueo
    def Desbloquear():
        btContinuar.disabled = True
        btContinuar.visible = False
        btConfig.disabled = True
        selecIdioma.disabled = True
        selecIdiomaFacebook.disabled = True

        segundo = config.tiempobloqueo
        for i in range(segundo):
            tempo.value = f"{dic.msjEspera} {segundo - i}"
            page.update()
            time.sleep(1)

        tempo.value = ""
        btContinuar.disabled = False
        btContinuar.visible = True
        btConfig.disabled = False
        selecIdioma.disabled = False
        selecIdiomaFacebook.disabled = False
        page.update()

    # Cambiar lenguaje
    def CambiarIdioma(e):
        # Selecionar lenguaje
        if e.control.key != config.lenguaje:
            if e.control.key == "ES":
                config.lenguaje = "ES"
            elif e.control.key == "EN":
                config.lenguaje = "EN"
            # Guardar
            GuardarConfig(config)
            selecIdioma.controls[2].value = dic.msgCambioLeng
            btContinuar.disabled = True
        RevisarIdioma()
        page.update()

    # Cambiar lenguaje Facebook
    def CambiarIdiomaFacebook(e):
        if e.control.key != config.facebookLeng:
            # Selecionar lenguaje
            if e.control.key == "ES":
                config.facebookLeng = "ES"
            elif e.control.key == "EN":
                config.facebookLeng = "EN"
            # Guardar
            GuardarConfig(config)
            # Cambiar ui
        RevisarIdioma()
        page.update()

    def RevisarIdioma():
        for i in selecIdioma.controls[1].controls:
            if i.key != config.lenguaje:
                i.elevation = 7
                i.bgcolor = ft.colors.BLUE_GREY_900
                i.color = ft.colors.WHITE
            else:
                i.elevation = 0
                i.bgcolor = ft.colors.GREEN
                i.color = ft.colors.WHITE
        for i in selecIdiomaFacebook.controls[1].controls:
            if i.key != config.facebookLeng:
                i.elevation = 7
                i.bgcolor = ft.colors.BLUE_GREY_900
                i.color = ft.colors.WHITE
            else:
                i.elevation = 0
                i.bgcolor = ft.colors.GREEN
                i.color = ft.colors.WHITE
        page.update()

    # TT Controles

    # Tiempo
    tempo = ft.Text(
        value="", size=16, color=ft.colors.GREEN, text_align=ft.TextAlign.CENTER
    )

    # SS Informacion
    info = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.END,
        width=350,
        spacing=8,
        controls=[
            ft.Text(
                value=Info.nombre,
                size=24,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE,
            ),
            ft.Text(value=dic.autor, size=12, text_align=ft.TextAlign.CENTER),
            # icono
            ft.TextButton(
                text=dic.btInfo,
                icon=ft.icons.INFO_OUTLINE_ROUNDED,
                tooltip="https://multipostfb.site",
                on_click=lambda _: ft.Page.launch_url(
                    self=page, url="https://multipostfb.site"
                ),
            ),
            ft.Text(
                value=dic.msjDonacion,
                size=12,
                width=350,
                text_align=ft.TextAlign.CENTER,
                color=ft.colors.AMBER,
            ),
            ft.VerticalDivider(),
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
        ],
    )

    ##selecionar idioma
    selecIdioma = ft.Column(
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=350,
        controls=[
            ft.Text(value=dic.titIdioma, size=14),
            ft.Row(
                width=350,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.ElevatedButton(
                        text="ES",
                        key="ES",
                        on_click=CambiarIdioma,
                        bgcolor=ft.colors.BLUE_GREY_900,
                        width=80,
                        color=ft.colors.WHITE,
                    ),
                    ft.ElevatedButton(
                        text="EN",
                        key="EN",
                        on_click=CambiarIdioma,
                        bgcolor=ft.colors.BLUE_GREY_900,
                        width=80,
                        color=ft.colors.WHITE,
                    ),
                ],
            ),
            ft.Text(size=12, color=ft.colors.BLUE),
        ],
    )

    selecIdiomaFacebook = ft.Column(
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=350,
        controls=[
            ft.Text(value=dic.titIdiomaFacebook, size=14),
            ft.Row(
                width=350,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.ElevatedButton(
                        text="ES",
                        key="ES",
                        on_click=CambiarIdiomaFacebook,
                        bgcolor=ft.colors.BLUE_GREY_900,
                        width=100,
                        color=ft.colors.WHITE,
                    ),
                    ft.ElevatedButton(
                        text="EN (US)",
                        key="EN",
                        on_click=CambiarIdiomaFacebook,
                        bgcolor=ft.colors.BLUE_GREY_900,
                        width=100,
                        color=ft.colors.WHITE,
                    ),
                ],
            ),
        ],
    )
    btConfig = ft.IconButton(
        icon=ft.icons.SETTINGS, on_click=lambda _: vConfig.activar()
    )

    # Boton continuar
    btContinuar = ft.ElevatedButton(
        text=dic.btContinuar,
        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
        height=40,
        width=200,
        on_click=lambda _: cambio("/login"),
        elevation=8,
        icon_color=ft.colors.BLUE,
    )

    # SS Inicializar
    RevisarIdioma()
    page.overlay.extend([vConfig.pick_files_dialog])

    # SS Cuerpo
    page.views.append(
        ft.View(
            route="/config",
            controls=[
                # TT Cuerpo
                ft.Column(
                    expand=1,
                    spacing=12,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        info,
                        ft.VerticalDivider(),
                        btConfig,
                        ft.VerticalDivider(),
                        selecIdioma,
                        selecIdiomaFacebook,
                    ],
                ),
                tempo,
                btContinuar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START,
        )
    )
    Desbloquear()
