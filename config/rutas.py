from pathlib import Path


RAIZ_PROYECTO = Path(__file__).resolve().parent.parent

CARPETA_DATOS = RAIZ_PROYECTO / "data"

CARPETA_SAMPLE = CARPETA_DATOS / "sample"

CARPETA_DIRTY = CARPETA_DATOS / "dirty"

CARPETA_RESULTADOS = RAIZ_PROYECTO / "resultados"


def crear_carpetas_salida():
    CARPETA_SAMPLE.mkdir(parents = True, exist_ok = True)
    CARPETA_DIRTY.mkdir(parents = True, exist_ok = True)
    CARPETA_RESULTADOS.mkdir(parents = True, exist_ok = True)