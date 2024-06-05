import flet as ft
import time

# TT archivos
from data.gestroDatos import CargarConfig
from data.diccionario.dicListaGrupos_ui import ListaGrupos as Dic
from ui.listGrupos.vmListGrupo import VmListGrupo
from data.enums import ColorAviso


# SS IniciarF
def ejecutar(page: ft.Page, cambio: str):

    config = CargarConfig()
    dic = Dic(config.lenguaje)

    def Aviso(mensaje: list[str, ColorAviso]):
        # Colores
        if mensaje[1] == ColorAviso.ok:
            aviso.color = ft.colors.GREY
        elif mensaje[1] == ColorAviso.error:
            aviso.color = ft.colors.RED
        elif mensaje[1] == ColorAviso.precaucion:
            aviso.color = ft.colors.ORANGE
        elif mensaje[1] == ColorAviso.correcto:
            aviso.color = ft.colors.GREEN

        # depurar
        depurado = ""
        if "xxx" in mensaje[0]:
            depurado = mensaje[0].replace("xxx", "")
        else:
            depurado = mensaje[0]
            ventana.controls.append(ft.Text(value=depurado, size=10, color=aviso.color))
        # Mensaje
        aviso.value = depurado
        page.update()

    vm = VmListGrupo(aviso=Aviso)

    # TT Funciones

    def Guardar():
        btContinuar.disabled = True
        btRecaudar.disabled = True
        btGuardar.disabled = True
        page.update()
        vm.GuardarGrupos(lista.value)
        time.sleep(1)
        btContinuar.disabled = False
        btRecaudar.disabled = False
        btGuardar.disabled = False
        page.update()

    def RecaudarDatos():
        btContinuar.disabled = True
        btGuardar.disabled = True
        btRecaudar.visible = False
        btcancelar.visible = True
        page.update()
        vm.RecaudarDatosGrupos()
        btRecaudar.visible = True
        btcancelar.visible = False
        btContinuar.disabled = False
        btGuardar.disabled = False
        page.update()

    def Continuar():
        Guardar()
        cambio("/publicacion")

    # TT Controles

    lista = ft.TextField(
        width=350, multiline=True, value=vm.grupos, text_size=10, expand=1
    )

    btGuardar = ft.CupertinoButton(
        text=dic.btGuardar,
        color=ft.cupertino_colors.WHITE,
        bgcolor=ft.colors.BLUE,
        width=240,
        on_click=lambda _: Guardar(),
    )

    btRecaudar = ft.TextButton(
        text=dic.btObtenerDatos,
        icon=ft.icons.SYNC,
        on_click=lambda _: RecaudarDatos(),
        icon_color=ft.colors.BLUE,
    )
    btcancelar = ft.TextButton(
        text=dic.btCancelar,
        icon=ft.icons.STOP_CIRCLE,
        visible=False,
        on_click=lambda _: vm.CancelarRecaudo(),
        icon_color=ft.colors.RED,
    )

    # ventana proceso
    ventana = ft.ListView(
        width=350,
        height=120,
        spacing=3,
        auto_scroll=True,
        expand=1,
        controls=[
            ft.Text(
                value=dic.titVentanaProgreso,
                size=12,
                color=ft.colors.BLUE,
                text_align=ft.TextAlign.CENTER,
            )
        ],
    )

    aviso = ft.Text(
        value="",
        size=14,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.GREEN,
        visible=True,
        width=350,
        text_align=ft.TextAlign.CENTER,
        max_lines=1,
    )

    # Continuar a Grupos
    btContinuar = ft.ElevatedButton(
        text=dic.btContinuar,
        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
        height=40,
        width=200,
        on_click=lambda _: Continuar(),
        elevation=8,
        icon_color=ft.colors.BLUE,
    )

    # SS Cuerpo
    page.views.append(
        ft.View(
            route="/listgrupos",
            controls=[
                # TT Cuerpo
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    width=350,
                    height=600,
                    expand=1,
                    controls=[
                        ft.Text(
                            value=dic.titulo,
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        lista,
                        # ventana
                        ft.Container(
                            width=350,
                            height=120,
                            bgcolor=ft.colors.GREY_800,
                            border_radius=ft.border_radius.all(10),
                            padding=5,
                            content=(ventana),
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[btRecaudar, btcancelar],
                        ),
                        btGuardar,
                        aviso,
                    ],
                ),
                btContinuar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START,
            bgcolor=page.bgcolor,
        )
    )
