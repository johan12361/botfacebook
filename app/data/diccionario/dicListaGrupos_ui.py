# TT view Lista Grupos
class ListaGrupos:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Iniciar
        self.titulo = ""
        self.titVentanaProgreso = ""
        self.btObtenerDatos = ""
        self.btCancelar = ""
        self.btGuardar = ""
        self.btContinuar = ""

        # SS Español
        if lenguaje == "ES":
            self.titulo = "Links de grupos"
            self.titVentanaProgreso = "Progreso"
            self.btObtenerDatos = "Obtener datos"
            self.btCancelar = "Cancelar"
            self.btGuardar = "Guardar"
            self.btContinuar = "CONTINUAR"

        # SS Ingles
        if lenguaje == "EN":
            self.titulo = "Group links"
            self.titVentanaProgreso = "Progress"
            self.btObtenerDatos = "Get information"
            self.btCancelar = "Stop"
            self.btGuardar = "Save"
            self.btContinuar = "NEXT"


# TT View Model
class VMListaGrupos:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Iniciar
        self.avis_Grupos = []

        # SS Español
        if lenguaje == "ES":
            self.avis_Grupos.append("Guardando listado de grupos...")  # 0
            self.avis_Grupos.append("Grupos guardados")  # 1
            self.avis_Grupos.append("Cargando ids grupos...")  # 2
            self.avis_Grupos.append("Iniciando búsqueda de datos...")  # 3
            self.avis_Grupos.append("Cancelando...")  # 4
            self.avis_Grupos.append("FIN DE BÚSQUEDA")  # 5

        # SS Ingles
        if lenguaje == "EN":
            self.avis_Grupos.append("Saving group list...")  # 0
            self.avis_Grupos.append("Saved groups")  # 1
            self.avis_Grupos.append("Loading group ids...")  # 2
            self.avis_Grupos.append("Starting data search...")  # 3
            self.avis_Grupos.append("Canceling...")  # 4
            self.avis_Grupos.append("END OF SEARCH")  # 5


# TT AC Login
class ACListaGrupos:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Login
        self.avis_ObtenerDatos = []

        # SS Español
        if lenguaje == "ES":
            self.avis_ObtenerDatos.append("Cargando grupo: ")  # 0
            self.avis_ObtenerDatos.append("Error al acceder al navegador")  # 1
            self.avis_ObtenerDatos.append("Cargando página...")  # 2
            self.avis_ObtenerDatos.append("Página tardó demasiado en responder")  # 3
            self.avis_ObtenerDatos.append("Buscando datos grupo...")  # 4
            self.avis_ObtenerDatos.append("Título de grupo: ")  # 5
            self.avis_ObtenerDatos.append("No se encontró título de grupo")  # 6
            self.avis_ObtenerDatos.append("No se encontró portada de grupo")  # 7
            self.avis_ObtenerDatos.append(
                "No se encontró cantidad de miembros del grupo"
            )  # 8
            self.avis_ObtenerDatos.append("Guardando datos grupo")  # 9

        # SS Ingles
        if lenguaje == "EN":
            self.avis_ObtenerDatos.append("Loading group: ")  # 0
            self.avis_ObtenerDatos.append("Error accessing the browser")  # 1
            self.avis_ObtenerDatos.append("Loading page...")  # 2
            self.avis_ObtenerDatos.append("Page took too long to respond")  # 3
            self.avis_ObtenerDatos.append("Searching for group data...")  # 4
            self.avis_ObtenerDatos.append("Group title: ")  # 5
            self.avis_ObtenerDatos.append("No group title found")  # 6
            self.avis_ObtenerDatos.append("No group cover found")  # 7
            self.avis_ObtenerDatos.append("No number of group members found")  # 8
            self.avis_ObtenerDatos.append("Saving group data")  # 9
