import os
import time

# TT archivos
from data.enums import ColorAviso
from data.gestroDatos import CargarConfig, CargarGrupo
from data.actividad import ac_buscarDatosGrupos as ac
from data.diccionario.dicListaGrupos_ui import VMListaGrupos as Dic


class VmListGrupo:

    def __init__(self, aviso: list[str, ColorAviso]):
        self.config = CargarConfig()
        # diciionario
        self.dic = Dic(self.config.lenguaje)

        self.grupos = self.CargarGrupos()
        self.aviso = aviso
        self.Recaudando = False

    def CargarGrupos(self):
        if os.path.exists(self.config.rutaGrupos):
            with open(self.config.rutaGrupos, "r") as data:
                return data.read()

    def GuardarGrupos(self, grupos: str):
        # Guardando listado de grupos...
        self.aviso([self.dic.avis_Grupos[0], ColorAviso.ok])
        self.grupos = grupos
        with open(self.config.rutaGrupos, "w") as data:
            data.write(self.grupos)
            # Grupos guardados
            self.aviso([self.dic.avis_Grupos[1], ColorAviso.correcto])

    def __CargarIds(self):
        if os.path.exists(self.config.rutaGrupos):
            with open(self.config.rutaGrupos, "r") as data:
                lista = data.readlines()
                new = []
                for i in range(len(lista)):
                    lista[i] = lista[i].replace("\n", "")
                    if lista[i] != "":
                        new.append(CargarGrupo(lista[i]))
                return new

    def RecaudarDatosGrupos(self):
        # Cargando ids grupos...
        self.aviso([self.dic.avis_Grupos[2], ColorAviso.ok])
        idGrupos = self.__CargarIds()

        # Iniciando búsqueda de datos...
        self.aviso([self.dic.avis_Grupos[3], ColorAviso.ok])
        self.Recaudando = True
        for i in range(len(idGrupos)):
            if self.Recaudando:
                ac.RecopilarDatos(idGrupo=idGrupos[i], aviso=self.aviso)
                time.sleep(1)
            else:
                # Cancelando...
                self.aviso([self.dic.avis_Grupos[4], ColorAviso.ok])
                break

        # FIN DE BÚSQUEDA
        self.aviso([self.dic.avis_Grupos[5], ColorAviso.correcto])

    def CancelarRecaudo(self):
        self.Recaudando = False
