from enum import Enum


class ColorAviso(Enum):
    ok = (1,)
    error = (2,)
    precaucion = (3,)
    correcto = (4,)


class EstadoGrupo(Enum):
    Publico = (0,)
    Privado = (1,)
