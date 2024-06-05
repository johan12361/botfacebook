import os
import time
import asyncio

# TT archivos
from data.actividad import ac_compartirGrupos as ac
from data.gestroDatos import CargarConfig, CargarGrupo, GuardarPost, CargarPostGuardados
from data.enums import ColorAviso
from data.singeltons import IdGrupo, Post
from data.diccionario.dicPublicacion_ui import VMPublicacion as Dic


class VmPublicacion:
    def __init__(self, aviso: list[str, ColorAviso], reintentar: list[bool, str]):
        self.config = CargarConfig()
        self.dic = Dic(self.config.lenguaje)
        self.aviso = aviso
        self.reintentarPost = reintentar
        self.cancelarPorceso = False

        self.corrReintentar = asyncio.Runner()
        self.loppActivo = True

        self.postGuardados: list[Post] = []
        # Post
        self.idGrupos: list[IdGrupo] = self.__CargarGrupos()
        self.nombrePost = self.dic.postDefault
        self.post = ""
        self.link = ""
        self.imgs = []
        self.postProgramado = False
        self.fechaPost = None
        self.horaPost = None

    def __CargarGrupos(self):
        if os.path.exists(self.config.rutaGrupos):
            with open(self.config.rutaGrupos, "r") as data:
                lista = data.readlines()
                new = []
                for i in range(len(lista)):
                    lista[i] = lista[i].replace("\n", "")
                    if lista[i] != "":
                        new.append(CargarGrupo(lista[i]))
                return new

    def SincroGrupos(self):
        # carga todos los grupos
        todos = self.__CargarGrupos()
        total = []

        if todos == None or len(todos) == 0:
            # No hay grupos guardados
            self.aviso([self.dic.avis_SincGrupos[0], ColorAviso.precaucion])
            return
        if self.idGrupos == None or self.idGrupos == []:
            total = todos
        else:
            for i in range(len(todos)):
                total.append(todos[i])
                for ii in range(len(self.idGrupos)):
                    if todos[i].url == self.idGrupos[ii].url:
                        total[i] = self.idGrupos[ii]

        self.idGrupos = total
        # Grupos cargados
        self.aviso([self.dic.avis_SincGrupos[1], ColorAviso.correcto])

    def GuardarPost(self):
        # Guardando publicación...
        self.aviso([self.dic.avis_GuardarPost[0], ColorAviso.ok])
        post = Post()
        # asignar
        post.nombre = self.nombrePost
        post.post = self.post
        post.link = self.link
        post.media = self.imgs
        post.grupos = self.idGrupos
        post.postProgramado = self.postProgramado
        post.fechaPost = self.fechaPost
        post.horaPost = self.horaPost
        try:
            GuardarPost(post, True)
        except:
            # No se logró guardar la publicación
            self.aviso([self.dic.avis_GuardarPost[1], ColorAviso.error])
            return
        # Publicación guardada
        self.aviso([self.dic.avis_GuardarPost[2], ColorAviso.correcto])

    def CargarPost(self, id: int):
        # Cargando publicación...
        self.aviso([self.dic.avis_GuardarPost[3], ColorAviso.ok])
        postN = self.postGuardados[id]
        # asignar
        self.post = postN.post
        self.link = postN.link
        self.imgs = postN.media
        self.nombrePost = postN.nombre
        self.idGrupos = postN.grupos
        self.postProgramado = postN.postProgramado
        self.fechaPost = postN.fechaPost
        self.horaPost = postN.horaPost
        # Publicaciones cargadas
        self.aviso([self.dic.avis_GuardarPost[7], ColorAviso.correcto])

    def PostGuardados(self):
        # Cargando publicaciones guardadas...
        self.aviso([self.dic.avis_GuardarPost[4], ColorAviso.ok])
        try:
            self.postGuardados = CargarPostGuardados()
        except:
            # No se pudieron cargar las publicaciones guardadas
            self.aviso([self.dic.avis_GuardarPost[5], ColorAviso.error])
            return
        # Publicaciones cargadas
        self.aviso([self.dic.avis_GuardarPost[6], ColorAviso.ok])

        for i in self.postGuardados:
            print(i.nombre)

    # SS Publicar**********************************
    def Publicar(self, manual=True):

        # contan grupos selec
        gruposLogrados = 0
        gruposSelec = 0
        for i in range(len(self.idGrupos)):
            if self.idGrupos[i].selec:
                gruposSelec = gruposSelec + 1
                if self.idGrupos[i].estado == "":
                    self.idGrupos[i].estado = "pendiente"

        # Activar cuerpo
        self.aviso(["ACT-", ColorAviso.ok])
        # Publicando en:
        self.aviso(
            [
                self.dic.avis_Publicar[0]
                + str(gruposSelec)
                + " "
                + self.dic.avis_PalGrupo,
                ColorAviso.ok,
            ]
        )
        # TT Inicio ciclo
        for i in range(len(self.idGrupos)):
            if self.idGrupos[i].selec:
                # Publicando en grupo:
                self.aviso(
                    [
                        self.dic.avis_Publicar[0] + " " + self.idGrupos[i].nombre + " ",
                        ColorAviso.ok,
                    ]
                )
                # SS Iniciar publicacion
                self.idGrupos[i].estado = "Publicando..."
                self.aviso(["ACT-", ColorAviso.ok])
                estado = ac.Compartir(
                    idGrupo=self.idGrupos[i],
                    post=self.post,
                    imgs=self.imgs,
                    link=self.link,
                    aviso=self.aviso,
                    cancelar=lambda: self.cancelarPorceso,
                )
                # SS si es correcto
                if estado == "-OK-":
                    gruposLogrados = gruposLogrados + 1
                    # Se publicó en:
                    self.aviso(
                        [
                            self.dic.avis_Publicar[2] + self.idGrupos[i].nombre + " ",
                            ColorAviso.correcto,
                        ]
                    )
                    self.idGrupos[i].selec = False
                    self.idGrupos[i].estado = "publicado"
                    self.aviso(["ACT-", ColorAviso.ok])

                # SS si hubo un problema al publicar
                else:
                    self.idGrupos[i].estado = "pendiente"
                    self.aviso(["ACT-", ColorAviso.ok])
                    if "FIN-" in estado:
                        depurado = estado.replace("FIN-", "")
                        self.aviso([depurado, ColorAviso.error])
                        break
                    else:
                        self.aviso(
                            [
                                estado + ": " + self.idGrupos[i].nombre + " ",
                                ColorAviso.precaucion,
                            ]
                        )

                # SS Si se cancela
                if self.cancelarPorceso:
                    # Proceso Cancelado
                    self.aviso([self.dic.avis_Publicar[3], ColorAviso.precaucion])
                    time.sleep(1)
                    break

                # SS Contador
                if i < len(self.idGrupos) - 1:
                    tiempo = int(self.config.esperaEntreGrupos)
                    for i in range(tiempo):
                        self.aviso(
                            # Continuando en:
                            [
                                "xxx"
                                + self.dic.avis_Publicar[4]
                                + str(tiempo - i)
                                + " ",
                                ColorAviso.correcto,
                            ]
                        )
                        time.sleep(1)

        # SS Estados de finalizacion
        #
        self.aviso(
            # Publicando en:
            [
                self.dic.avis_Publicar[0]
                + str(gruposLogrados)
                + "/"
                + str(gruposSelec)
                + " "
                + self.dic.avis_PalGrupo,
                ColorAviso.correcto,
            ]
        )
        self.cancelarPorceso = False
        if gruposLogrados == gruposSelec:
            return True
        else:
            return False

    # TT Bucle de intentos
    async def BucleIntento(self):
        repeticiones = 10
        # Comprobar cantidad de vecer
        for i in range(repeticiones):
            tiempo = self.config.tiempoEsperaReintento * 60
            # Contar
            for i in range(tiempo):
                if self.config.reintentarPots and self.loppActivo:
                    total = tiempo - i
                    minutos = total // 60
                    segundos = total - (minutos * 60)

                    self.reintentarPost(
                        [
                            False,
                            str(minutos) + ":" + str(segundos),
                        ]
                    )
                    print("*/*/*/BucleIntento/*/*/")
                    await asyncio.sleep(1)
                else:
                    return
            # fin de contar
            # Apagr ui
            if self.loppActivo == False:
                return
            self.reintentarPost([True, ""])
            completo = self.Publicar(manual=False)
            self.reintentarPost([True, "encender"])
            if completo:
                return
        # no se logro completar las publicaciones en los 10 intentos
        # Proceso auto-post expirado
        self.aviso([self.dic.avis_GuardarPost[5], ColorAviso.precaucion])
