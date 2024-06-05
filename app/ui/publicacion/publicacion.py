import flet as ft
import time
import copy

# TT archivos
from ui.publicacion.vmPublicacion import VmPublicacion
from data.enums import ColorAviso
from data.gestroDatos import CargarConfig
from data.diccionario.dicPublicacion_ui import Publicacion as Dic


# SS IniciarF
def ejecutar(page: ft.Page, cambio: str):

    config = CargarConfig()
    dic = Dic(config.lenguaje)

    def ReintentarPost(blok: list[bool, str]):
        if blok[0] == False:
            CuerpoPost.controls[0].controls[0].disabled = False
            CuerpoPost.controls[0].controls[0].content.controls[0].name = ft.icons.SYNC
            CuerpoPost.controls[0].controls[0].content.controls[1].value = blok[1]
            page.update()

        elif blok[0] and blok[1] == "":
            CuerpoPost.controls[0].controls[0].disabled = True
            CuerpoPost.controls[0].controls[0].content.controls[0].name = None
            CuerpoPost.controls[0].controls[0].content.controls[1].value = ""
            # Guardar post
            GuardarPost()
            # desactivar ui
            CuerpoPost.visible = False
            CuerpoProceso.visible = True
            btPost.disabled = True
            prProgreso.visible = True
            page.update()
            time.sleep(1)
            btPost.visible = False
            # Activar cancelar
            btCancelarPost.disabled = False
            btCancelarPost.visible = True
            page.update()
        elif blok[0] and blok[1] != "":
            # Activar cancelar
            btCancelarPost.disabled = True
            btCancelarPost.visible = False
            # fin de publicacion
            btPost.disabled = False
            btPost.visible = True
            CuerpoPost.visible = True
            CuerpoProceso.visible = False
            prProgreso.visible = False
            page.update()

    # TT Funciones infladas
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
        if "ACT-" in mensaje[0]:
            ActualizarGrupos()
            time.sleep(2)
            blokGrupos.content.scroll_to(key="XXX", duration=1000)

        elif "xxx" in mensaje[0]:
            depurado = mensaje[0].replace("xxx", "")
            aviso.value = depurado
        else:
            depurado = mensaje[0]
            ventanaPoceso.content.controls.append(
                ft.Text(value=depurado, size=10, color=aviso.color)
            )
            aviso.value = depurado

        page.update()

    vm = VmPublicacion(aviso=Aviso, reintentar=ReintentarPost)  # SS Crear VM

    # TT Dialogo grupos

    def AbrirDialogoGrupos():
        page.dialog = dialogoGrupos
        dialogoGrupos.open = True
        page.update()
        ActualizarGrupos()
        page.update()

    def GuardarDiaGrupos():
        for i in range(len(vm.idGrupos)):
            vm.idGrupos[i].selec = (
                blokGrupos.content.controls[i].content.controls[2].value
            )
        dialogoGrupos.open = False
        page.update()

    def SincroGrupos():
        vm.SincroGrupos()
        ActualizarGrupos()
        page.update()

    # Card Grupos
    cardGrupo = ft.Container(
        height=60,
        expand=1,
        border_radius=8,
        padding=6,
        # 0
        content=ft.Row(
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                # 00
                ft.Image(
                    width=44,
                    height=44,
                    src="https://www.facebook.com/favicon.ico",
                    fit=ft.ImageFit.COVER,
                    border_radius=ft.border_radius.all(24),
                ),
                # 01
                ft.Column(
                    expand=1,
                    spacing=1,
                    controls=[
                        # 010
                        ft.Text(
                            value="Nombre de grupo",
                            color=ft.colors.BLUE_500,
                            size=14,
                            width=500,
                            max_lines=1,
                        ),
                        # 011
                        ft.Text(
                            value="Miembros",
                            size=10,
                            width=500,
                            max_lines=1,
                        ),
                        # 012
                        ft.Text(
                            value="estado",
                            size=10,
                            width=500,
                            max_lines=1,
                            text_align=ft.TextAlign.END,
                        ),
                    ],
                ),
                # 02
                ft.Checkbox(),
            ],
        ),
    )

    # Grupo Dialogos
    blokGrupos = ft.Container(
        width=350,
        height=375,
        bgcolor="#262626",
        border_radius=ft.border_radius.all(8),
        content=ft.ListView(expand=1, spacing=12, padding=10, auto_scroll=False),
    )

    # Dialogo Grupos
    dialogoGrupos = ft.AlertDialog(
        modal=True,
        content=blokGrupos,
        open=False,
        content_padding=0,
        actions_padding=5,
        shape=ft.RoundedRectangleBorder(radius=8),
        title_padding=5,
        actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        alignment=ft.alignment.center,
        title=ft.Text(
            size=16,
            text_align=ft.TextAlign.CENTER,
        ),
        actions=[
            ft.TextButton(
                text=dic.dia_brGuardar,
                on_click=lambda _: GuardarDiaGrupos(),
                icon=ft.icons.SAVE,
            ),
            ft.IconButton(
                icon=ft.icons.SYNC,
                on_click=lambda _: SincroGrupos(),
                tooltip=dic.dia_btSincGrup_Tool,
            ),
        ],
    )

    def ContarGrupos():
        contar = 0
        for i in vm.idGrupos:
            if i.selec:
                contar = contar + 1
        btSelecGrupos.text = str(contar) + "/" + str(len(vm.idGrupos))
        page.update()

    def ActualizarGrupos():
        blokGrupos.content.controls = None
        page.update()
        contar = 0
        publicados = 0
        for i in range(len(vm.idGrupos)):
            car = copy.deepcopy(cardGrupo)
            # imagen
            car.content.controls[0].src = vm.idGrupos[i].img
            # nombre
            car.content.controls[1].controls[0].value = vm.idGrupos[i].nombre
            car.content.controls[1].controls[0].tooltip = vm.idGrupos[i].nombre
            # miembros
            car.content.controls[1].controls[1].value = vm.idGrupos[i].miembros
            # selec
            car.content.controls[2].value = vm.idGrupos[i].selec
            # url tool
            car.tooltip = vm.idGrupos[i].url
            car.key = ""

            # Estado
            if vm.idGrupos[i].estado == "Publicando...":
                car.content.controls[1].controls[2].color = ft.colors.WHITE
                car.content.controls[1].controls[2].value = dic.dia_EstadoPublicando
                car.bgcolor = ft.colors.INDIGO_900
                car.key = "XXX"
            elif vm.idGrupos[i].estado == "publicado":
                car.content.controls[1].controls[2].color = ft.colors.GREEN
                car.content.controls[1].controls[2].value = dic.dia_EstadoPublicado
                car.bgcolor = ft.colors.GREEN_900
                publicados = publicados + 1
            elif vm.idGrupos[i].estado == "pendiente":
                car.content.controls[1].controls[2].color = ft.colors.ORANGE
                car.content.controls[1].controls[2].value = dic.dia_EstadoPendiente
                car.bgcolor = ft.colors.BROWN_800
            else:
                car.content.controls[1].controls[2].color = ft.colors.WHITE
                car.content.controls[1].controls[2].value = ""
                car.bgcolor = ft.colors.BLUE_GREY_900

            blokGrupos.content.controls.append(car)
            # contar
            if vm.idGrupos[i].selec:
                contar = contar + 1
        CuerpoProceso.controls[0].value = (
            dic.dia_GrupTitulo + str(publicados) + " " + dic.pal_Grupo
        )
        dialogoGrupos.title.value = (
            dic.dia_GrupTitulo + str(publicados) + " " + dic.pal_Grupo
        )
        btSelecGrupos.text = str(contar) + "/" + str(len(vm.idGrupos))
        page.update()

    # SS Funciones
    def Publicar():

        vm.loppActivo = False
        # Guardar post
        GuardarPost()
        # desactivar ui
        CuerpoPost.visible = False
        CuerpoProceso.visible = True
        btPost.disabled = True
        prProgreso.visible = True
        page.update()
        time.sleep(1)
        btPost.visible = False
        # Activar cancelar
        btCancelarPost.disabled = False
        btCancelarPost.visible = True
        # publicar
        postcompleto = vm.Publicar()
        # Activar cancelar
        btCancelarPost.disabled = True
        btCancelarPost.visible = False
        # fin de publicacion
        btPost.disabled = False
        btPost.visible = True
        CuerpoPost.visible = True
        CuerpoProceso.visible = False
        prProgreso.visible = False
        page.update()
        if postcompleto == False:
            vm.loppActivo = True
            vm.corrReintentar.run(vm.BucleIntento())

    # cancelar publicacion
    def CancelarProceso():
        btCancelarPost.disabled = True
        vm.cancelarPorceso = True
        page.update()

    # cancelar reintentos
    def CancelarReeintentoAuto():
        vm.loppActivo = False
        CuerpoPost.controls[0].controls[0].content.controls[0].name = None
        CuerpoPost.controls[0].controls[0].content.controls[1].value = ""
        CuerpoPost.controls[0].controls[0].disabled = True
        page.update()

    # guardar post
    def GuardarPost():
        vm.nombrePost = gesPost.controls[0].value
        vm.post = post.value
        vm.link = link.value
        vm.GuardarPost()
        page.update()

    # Cargar post
    def CargarPost(e):
        diaCargarpost.open = False
        val = e.control.key
        vm.CargarPost(val)
        post.value = vm.post
        link.value = vm.link
        gesPost.controls[0].value = vm.nombrePost
        page.update()
        ContarGrupos()
        ActualizarMedia()
        page.update()

    def ActualizarMedia():
        carrucel.content.controls = None
        page.update()
        if vm.imgs != [] and vm.imgs != None:
            for i in vm.imgs:
                carrucel.content.controls.append(
                    ft.Image(
                        src=i,
                        width=60,
                        height=60,
                        border_radius=ft.border_radius.all(16),
                        tooltip=i,
                    )
                )
        page.update()

    # Dialogo Driver
    def SelecMedia(e: ft.FilePickerResultEvent):
        if e.files:
            vm.imgs = []
            carrucel.content.controls = []
            for i in e.files:
                vm.imgs.append(i.path)
                carrucel.content.controls.append(
                    ft.Image(
                        src=i.path,
                        width=60,
                        height=60,
                        border_radius=ft.border_radius.all(16),
                        tooltip=i.path,
                    )
                )
        page.update()

    # eliminar imagenes
    def EliImgs():
        vm.imgs = None
        carrucel.content.controls = None
        page.update()

    # SS Controles
    # Selecinar grupos
    btSelecGrupos = ft.ElevatedButton(
        icon=ft.icons.GROUP,
        on_click=lambda _: AbrirDialogoGrupos(),
        icon_color=ft.colors.BLUE,
    )

    # TT dialogo Posts
    cardPost = ft.Container(
        height=44,
        expand=1,
        bgcolor=ft.colors.BLUE_GREY_800,
        border_radius=8,
        padding=4,
        on_click=CargarPost,
        content=ft.Row(
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(value="    Post N1", size=14),
            ],
        ),
    )

    def CerrarDiaPost():
        diaCargarpost.open = False
        page.update()

    # Dialogo
    diaCargarpost = ft.AlertDialog(
        modal=True,
        open=False,
        title=ft.Text(
            value=dic.dia_PostTitulo,
            size=18,
            text_align=ft.TextAlign.CENTER,
        ),
        content=ft.ListView(
            width=300,
            height=300,
            spacing=5,
        ),
        actions=[
            ft.TextButton(text=dic.dia_PostBtCerrar, on_click=lambda _: CerrarDiaPost())
        ],
    )

    def AbrirDiaPost():
        diaCargarpost.content.controls = None
        page.update()
        page.dialog = diaCargarpost
        diaCargarpost.open = True
        page.update()
        vm.PostGuardados()
        if vm.postGuardados != [] and vm.postGuardados != None:
            for i in range(len(vm.postGuardados)):
                post = copy.deepcopy(cardPost)
                post.key = i
                post.content.controls[0].value = "   " + vm.postGuardados[i].nombre
                diaCargarpost.content.controls.append(post)
        page.update()

    # gestion post
    gesPost = ft.Row(
        width=350,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            # nombre
            ft.TextField(
                width=150,
                height=32,
                value=vm.nombrePost,
                text_size=12,
                multiline=False,
                content_padding=5,
                input_filter=ft.InputFilter(
                    allow=False, regex_string=r"[^a-zA-Z0-9 ]", replacement_string=""
                ),
            ),
            # guardar
            ft.IconButton(
                icon=ft.icons.SAVE_OUTLINED,
                on_click=lambda _: GuardarPost(),
                icon_color=ft.colors.BLUE,
                icon_size=24,
                tooltip=dic.btGuardar_Tool,
            ),
            # cargar
            ft.IconButton(
                icon=ft.icons.FILE_OPEN_OUTLINED,
                on_click=lambda _: AbrirDiaPost(),
                icon_color=ft.colors.BLUE,
                icon_size=24,
                tooltip=dic.btCargar_Tool,
            ),
            btSelecGrupos,
        ],
    )

    # post
    post = ft.TextField(
        width=350,
        height=150,
        multiline=True,
        label=dic.labeCuerpoPots,
        value=vm.post,
        text_size=14,
        content_padding=10,
    )
    # Link
    link = ft.TextField(
        width=350,
        height=32,
        multiline=False,
        label=dic.labeLink,
        value=vm.post,
        text_size=12,
        content_padding=5,
    )
    # Boton publicar
    btPost = ft.CupertinoButton(
        text=dic.btPublicar,
        color=ft.cupertino_colors.WHITE,
        bgcolor=ft.colors.BLUE,
        width=160,
        on_click=lambda e: Publicar(),
        padding=0,
    )

    # Boton programar post
    btProgramarPost = ft.IconButton(icon=ft.icons.ACCESS_TIME_FILLED, width=40)

    # Boton cancelar
    btCancelarPost = ft.CupertinoButton(
        visible=False,
        text=dic.btCancelar,
        color=ft.cupertino_colors.WHITE,
        bgcolor=ft.colors.RED,
        width=160,
        on_click=lambda _: CancelarProceso(),
        padding=0,
    )

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
    ventanaPoceso = ft.Container(
        width=350,
        height=120,
        bgcolor=ft.colors.GREY_800,
        border_radius=ft.border_radius.all(10),
        padding=5,
        content=(
            ft.ListView(
                width=350,
                height=120,
                spacing=3,
                auto_scroll=True,
                expand=1,
                controls=[
                    ft.Text(
                        value=dic.titVentanaProceso,
                        size=12,
                        color=ft.colors.BLUE,
                        text_align=ft.TextAlign.CENTER,
                    )
                ],
            )
        ),
    )

    # indicador Progeso
    prProgreso = ft.ProgressBar(
        width=200, color=ft.colors.BLUE, bgcolor=ft.colors.WHITE, visible=False
    )

    blokSelecMedia = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            # Selec Media
            ft.ElevatedButton(
                dic.btCargarMedia,
                icon=ft.icons.IMAGE,
                on_click=lambda _: pick_files_dialog.pick_files(
                    allow_multiple=True, file_type=ft.FilePickerFileType.IMAGE
                ),
            ),
            # Eliminar Media
            ft.IconButton(
                icon=ft.icons.HIDE_IMAGE_OUTLINED,
                on_click=lambda e: EliImgs(),
                tooltip=dic.btBorrarMedia,
            ),
        ],
    )

    pick_files_dialog = ft.FilePicker(on_result=SelecMedia)

    carrucel = ft.Container(
        width=350,
        height=64,
        bgcolor=ft.colors.GREY_800,
        border_radius=ft.border_radius.all(10),
        padding=5,
        content=ft.ListView(spacing=3, expand=1, auto_scroll=True, horizontal=True),
    )

    # SS Cuerpos
    # Cuerpo post
    CuerpoPost = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
        width=350,
        height=420,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    # Tempo
                    ft.TextButton(
                        disabled=True,
                        width=100,
                        height=26,
                        icon_color=ft.colors.GREEN,
                        on_click=lambda _: CancelarReeintentoAuto(),
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[ft.Icon(size=18), ft.Text(size=12)],
                        ),
                    ),
                    # Titulo
                    ft.Text(
                        value=dic.titulo,
                        size=20,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    # Espacio
                    ft.VerticalDivider(width=100),
                ],
            ),
            gesPost,
            post,
            link,
            blokSelecMedia,
            carrucel,
        ],
    )
    # Cuerpo Grupos
    CuerpoProceso = ft.Column(
        disabled=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
        width=350,
        height=420,
        visible=False,
        controls=[
            ft.Text(text_align=ft.TextAlign.CENTER, size=20, color=ft.colors.BLUE),
            blokGrupos,
        ],
    )

    # SS Inicializar
    page.overlay.extend([pick_files_dialog])
    ContarGrupos()
    page.update()

    # SS Cuerpo
    page.views.append(
        ft.View(
            route="/publicacion",
            controls=[
                # TT Cuerpo
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                    width=350,
                    controls=[
                        # Cuerpos
                        CuerpoPost,
                        CuerpoProceso,
                        # ---
                        ventanaPoceso,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                # ft.VerticalDivider(width=40),
                                btPost,
                                btCancelarPost,
                                # btProgramarPost,
                            ],
                        ),
                        aviso,
                        prProgreso,
                    ],
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START,
            bgcolor=page.bgcolor,
        )
    )
