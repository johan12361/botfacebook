# TT web Pagina Grupos
class PaginaGrupos:
    # Asignar
    def __init__(self, lenguaje: str) -> None:

        # SS Iniciar
        # informacion para extraer
        self.eti_miembros = ""
        self.input_PublicMain = ""
        self.input_PublicDia = ""
        self.bt_FotoVideo = ""
        self.bt_Publicar = ""
        self.msg_LimitarPost = ""

        # SS Facebook Español
        if lenguaje == "ES":
            self.eti_miembros = "miembros"
            self.input_PublicMain = "Escribe algo"
            self.input_PublicDia = "Crea una publicación"
            self.bt_FotoVideo = "Foto/video"
            self.bt_Publicar = "Publicar"
            self.msg_LimitarPost = "Limitamos la frecuencia con la que puedes publicar"

        # SS Facebook Ingles
        if lenguaje == "EN":
            self.eti_miembros = "members"
            self.input_PublicMain = "Write something"
            self.input_PublicDia = "Create a public post"
            self.bt_FotoVideo = "Photo/video"
            self.bt_Publicar = "Post"
            # SIN PROBAR***************************
            self.msg_LimitarPost = "limit how often you can post"
