import time
import flet as ft

# TT archivos
from ui.login.vmLogin import VmLogin
from data.enums import ColorAviso
from data.singeltons import Info
from data.gestroDatos import CargarConfig, GuardarConfig
from data.diccionario.dicLogin_ui import Login as Dic


# SS IniciarF
def ejecutar(page: ft.Page, cambio: str):

    config = CargarConfig()
    dic = Dic(config.lenguaje)

    # TT funciones infladas
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

    def LoginLogrado(e: bool):
        if e:
            btContinuar.visible = True
        page.update()

    vm = VmLogin(aviso=Aviso, logLogrado=LoginLogrado)  # SS Crear vm

    # TT Funciones
    # comprobar ui
    def ComprobarUI():

        checkCuenta.value = vm.usarCookies
        if vm.webAbierta == False:
            txWebAbierta.value = ""
            btIniciar.text = dic.btIniciar
            btIniciar.bgcolor = ft.colors.BLUE
            if tfCorreo.value != "" and tdClave.value != "" or checkCuenta.value:
                btIniciar.disabled = False
            else:
                btIniciar.disabled = True
        else:
            txWebAbierta.value = dic.webAbierta
            btIniciar.disabled = False
            btIniciar.text = dic.btDetener
            btIniciar.bgcolor = ft.colors.RED
        page.update()

    # sesion iniciada
    def EstadoIniciar(e):
        vm.ActualizarIniciado(e.control.value)
        tfCorreo.read_only = e.control.value
        tdClave.read_only = e.control.value
        ComprobarUI()
        page.update()

    # actualizar correo
    def ActualizarCorreo(e):
        vm.ActualizarCorreo(e.control.value)
        ComprobarUI()
        page.update()

    # actualizar clave
    def ActualizarClave(e):
        vm.ActualizarClave(e.control.value)
        ComprobarUI()
        page.update()

    # iniciar web
    def IniciarNavegador(e):
        btIniciar.disabled = True
        prProgreso.visible = True
        page.update()
        if vm.webAbierta == False:
            btIniciar.disabled = True
            vm.IniciarWeb()
            ComprobarUI()
        else:
            vm.DetenerWeb()
            ComprobarUI()
            aviso.value = ""
        prProgreso.visible = False
        page.update()

    def IniciarManual(e):
        btIniciar.disabled = True
        prProgreso.visible = True
        page.update()
        vm.InicioManual()
        time.sleep(1)
        prProgreso.visible = False
        page.update()
        ComprobarUI()

    def Continuar():
        cookies = True
        if vm.usarCookies:
            cookies = vm.GuardarCookies()
        if cookies:
            cambio("/listgrupos")

    # TT Controles
    # Check cuenta
    checkCuenta = ft.Checkbox(
        label=dic.CheckUsarCookies,
        value=vm.usarCookies,
        on_change=EstadoIniciar,
        tooltip=dic.CheckUsarCookies_Tool,
    )
    # Borrar cokies
    btBorrarCookies = ft.IconButton(
        icon=ft.icons.COOKIE,
        on_click=lambda _: vm.BorrarCookies(),
        tooltip=dic.btBorrarCookies_Tool,
    )
    # campo correo
    tfCorreo = ft.TextField(
        label=dic.labelTexFielCorreo,
        value=vm.correo,
        text_align=ft.TextAlign.LEFT,
        width=350,
        on_change=ActualizarCorreo,
    )
    # campo contraseña
    tdClave = ft.TextField(
        label=dic.labelTexFielClave,
        value=vm.clave,
        text_align=ft.TextAlign.LEFT,
        width=350,
        password=True,
        can_reveal_password=True,
        on_change=ActualizarClave,
    )
    # Boton Inicio
    btIniciar = ft.CupertinoButton(
        text=dic.btIniciar,
        color=ft.cupertino_colors.WHITE,
        bgcolor=ft.colors.BLUE,
        on_click=IniciarNavegador,
        width=120,
        height=48,
        alignment=ft.alignment.center,
        padding=10,
    )

    # Boton Inicio manual
    btManual = ft.IconButton(
        icon=ft.icons.PSYCHOLOGY_ALT_OUTLINED,
        tooltip=dic.btIniciarManual_Tool,
        icon_color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE,
        highlight_color=ft.colors.GREY_900,
        on_click=IniciarManual,
    )

    # indicar de wed
    txWebAbierta = ft.Text(
        value=dic.webAbierta,
        size=10,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_300,
    )

    # iniciar omprobacion inicial
    aviso = ft.Text(
        value="",
        size=14,
        weight=ft.FontWeight.BOLD,
        visible=True,
        width=350,
        text_align=ft.TextAlign.CENTER,
        max_lines=1,
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
                value=dic.titVantanaProgreso,
                size=12,
                color=ft.colors.BLUE,
                text_align=ft.TextAlign.CENTER,
            )
        ],
    )

    # indicador Progeso
    prProgreso = ft.ProgressBar(
        width=200, color=ft.colors.BLUE, bgcolor=ft.colors.WHITE, visible=False
    )

    # Continuar Grupos
    btContinuar = ft.ElevatedButton(
        text=dic.btContinuar,
        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
        visible=False,
        height=40,
        width=200,
        on_click=lambda _: Continuar(),
        elevation=8,
        icon_color=ft.colors.BLUE,
    )
    # SS Inicializar
    vm.ComprobarCokkies()
    ComprobarUI()

    # TT Cuerpo
    page.views.append(
        ft.View(
            route="/principal",
            controls=[
                # Cuerpo
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    width=350,
                    height=600,
                    expand=1,
                    controls=[
                        # TT cabeza
                        # Titulo
                        ft.Text(
                            value=Info.nombre,
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE,
                        ),
                        # version
                        ft.Text(value=Info.version, size=10),
                        # Facebook
                        ft.Text(value=dic.titIniciarSesion, size=16),
                        # Correo
                        tfCorreo,
                        # TT formulario
                        # Contraseña
                        tdClave,
                        # Cuenta iniciada ?
                        ft.Row(
                            spacing=20,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[checkCuenta, btBorrarCookies],
                        ),
                        # bt Iniciar secion
                        ft.Row(
                            spacing=20,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[btManual, btIniciar, ft.VerticalDivider()],
                        ),
                        # indicador web
                        txWebAbierta,
                        # ventana
                        ft.Container(
                            width=350,
                            height=120,
                            bgcolor=ft.colors.GREY_800,
                            border_radius=ft.border_radius.all(10),
                            padding=5,
                            content=(ventana),
                        ),
                        # indicador de progreso
                        prProgreso,
                        # Aviso
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
    page.update()
