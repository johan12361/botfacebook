import flet as ft
from enum import Enum
# TT archivos
from data.singeltons import Config
from data.gestroDatos import GuardarConfig
from data.diccionario.dicVentanaConfig_ui import VentanaConfig as Dic


class EnuTipoVentana(Enum):
    general = 0
    web = 1


class VentanaConfig:

    # TT Funciones
    def activar(self):
        self.page.dialog = self.dialogo
        self.dialogo.open = True

        # Tipo view
        if self.tView == "config":
            self.contActivo = EnuTipoVentana.general
            self.CambiarContenedor(self.contActivo)
        self.page.update()
        pass

    def Guardar(self):
        GuardarConfig(self.config)
        self.dialogo.open = False
        self.page.update()

    def CambiarContenedor(self, tipo: EnuTipoVentana):

        # color icono
        for icon in self.carrusel.controls:
            if icon.key == tipo.value:
                icon.icon_color = ft.colors.GREEN
            else:
                icon.icon_color = ft.colors.BLUE

        # activar contenedor
        for cont in self.dialogo.content.controls[1].controls:
            if cont.key == tipo.value:
                cont.visible = True
            else:
                cont.visible = False

        self.contActivo = tipo
        self.page.update()

    # SS General
    def DatosGrupos(self, e):
        self.config.datosGrupos = e.control.value
        self.page.update()

    def TiempoEsperaGrupo(self, e):
        self.config.esperaEntreGrupos = e.control.value
        print (str(self.config.esperaEntreGrupos))
        self.page.update()
        
    def ReintentarPost(self,e):
        self.config.reintentarPots = e.control.value
        self.listGen.controls[3].controls[0].visible = e.control.value
        self.listGen.controls[3].controls[1].visible = e.control.value
        self.page.update()
        
    def TiempoReintentoPost(self, e):
        self.config.tiempoEsperaReintento = int(e.control.value)
        print(str(self.config.tiempoEsperaReintento))
        self.page.update()
    
    # SS Web
    def SelecionarDriver(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.listNav.controls[1].controls[1].text = e.files[0].path
            self.listNav.controls[1].controls[1].tooltip = e.files[0].path
            self.config.rutaWebdriver = e.files[0].path
        self.listNav.update()

    def WebDriverInterno(self, e):
        self.config.usarWebdriver = e.control.value
        self.listNav.controls[1].controls[0].visible = e.control.value
        self.listNav.controls[1].controls[1].visible = e.control.value
        self.page.update()

    def NavOculto(self, e):
        self.config.navOculto = e.control.value

    def __init__(self, page: ft.Page, cof: Config, tView: str):
        self.page = page
        self.config = cof
        self.contActivo: EnuTipoVentana = EnuTipoVentana.general
        self.tView = tView
        self.dic = Dic(cof.lenguaje)

        # TT Controles                                                      

        # SS Carrucel
        self.carrusel = ft.Row(
            spacing=3,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                # general
                ft.IconButton(
                    key=0,
                    icon=ft.icons.DISPLAY_SETTINGS,
                    height=40,
                    width=40,
                    icon_size=24,
                    alignment=ft.alignment.center,
                    tooltip=self.dic.toolIcoGeneral,
                    on_click=lambda _: self.CambiarContenedor(EnuTipoVentana.general),
                ),
                # navegador
                ft.IconButton(
                    key=1,
                    icon=ft.icons.OPEN_IN_BROWSER,
                    height=40,
                    width=40,
                    icon_size=24,
                    alignment=ft.alignment.center,
                    tooltip=self.dic.toolIcoWeb,
                    on_click=lambda _: self.CambiarContenedor(EnuTipoVentana.web),
                ),
            ],
        )

        # SS General
        self.listGen = ft.ListView(
            key=0,
            width=320,
            height=400,
            controls=[
                # Descargar datos de grupos
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.g_DatosGrupos,
                            size=14,
                        ),
                        ft.Checkbox(
                            value=self.config.datosGrupos, on_change=self.DatosGrupos
                        ),
                    ],
                ),
                # Espera entre grupos
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.g_EsperaGrupos,
                            size=14,
                            
                        ),
                        ft.Slider(
                            round=0,
                            min=10,
                            max=60,
                            divisions=10,
                            value=self.config.esperaEntreGrupos,
                            label="{value}sgs",
                            on_change_end=self.TiempoEsperaGrupo,
                            width=120
                        ),
                    ],
                ),
                #eintentar post
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.g_ReintetarPost,
                            size=14,
                        ),
                        ft.Checkbox(
                            value=self.config.reintentarPots, on_change=self.ReintentarPost
                        ),

                    ],
                ),
                # Tiempo Reintento
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.g_ReintentarCada,
                            size=14,
                            visible=self.config.reintentarPots,
                        ),
                        ft.Slider(
                            round=0,
                            min=10,
                            max=120,
                            divisions=11,
                            value=self.config.tiempoEsperaReintento,
                            label="{value}min",
                            on_change_end=self.TiempoReintentoPost,
                            visible=self.config.reintentarPots,
                            
                        ),
                    ],
                ),
            ],
        )

        # SS Web
        self.pick_files_dialog = ft.FilePicker(on_result=self.SelecionarDriver)
        self.listNav = ft.ListView(
            key=1,
            width=320,
            height=400,
            controls=[
                # usar navegador interno
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.w_UsarWebExterno,
                            size=14,
                        ),
                        ft.Checkbox(
                            value=self.config.usarWebdriver, on_change=self.WebDriverInterno
                        ),
                    ],
                ),
                # ruta navegar externo
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.w_RutaWebDriver,
                            size=14,
                            visible=self.config.usarWebdriver,
                        ),
                        ft.TextButton(
                            text=self.config.rutaWebdriver,
                            width=100,
                            height=24,
                            visible=self.config.usarWebdriver,
                            on_click=lambda _: self.pick_files_dialog.pick_files(
                                allow_multiple=False,
                                file_type=ft.FilePickerFileType.CUSTOM,
                                allowed_extensions=["exe"],
                            ),
                        ),
                    ],
                ),
                # Navegador oculto
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value=self.dic.w_OcultarNavegador,
                            tooltip=self.dic.w_OcultarNavegadorTool,
                            size=14,
                        ),
                        ft.Checkbox(value=self.config.navOculto, on_change=self.NavOculto),
                    ],
                ),
            ],
        )

        # TT Dialogo
        self.dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text(self.dic.titDialo),
            inset_padding=ft.padding.Padding(20, 60, 20, 60),
            actions_padding=20,
            title_padding=20,
            content_padding=10,
            actions_alignment=ft.MainAxisAlignment.CENTER,
            actions=[
                ft.TextButton(
                    icon=ft.icons.SAVE,
                    icon_color=ft.colors.GREEN,
                    text=self.dic.btGuardar,
                    on_click=lambda _: self.Guardar(),
                )
            ],
            content=ft.Column(
                controls=[
                    self.carrusel,
                    ft.Stack(height=400, controls=[self.listNav, self.listGen]),
                ]
            ),
        )
