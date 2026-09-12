import pandas as pd

COLUMNAS_TRABAJADORES = [
    "id_trabajador",
    "nombre",
    "fecha_nacimiento",
    "edad",
    "genero",
    "ciudad",
    "departamento",
    "cargo",
    "nivel",
    "area_proceso",
    "tipo_vinculacion",
    "fecha_ingreso",
    "fecha_retiro",
]

COLUMNAS_ACCIDENTALIDAD = [
    "id_accidente",
    "id_trabajador",
    "fecha_accidente",
    "tipo_accidente",
    "mecanismo",
    "agente",
    "area_accidente",
    "codigo_diagnostico",
    "diagnostico",
    "tipo_lesion",
    "parte_cuerpo",
    "gravedad_accidente",
    "dias_incapacidad",
    "salario",
]


def crear_dataframe_trabajadores(
    trabajadores,
):
    """
    Convierte la matriz de trabajadores generada
    por el modelo en un DataFrame.
    """

    df = pd.DataFrame(
        trabajadores
    )

    columnas_faltantes = [
        columna
        for columna in COLUMNAS_TRABAJADORES
        if columna not in df.columns
    ]

    if columnas_faltantes:
        raise ValueError(
            "Faltan columnas en trabajadores: "
            f"{columnas_faltantes}"
        )

    return df[
        COLUMNAS_TRABAJADORES
    ].copy()


def crear_dataframe_accidentalidad(
    accidentes,
):
    """
    Convierte la matriz de accidentalidad generada
    por el modelo en un DataFrame.
    """

    df = pd.DataFrame(
        accidentes
    )

    columnas_faltantes = [
        columna
        for columna in COLUMNAS_ACCIDENTALIDAD
        if columna not in df.columns
    ]

    if columnas_faltantes:
        raise ValueError(
            "Faltan columnas en accidentalidad: "
            f"{columnas_faltantes}"
        )

    return df[
        COLUMNAS_ACCIDENTALIDAD
    ].copy()