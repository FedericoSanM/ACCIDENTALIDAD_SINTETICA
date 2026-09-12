from copy import deepcopy

import numpy as np
import pandas as pd


# ============================================================
# CONFIGURACIÓN
# ============================================================

DEFAULT_CONFIG = {
    "trabajadores": {
        "nulos": 0.02,
        "duplicados": 0.01,
        "espacios": 0.02,
        "categorias": 0.02,
        "relaciones": 0.01,
        "fechas": 0.01,
    },
    "accidentalidad": {
        "nulos": 0.02,
        "duplicados": 0.01,
        "espacios": 0.02,
        "categorias": 0.02,
        "referencias": 0.01,
        "fechas": 0.01,
        "incapacidad": 0.01,
    },
}


# ============================================================
# UTILIDADES
# ============================================================

def copiar_dataframe(df):
    """
    Crea una copia independiente del DataFrame.

    El dataset CLEAN nunca debe modificarse.
    """
    return df.copy(deep = True)


def calcular_cantidad(n_registros, porcentaje):
    """
    Calcula cuántos registros serán afectados.

    Siempre devuelve al menos 1 cuando el porcentaje
    es mayor que cero y existe información.
    """
    if n_registros == 0 or porcentaje <= 0:
        return 0

    cantidad = int(round(n_registros * porcentaje))

    return max(1, cantidad)


def seleccionar_indices(df, porcentaje, rng):
    """
    Selecciona aleatoriamente registros que serán alterados.
    """
    cantidad = calcular_cantidad(
        len(df),
        porcentaje,
    )

    if cantidad == 0:
        return []

    return rng.choice(
        df.index.to_numpy(),
        size=cantidad,
        replace=False,
    )


# ============================================================
# ERRORES DE TEXTO
# ============================================================

def introducir_espacios(df, columnas, porcentaje, rng):
    """
    Introduce espacios innecesarios en valores de texto.

    Ejemplo:

        'Bogotá'
        ↓
        '  Bogotá '

    """
    df = copiar_dataframe(df)

    columnas_validas = [
        columna
        for columna in columnas
        if columna in df.columns
    ]

    for columna in columnas_validas:

        indices = seleccionar_indices(
            df,
            porcentaje,
            rng,
        )

        for indice in indices:

            valor = df.at[indice, columna]

            if pd.notna(valor):
                df.at[indice, columna] = (
                    f"  {str(valor)} "
                )

    return df


def introducir_variaciones_categoricas(
    df,
    columnas,
    porcentaje,
    rng,
):
    """
    Introduce variaciones de escritura en categorías.

    Ejemplos:

        Masculino → masculino
        Bogotá → BOGOTÁ
        Indefinido → INDEFINIDO
    """
    df = copiar_dataframe(df)

    columnas_validas = [
        columna
        for columna in columnas
        if columna in df.columns
    ]

    for columna in columnas_validas:

        indices = seleccionar_indices(
            df,
            porcentaje,
            rng,
        )

        for indice in indices:

            valor = df.at[indice, columna]

            if pd.isna(valor):
                continue

            valor = str(valor)

            transformacion = rng.choice(
                [
                    "lower",
                    "upper",
                    "title",
                ]
            )

            if transformacion == "lower":
                valor = valor.lower()

            elif transformacion == "upper":
                valor = valor.upper()

            else:
                valor = valor.title()

            df.at[indice, columna] = valor

    return df


# ============================================================
# VALORES NULOS
# ============================================================

def introducir_nulos(
    df,
    columnas,
    porcentaje,
    rng,
):
    """
    Introduce valores nulos de manera controlada.
    """
    df = copiar_dataframe(df)

    columnas_validas = [
        columna
        for columna in columnas
        if columna in df.columns
    ]

    if not columnas_validas:
        return df

    cantidad_total = calcular_cantidad(
        len(df),
        porcentaje,
    )

    for _ in range(cantidad_total):

        columna = rng.choice(
            columnas_validas
        )

        indices_disponibles = df.index[
            df[columna].notna()
        ].to_numpy()

        if len(indices_disponibles) == 0:
            continue

        indice = rng.choice(
            indices_disponibles
        )

        df.at[indice, columna] = np.nan

    return df


# ============================================================
# DUPLICADOS
# ============================================================

def introducir_duplicados(
    df,
    porcentaje,
    rng,
):
    """
    Duplica registros existentes.

    Los duplicados se agregan al final del DataFrame.
    """
    df = copiar_dataframe(df)

    cantidad = calcular_cantidad(
        len(df),
        porcentaje,
    )

    if cantidad == 0:
        return df

    indices = rng.choice(
        df.index.to_numpy(),
        size=cantidad,
        replace=False,
    )

    duplicados = df.loc[indices].copy()

    return pd.concat(
        [df, duplicados],
        ignore_index=True,
    )


# ============================================================
# TRABAJADORES
# ============================================================

def introducir_inconsistencias_trabajadores(
    df,
    porcentaje,
    rng,
):
    """
    Introduce inconsistencias relacionales en trabajadores.

    Estas alteraciones están diseñadas para violar
    reglas que posteriormente pueden ser detectadas
    durante la limpieza/validación.
    """
    df = copiar_dataframe(df)

    cantidad = calcular_cantidad(
        len(df),
        porcentaje,
    )

    if cantidad == 0:
        return df

    # --------------------------------------------------------
    # CIUDAD → DEPARTAMENTO
    # --------------------------------------------------------

    if {
        "ciudad",
        "departamento",
    }.issubset(df.columns):

        indices = rng.choice(
            df.index.to_numpy(),
            size=cantidad,
            replace=False,
        )

        for indice in indices:

            valor_actual = df.at[
                indice,
                "departamento",
            ]

            valores = (
                df["departamento"]
                .dropna()
                .unique()
            )

            valores = [
                valor
                for valor in valores
                if valor != valor_actual
            ]

            if valores:
                df.at[
                    indice,
                    "departamento",
                ] = rng.choice(valores)

    # --------------------------------------------------------
    # FECHA DE RETIRO
    # --------------------------------------------------------

    if {
        "fecha_ingreso",
        "fecha_retiro",
    }.issubset(df.columns):

        indices = rng.choice(
            df.index.to_numpy(),
            size=cantidad,
            replace=False,
        )

        for indice in indices:

            ingreso = df.at[
                indice,
                "fecha_ingreso",
            ]

            if pd.notna(ingreso):

                fecha = pd.Timestamp(
                    ingreso
                ) - pd.Timedelta(
                    days=int(
                        rng.integers(
                            1,
                            365,
                        )
                    )
                )

                df.at[
                    indice,
                    "fecha_retiro",
                ] = fecha

    return df


# ============================================================
# ACCIDENTALIDAD
# ============================================================

def introducir_referencias_invalidas(
    df,
    columna,
    porcentaje,
    rng,
):
    """
    Sustituye algunas referencias por IDs inexistentes.
    """
    df = copiar_dataframe(df)

    if columna not in df.columns:
        return df

    indices = seleccionar_indices(
        df,
        porcentaje,
        rng,
    )

    if len(indices) == 0:
        return df

    valores = pd.to_numeric(
        df[columna],
        errors="coerce",
    )

    maximo = (
        int(valores.max())
        if valores.notna().any()
        else 1000
    )

    for indice in indices:

        df.at[
            indice,
            columna,
        ] = maximo + int(
            rng.integers(
                100,
                10000,
            )
        )

    return df


def introducir_inconsistencias_incapacidad(
    df,
    porcentaje,
    rng,
):
    """
    Introduce valores incompatibles en días de incapacidad.

    Ejemplo:
        valores negativos
        o valores exageradamente altos.
    """
    df = copiar_dataframe(df)

    if "dias_incapacidad" not in df.columns:
        return df

    indices = seleccionar_indices(
        df,
        porcentaje,
        rng,
    )

    for indice in indices:

        valor = rng.choice(
            [
                -1,
                -5,
                999,
            ]
        )

        df.at[
            indice,
            "dias_incapacidad",
        ] = valor

    return df


def introducir_fechas_accidente_invalidas(
    df,
    porcentaje,
    rng,
):
    """
    Genera fechas de accidente potencialmente
    incompatibles con el período del dataset.
    """
    df = copiar_dataframe(df)

    if "fecha_accidente" not in df.columns:
        return df

    indices = seleccionar_indices(
        df,
        porcentaje,
        rng,
    )

    for indice in indices:

        fecha = pd.Timestamp(
            "2010-01-01"
        ) + pd.Timedelta(
            days=int(
                rng.integers(
                    0,
                    365,
                )
            )
        )

        df.at[
            indice,
            "fecha_accidente",
        ] = fecha

    return df


# ============================================================
# DATASET DE TRABAJADORES DIRTY
# ============================================================

def crear_trabajadores_dirty(
    df,
    rng,
    config=None,
):
    """
    Crea una versión DIRTY del dataset de trabajadores.
    """
    configuracion = deepcopy(
        DEFAULT_CONFIG["trabajadores"]
    )

    if config is not None:
        configuracion.update(config)

    dirty = copiar_dataframe(df)

    columnas_texto = [
        "nombre",
        "genero",
        "ciudad",
        "departamento",
        "cargo",
        "nivel",
        "area_proceso",
        "tipo_vinculacion",
    ]

    dirty = introducir_espacios(
        dirty,
        columnas_texto,
        configuracion["espacios"],
        rng,
    )

    dirty = introducir_variaciones_categoricas(
        dirty,
        columnas_texto,
        configuracion["categorias"],
        rng,
    )

    dirty = introducir_nulos(
        dirty,
        columnas_texto,
        configuracion["nulos"],
        rng,
    )

    dirty = introducir_inconsistencias_trabajadores(
        dirty,
        configuracion["relaciones"],
        rng,
    )

    dirty = introducir_duplicados(
        dirty,
        configuracion["duplicados"],
        rng,
    )

    return dirty


# ============================================================
# DATASET DE ACCIDENTALIDAD DIRTY
# ============================================================

def crear_accidentalidad_dirty(
    df,
    rng,
    config=None,
):
    """
    Crea una versión DIRTY del dataset de accidentalidad.
    """
    configuracion = deepcopy(
        DEFAULT_CONFIG["accidentalidad"]
    )

    if config is not None:
        configuracion.update(config)

    dirty = copiar_dataframe(df)

    columnas_texto = [
        "tipo_accidente",
        "mecanismo",
        "agente",
        "tipo_lesion",
        "parte_cuerpo",
        "codigo_diagnostico",
        "diagnostico",
        "area_accidente",
        "gravedad_accidente",
    ]

    dirty = introducir_espacios(
        dirty,
        columnas_texto,
        configuracion["espacios"],
        rng,
    )

    dirty = introducir_variaciones_categoricas(
        dirty,
        columnas_texto,
        configuracion["categorias"],
        rng,
    )

    dirty = introducir_nulos(
        dirty,
        columnas_texto,
        configuracion["nulos"],
        rng,
    )

    dirty = introducir_referencias_invalidas(
        dirty,
        "id_trabajador",
        configuracion["referencias"],
        rng,
    )

    dirty = introducir_inconsistencias_incapacidad(
        dirty,
        configuracion["incapacidad"],
        rng,
    )

    dirty = introducir_fechas_accidente_invalidas(
        dirty,
        configuracion["fechas"],
        rng,
    )

    dirty = introducir_duplicados(
        dirty,
        configuracion["duplicados"],
        rng,
    )

    return dirty