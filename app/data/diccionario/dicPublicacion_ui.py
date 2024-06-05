# TT view Publicacion
class Publicacion:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # CUERPO GENERAL
        self.titulo = ""
        self.btGuardar_Tool = ""
        self.btCargar_Tool = ""
        self.labeCuerpoPots = ""
        self.labeLink = ""
        self.btCargarMedia = ""
        self.btBorrarMedia = ""
        self.titVentanaProceso = ""
        self.btPublicar = ""
        self.btCancelar = ""

        # DIALOGOS GRUPOS
        self.dia_GrupTitulo = ""
        self.pal_Grupo = ""
        self.dia_brGuardar = ""
        self.dia_btSincGrup_Tool = ""
        self.dia_EstadoPublicado = ""
        self.dia_EstadoPendiente = ""
        self.dia_EstadoPublicando = ""

        # DIALOGOS POST GUARDADOS
        self.dia_PostTitulo = ""
        self.dia_PostBtCerrar = ""

        # SS Español
        if lenguaje == "ES":
            # CUERPO GENERAL ES
            self.titulo = "Publicación"
            self.btGuardar_Tool = "Guardar publicación"
            self.btCargar_Tool = "Cargar publicación"
            self.labeCuerpoPots = "Cuerpo publicación"
            self.labeLink = "Link"
            self.btCargarMedia = "Adjuntar media"
            self.btBorrarMedia = "Eliminar media"
            self.titVentanaProceso = "Proceso"
            self.btPublicar = "Publicar"
            self.btCancelar = "Cancelar"

            # DIALOGOS GRUPOS ES
            self.dia_GrupTitulo = "Publicado en "
            self.pal_Grupo = "Grupos"
            self.dia_brGuardar = "Guardar"
            self.dia_btSincGrup_Tool = "Sincronizar grupos"
            self.dia_EstadoPublicado = "Publicado"
            self.dia_EstadoPendiente = "Pendiente"
            self.dia_EstadoPublicando = "Publicando..."

            # DIALOGOS POST GUARDADOS ES
            self.dia_PostTitulo = "Cargar publicación"
            self.dia_PostBtCerrar = "Cerrar"

        # SS Ingles
        if lenguaje == "EN":
            # CUERPO GENERAL EN
            self.titulo = "Post"
            self.btGuardar_Tool = "Save post"
            self.btCargar_Tool = "Load post"
            self.labeCuerpoPots = "Body"
            self.labeLink = "Link"
            self.btCargarMedia = "Add media"
            self.btBorrarMedia = "Remove media"
            self.titVentanaProceso = "Proceso"
            self.btPublicar = "Post"
            self.btCancelar = "Cancel"

            # DIALOGOS GRUPOS EN
            self.dia_GrupTitulo = "Published in "
            self.pal_Grupo = "Groups"
            self.dia_brGuardar = "Save"
            self.dia_btSincGrup_Tool = "Sync groups"
            self.dia_EstadoPublicado = "Published"
            self.dia_EstadoPendiente = "Earring"
            self.dia_EstadoPublicando = "Posting..."

            # DIALOGOS POST GUARDADOS EN
            self.dia_PostTitulo = "Load post"
            self.dia_PostBtCerrar = "Cancel"


# TT view model Publicacion
class VMPublicacion:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # CUERPO GENERAL
        self.postDefault = ""

        # AVISO SINCRONIZAR GRUPOS
        self.avis_SincGrupos = []

        # AVISO GUARDAR POST
        self.avis_GuardarPost = []

        # AVISO PUBLICAR
        self.avis_PalGrupo = ""
        self.avis_Publicar = []

        # SS Español
        if lenguaje == "ES":
            # CUERPO GENERAL ES
            self.postDefault = "Pub nuevo"

            # AVISO SINCRONIZAR GRUPOS 1 ES
            self.avis_SincGrupos.append("No hay grupos guardados")  # 0
            self.avis_SincGrupos.append("Grupos cargados")  # 1

            # AVISO GUARDAR POST 7 ES
            self.avis_GuardarPost.append("Guardando publicación...")  # 0
            self.avis_GuardarPost.append("No se logró guardar la publicación")  # 1
            self.avis_GuardarPost.append("Publicación guardada")  # 2
            self.avis_GuardarPost.append("Cargando publicación...")  # 3
            self.avis_GuardarPost.append("Cargando publicaciones guardadas...")  # 4
            self.avis_GuardarPost.append(
                "No se pudieron cargar las publicaciones guardadas"
            )  # 5
            self.avis_GuardarPost.append("Publicaciones cargadas")  # 6
            self.avis_GuardarPost.append("Publicación cargada")  # 7

            # AVISO PUBLICAR 5 ES
            self.avis_PalGrupo = "Grupos"
            self.avis_Publicar.append("Publicando en: ")  # 0
            self.avis_Publicar.append("Publicando en grupo: ")  # 1
            self.avis_Publicar.append("Se publicó en: ")  # 2
            self.avis_Publicar.append("Proceso Cancelado")  # 3
            self.avis_Publicar.append("Continuando en: ")  # 4
            self.avis_Publicar.append("Proceso auto-post expirado")  # 5

        # SS Ingles
        if lenguaje == "EN":
            # CUERPO GENERAL EN
            self.postDefault = "New post"

            # AVISO SINCRONIZAR GRUPOS 1 EN
            self.avis_SincGrupos.append("There are no saved groups")  # 0
            self.avis_SincGrupos.append("Loaded groups")  # 1

            ## AVISO GUARDAR POST 7 EN
            self.avis_GuardarPost.append("Saving post...")  # 0
            self.avis_GuardarPost.append("Post could not be saved")  # 1
            self.avis_GuardarPost.append("Saved post")  # 2
            self.avis_GuardarPost.append("Loading post...")  # 3
            self.avis_GuardarPost.append("Loading saved posts...")  # 4
            self.avis_GuardarPost.append("Saved posts could not be loaded")  # 5
            self.avis_GuardarPost.append("Posts uploaded")  # 6
            self.avis_GuardarPost.append("Post uploaded")  # 7

            # AVISO PUBLICAR 5 EN
            self.avis_PalGrupo = "Groups"
            self.avis_Publicar.append("Posting in: ")  # 0
            self.avis_Publicar.append("Group posting: ")  # 1
            self.avis_Publicar.append("It was published in:")  # 2
            self.avis_Publicar.append("Canceled Process")  # 3
            self.avis_Publicar.append("Continuing on:")  # 4
            self.avis_Publicar.append("Auto-post process expired")  # 5


# TT view model Publicacion
class ACPublicacion:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # AVISO PUBLICAR
        self.avis_Cancelar = ""
        self.avis_Publicar = []

        # SS Español
        if lenguaje == "ES":
            # AVISO PUBLICAR 25 ES
            self.avis_Cancelar = "Proceso Cancelado"
            self.avis_Publicar.append("Cargando grupo: ")  # 0
            self.avis_Publicar.append("Error al acceder al navegador")  # 1
            self.avis_Publicar.append("Página de grupo cargado con éxito")  # 2
            self.avis_Publicar.append("Error al cargar página de grupo")  # 3
            self.avis_Publicar.append("Buscando datos grupo...")  # 4
            self.avis_Publicar.append("Título de grupo: ")  # 5
            self.avis_Publicar.append("No se encontró título de grupo")  # 6
            self.avis_Publicar.append("No se encontró portada de grupo")  # 7
            self.avis_Publicar.append("No se encontró cantidad de miembros")  # 8
            self.avis_Publicar.append("Guardando datos grupo...")  # 9
            self.avis_Publicar.append("Buscando input de publicación...")  # 10
            self.avis_Publicar.append("No se encontró input de publicación")  # 11
            self.avis_Publicar.append("Cargando archivos...")  # 12
            self.avis_Publicar.append("No se encontró botón de agregar media")  # 13
            self.avis_Publicar.append("Cargando archivos 2...")  # 14
            self.avis_Publicar.append("No se encontró botón de agregar media 2")  # 15
            self.avis_Publicar.append("Cargando archivos 3...")  # 16
            self.avis_Publicar.append("Archivos cargados")  # 17
            self.avis_Publicar.append("Buscando input de publicación 2...")  # 18
            self.avis_Publicar.append("No se encontró input de publicación 2")  # 19
            self.avis_Publicar.append("Escribiendo...")  # 20
            self.avis_Publicar.append("Pegando link: ")  # 21
            self.avis_Publicar.append("Buscando botón publicar")  # 22
            self.avis_Publicar.append("No se encontró botón de publicación")  # 23
            self.avis_Publicar.append("Publicación limitada")  # 24

        # SS Ingles
        if lenguaje == "EN":
            # AVISO PUBLICAR 25 EN
            self.avis_Cancelar = "Canceled Process"
            self.avis_Publicar.append("Loading group: ")  # 0
            self.avis_Publicar.append("Error accessing the browser")  # 1
            self.avis_Publicar.append("Group page loaded successfully")  # 2
            self.avis_Publicar.append("Error loading group page")  # 3
            self.avis_Publicar.append("Searching for group data...")  # 4
            self.avis_Publicar.append("Group title: ")  # 5
            self.avis_Publicar.append("No group title found")  # 6
            self.avis_Publicar.append("No group cover found")  # 7
            self.avis_Publicar.append("No number of members found")  # 8
            self.avis_Publicar.append("Saving group data...")  # 9
            self.avis_Publicar.append("Looking for publication input...")  # 10
            self.avis_Publicar.append("No publication entry found")  # 11
            self.avis_Publicar.append("Loading files...")  # 12
            self.avis_Publicar.append("No add media button found")  # 13
            self.avis_Publicar.append("Loading files 2...")  # 14
            self.avis_Publicar.append("No add media button found 2")  # 15
            self.avis_Publicar.append("Loading files 3...")  # 16
            self.avis_Publicar.append("Archivos cargados")  # 17
            self.avis_Publicar.append("Looking for publication input 2...")  # 18
            self.avis_Publicar.append("No publication entry 2 found")  # 19
            self.avis_Publicar.append("Writing...")  # 20
            self.avis_Publicar.append("Pasting link: ")  # 21
            self.avis_Publicar.append("Looking for publish button")  # 22
            self.avis_Publicar.append("No publish button found")  # 23
            self.avis_Publicar.append("Limited publication")  # 24
