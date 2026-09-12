import numpy as np
from datetime import date

from src.trabajadores import (
    generar_trabajadores
)

from src.accidentalidad import (
    generar_accidentalidad_anual
)

from src.dataframes import (
    crear_dataframe_trabajadores,
    crear_dataframe_accidentalidad,
)

from src.exportacion import (
    exportar_matrices_excel,
)

from src.dirty import (
    crear_trabajadores_dirty,
    crear_accidentalidad_dirty,
)

from config.parametros import (
    FECHA_INICIO_EMPRESA,
    FECHA_CORTE,
    TOTAL_TRABAJADORES,
    SEED
)

from config.rutas import (
    CARPETA_SAMPLE,
    CARPETA_DIRTY,
    crear_carpetas_salida,
)

from src.analisis_anual import generar_informe_anual


fecha_inicio = date.fromisoformat(FECHA_INICIO_EMPRESA)

fecha_corte = date.fromisoformat(FECHA_CORTE)


def generar_matrices():

    rng = np.random.default_rng(SEED)

    # -----------------------------------------------------
    # 1. TRABAJADORES
    # -----------------------------------------------------

    trabajadores = generar_trabajadores(
        cantidad = TOTAL_TRABAJADORES
    )

    # -----------------------------------------------------
    # 2. ACCIDENTALIDAD
    # -----------------------------------------------------

    accidentalidad = generar_accidentalidad_anual(
        trabajadores = trabajadores,
        fecha_inicio = fecha_inicio,
        fecha_corte = fecha_corte,
        rng = rng,
    )

    return (
        trabajadores,
        accidentalidad
    )

if __name__ == "__main__":

    # =====================================================
    # GENERACIÓN CLEAN
    # =====================================================

    trabajadores, accidentalidad = (
        generar_matrices()
    )

    # =====================================================
    # DATAFRAMES CLEAN
    # =====================================================

    df_trabajadores = (
        crear_dataframe_trabajadores(
            trabajadores
        )
    )

    df_accidentalidad = (
        crear_dataframe_accidentalidad(
            accidentalidad
        )
    )

    # =====================================================
    # DATASETS DIRTY
    # =====================================================

    rng_dirty = np.random.default_rng(
        SEED + 1
    )

    df_trabajadores_dirty = (
        crear_trabajadores_dirty(
            df_trabajadores,
            rng_dirty,
        )
    )

    df_accidentalidad_dirty = (
        crear_accidentalidad_dirty(
            df_accidentalidad,
            rng_dirty,
        )
    )

    # =====================================================
    # EXPORTACIÓN CLEAN
    # =====================================================

    crear_carpetas_salida()

    exportar_matrices_excel(
        df_trabajadores,
        df_accidentalidad,
        CARPETA_SAMPLE / "trabajadores_sinteticos.xlsx",
        CARPETA_SAMPLE / "accidentalidad_sintetica.xlsx",
    )

    # =====================================================
    # EXPORTACIÓN DIRTY
    # =====================================================

    exportar_matrices_excel(
        df_trabajadores_dirty,
        df_accidentalidad_dirty,
        CARPETA_DIRTY / "trabajadores_dirty.xlsx",
        CARPETA_DIRTY / "accidentalidad_dirty.xlsx",
    )

    # =====================================================
    # RESUMEN
    # =====================================================

    print()
    print("=" * 60)
    print("GENERACIÓN DE DATASETS")
    print("=" * 60)

    print(
        f"Trabajadores CLEAN: "
        f"{df_trabajadores.shape[0]}"
    )

    print(
        f"Accidentalidad CLEAN: "
        f"{df_accidentalidad.shape[0]}"
    )

    print()

    print(
        f"Trabajadores DIRTY: "
        f"{df_trabajadores_dirty.shape[0]}"
    )

    print(
        f"Accidentalidad DIRTY: "
        f"{df_accidentalidad_dirty.shape[0]}"
    )

    print()
    print(
        "Datasets generados correctamente."
    )

    # =====================================================
    # GENERACIÓN INFORME
    # =====================================================

    print("Generando informe anual...")

    archivo_informe = generar_informe_anual(
        trabajadores = df_trabajadores,
        accidentes = df_accidentalidad,
    )

    print(
        f"✓ Informe anual generado: {archivo_informe}"
    )
