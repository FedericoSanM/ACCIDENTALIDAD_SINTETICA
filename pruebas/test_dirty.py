import numpy as np
import pandas as pd

from src.dirty import (
    calcular_cantidad,
    seleccionar_indices,
    introducir_espacios,
    introducir_variaciones_categoricas,
    introducir_nulos,
    introducir_duplicados,
    crear_trabajadores_dirty,
    crear_accidentalidad_dirty,
)

from src.dataframes import (
    crear_dataframe_trabajadores,
    crear_dataframe_accidentalidad,
)

from src.trabajadores import generar_trabajadores
from src.accidentalidad import generar_accidentalidad_anual

from config.parametros import (
    TOTAL_TRABAJADORES,
    FECHA_INICIO_EMPRESA,
    FECHA_CORTE,
    SEED,
)

from datetime import date


# ============================================================
# DATOS DE PRUEBA
# ============================================================

def generar_dataframe_trabajadores_prueba():
    trabajadores = generar_trabajadores(
        cantidad = TOTAL_TRABAJADORES
    )

    return crear_dataframe_trabajadores(
        trabajadores
    )


def generar_dataframe_accidentalidad_prueba():
    trabajadores = generar_trabajadores(
        cantidad = TOTAL_TRABAJADORES
    )

    rng = np.random.default_rng(SEED)

    accidentes = generar_accidentalidad_anual(
        trabajadores=trabajadores,
        fecha_inicio=date.fromisoformat(
            FECHA_INICIO_EMPRESA
        ),
        fecha_corte=date.fromisoformat(
            FECHA_CORTE
        ),
        rng=rng,
    )

    return crear_dataframe_accidentalidad(
        accidentes
    )


# ============================================================
# UTILIDADES
# ============================================================

def test_calcular_cantidad_respeta_las_reglas():
    assert calcular_cantidad(0, 0.02) == 0
    assert calcular_cantidad(100, 0) == 0
    assert calcular_cantidad(100, -0.1) == 0

    assert calcular_cantidad(100, 0.02) == 2
    assert calcular_cantidad(10, 0.02) == 1


def test_seleccionar_indices_no_supera_el_numero_de_registros():
    df = pd.DataFrame(
        {
            "valor": range(100)
        }
    )

    rng = np.random.default_rng(42)

    indices = seleccionar_indices(
        df=df,
        porcentaje=0.10,
        rng=rng,
    )

    assert len(indices) == 10
    assert len(set(indices)) == 10

    assert all(
        indice in df.index
        for indice in indices
    )


# ============================================================
# TRANSFORMACIONES INDIVIDUALES
# ============================================================

def test_introducir_espacios_no_modifica_dataframe_original():
    df = pd.DataFrame(
        {
            "ciudad": [
                "Bogotá",
                "Medellín",
                "Cali",
                "Barranquilla",
            ]
        }
    )

    original = df.copy(deep=True)

    rng = np.random.default_rng(42)

    resultado = introducir_espacios(
        df=df,
        columnas=["ciudad"],
        porcentaje=0.50,
        rng=rng,
    )

    pd.testing.assert_frame_equal(
        df,
        original,
    )

    assert resultado is not df


def test_introducir_espacios_agrega_espacios_externos():
    df = pd.DataFrame(
        {
            "ciudad": [
                "Bogotá",
                "Medellín",
                "Cali",
                "Barranquilla",
            ]
        }
    )

    rng = np.random.default_rng(42)

    resultado = introducir_espacios(
        df=df,
        columnas=["ciudad"],
        porcentaje=0.50,
        rng=rng,
    )

    valores_con_espacios = resultado[
        "ciudad"
    ].astype(str).str.contains(
        r"^\s|\s$",
        regex=True,
    )

    assert valores_con_espacios.any()


def test_introducir_variaciones_categoricas_no_genera_valores_no_textuales():
    df = pd.DataFrame(
        {
            "ciudad": [
                "Bogotá",
                "Medellín",
                "Cali",
                "Barranquilla",
            ]
        }
    )

    rng = np.random.default_rng(42)

    resultado = introducir_variaciones_categoricas(
        df=df,
        columnas=["ciudad"],
        porcentaje=0.50,
        rng=rng,
    )

    assert resultado["ciudad"].notna().all()
    assert resultado["ciudad"].map(
        lambda valor: isinstance(valor, str)
    ).all()


def test_introducir_nulos_genera_valores_nulos():
    df = pd.DataFrame(
        {
            "ciudad": [
                "Bogotá",
                "Medellín",
                "Cali",
                "Barranquilla",
            ]
        }
    )

    rng = np.random.default_rng(42)

    resultado = introducir_nulos(
        df=df,
        columnas=["ciudad"],
        porcentaje=0.50,
        rng=rng,
    )

    assert resultado["ciudad"].isna().any()


def test_introducir_duplicados_agrega_registros():
    df = pd.DataFrame(
        {
            "id": range(100),
            "valor": range(100),
        }
    )

    rng = np.random.default_rng(42)

    resultado = introducir_duplicados(
        df=df,
        porcentaje=0.10,
        rng=rng,
    )

    assert len(resultado) == 110

    assert resultado.duplicated(
        subset=["id", "valor"]
    ).sum() == 10


# ============================================================
# DATASET DIRTY — TRABAJADORES
# ============================================================

def test_crear_trabajadores_dirty_preserva_dataframe_original():
    df = generar_dataframe_trabajadores_prueba()

    original = df.copy(deep=True)

    rng = np.random.default_rng(42)

    dirty = crear_trabajadores_dirty(
        df=df,
        rng=rng,
    )

    pd.testing.assert_frame_equal(
        df,
        original,
    )

    assert dirty is not df


def test_crear_trabajadores_dirty_preserva_columnas():
    df = generar_dataframe_trabajadores_prueba()

    rng = np.random.default_rng(42)

    dirty = crear_trabajadores_dirty(
        df=df,
        rng=rng,
    )

    assert list(dirty.columns) == list(
        df.columns
    )


def test_crear_trabajadores_dirty_genera_duplicados():
    df = generar_dataframe_trabajadores_prueba()

    rng = np.random.default_rng(42)

    dirty = crear_trabajadores_dirty(
        df=df,
        rng=rng,
    )

    assert len(dirty) > len(df)

    assert dirty.duplicated().any()


# ============================================================
# DATASET DIRTY — ACCIDENTALIDAD
# ============================================================

def test_crear_accidentalidad_dirty_preserva_dataframe_original():
    df = generar_dataframe_accidentalidad_prueba()

    original = df.copy(deep=True)

    rng = np.random.default_rng(42)

    dirty = crear_accidentalidad_dirty(
        df=df,
        rng=rng,
    )

    pd.testing.assert_frame_equal(
        df,
        original,
    )

    assert dirty is not df


def test_crear_accidentalidad_dirty_preserva_columnas():
    df = generar_dataframe_accidentalidad_prueba()

    rng = np.random.default_rng(42)

    dirty = crear_accidentalidad_dirty(
        df=df,
        rng=rng,
    )

    assert list(dirty.columns) == list(
        df.columns
    )


def test_crear_accidentalidad_dirty_genera_duplicados():
    df = generar_dataframe_accidentalidad_prueba()

    rng = np.random.default_rng(42)

    dirty = crear_accidentalidad_dirty(
        df=df,
        rng=rng,
    )

    assert len(dirty) > len(df)

    assert dirty.duplicated().any()