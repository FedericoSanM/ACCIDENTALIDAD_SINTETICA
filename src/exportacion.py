import pandas as pd


def exportar_matrices_excel(
    df_trabajadores,
    df_accidentalidad,
    ruta_trabajadores,
    ruta_accidentalidad,
):
    """
    Exporta las matrices de trabajadores y accidentalidad
    a archivos Excel y CSV independientes.
    """

    with pd.ExcelWriter(
        ruta_trabajadores,
        engine="openpyxl",
    ) as writer:

        df_trabajadores.to_excel(
            writer,
            sheet_name="Trabajadores",
            index=False,
        )

    with pd.ExcelWriter(
        ruta_accidentalidad,
        engine="openpyxl",
    ) as writer:

        df_accidentalidad.to_excel(
            writer,
            sheet_name="Accidentalidad",
            index=False,
        )

    ruta_trabajadores_csv = ruta_trabajadores.with_suffix(".csv")
    ruta_accidentalidad_csv = ruta_accidentalidad.with_suffix(".csv")

    df_trabajadores.to_csv(
        ruta_trabajadores_csv,
        index=False,
        encoding="utf-8-sig",
    )

    df_accidentalidad.to_csv(
        ruta_accidentalidad_csv,
        index=False,
        encoding="utf-8-sig",
    )