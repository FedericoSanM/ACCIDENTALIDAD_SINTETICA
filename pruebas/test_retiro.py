from datetime import date

import pytest

from src.accidentalidad import (
    ajustar_dias_por_fecha_retiro,
    determinar_uso_peso_ventana,
)


def test_trabajador_activo_no_recorta_incapacidad():
    """
    Si el trabajador no tiene fecha de retiro, los días
    de incapacidad deben conservarse sin modificación.
    """

    fecha_accidente = date(2025, 5, 10)
    dias_originales = 30

    dias_finales = ajustar_dias_por_fecha_retiro(
        fecha_accidente,
        None,
        dias_originales,
    )

    assert dias_finales == dias_originales


def test_incapacidad_cabe_antes_del_retiro():
    """
    Si la incapacidad completa termina antes del retiro,
    no debe realizarse ningún recorte.
    """

    fecha_accidente = date(2025, 5, 1)
    fecha_retiro = date(2025, 6, 1)

    dias_originales = 20

    dias_finales = ajustar_dias_por_fecha_retiro(
        fecha_accidente,
        fecha_retiro,
        dias_originales,
    )

    assert dias_finales == dias_originales


def test_incapacidad_se_recorta_al_retiro():
    """
    Si los días originales superan el tiempo disponible
    hasta el retiro, deben recortarse exactamente al
    número de días disponibles.
    """

    fecha_accidente = date(2025, 5, 1)
    fecha_retiro = date(2025, 5, 16)

    dias_originales = 30

    dias_finales = ajustar_dias_por_fecha_retiro(
        fecha_accidente,
        fecha_retiro,
        dias_originales,
    )

    assert dias_finales == 15


def test_incapacidad_no_puede_superar_fecha_retiro():
    """
    Verifica que la incapacidad final nunca supere
    los días disponibles hasta la fecha de retiro.
    """

    fecha_accidente = date(2025, 5, 1)
    fecha_retiro = date(2025, 5, 10)

    dias_originales = 180

    dias_finales = ajustar_dias_por_fecha_retiro(
        fecha_accidente,
        fecha_retiro,
        dias_originales,
    )

    dias_disponibles = (
        fecha_retiro - fecha_accidente
    ).days

    assert dias_finales <= dias_disponibles


def test_fecha_retiro_no_puede_ser_anterior_o_igual():
    """
    La fecha de retiro debe ser posterior a la fecha
    del accidente.
    """

    fecha_accidente = date(2025, 5, 10)

    fechas_invalidas = [
        date(2025, 5, 10),
        date(2025, 5, 9),
    ]

    for fecha_retiro in fechas_invalidas:

        with pytest.raises(ValueError):
            ajustar_dias_por_fecha_retiro(
                fecha_accidente,
                fecha_retiro,
                10,
            )


def test_dias_incapacidad_deben_ser_mayores_o_iguales_a_uno():
    """
    No se permiten incapacidades de cero o menos días.
    """

    fecha_accidente = date(2025, 5, 1)
    fecha_retiro = date(2025, 6, 1)

    for dias in (0, -1, -10):

        with pytest.raises(ValueError):
            ajustar_dias_por_fecha_retiro(
                fecha_accidente,
                fecha_retiro,
                dias,
            )

def test_trabajador_activo_usa_peso_normal():
    """
    Un trabajador sin fecha de retiro debe utilizar
    la distribución NORMAL.
    """

    fecha_accidente = date(2025, 1, 1)

    resultado = determinar_uso_peso_ventana(
        fecha_accidente,
        None,
    )

    assert resultado is False


def test_accidente_fuera_de_ventana_usa_peso_normal():
    """
    Si faltan más de 180 días para el retiro,
    debe utilizarse la distribución NORMAL.
    """

    fecha_accidente = date(2025, 1, 1)
    fecha_retiro = date(2025, 7, 1)

    dias_hasta_retiro = (
        fecha_retiro - fecha_accidente
    ).days

    assert dias_hasta_retiro > 180

    resultado = determinar_uso_peso_ventana(
        fecha_accidente,
        fecha_retiro,
    )

    assert resultado is False


def test_exactamente_180_dias_usa_peso_ventana():
    """
    Exactamente 180 días antes del retiro pertenece
    a la ventana.
    """

    fecha_accidente = date(2025, 1, 1)
    fecha_retiro = date(2025, 6, 30)

    dias_hasta_retiro = (
        fecha_retiro - fecha_accidente
    ).days

    assert dias_hasta_retiro == 180

    resultado = determinar_uso_peso_ventana(
        fecha_accidente,
        fecha_retiro,
    )

    assert resultado is True


def test_dentro_de_ventana_usa_peso_ventana():
    """
    Un accidente ocurrido dentro de los 180 días
    anteriores al retiro debe utilizar VENTANA.
    """

    fecha_accidente = date(2025, 5, 1)
    fecha_retiro = date(2025, 6, 30)

    dias_hasta_retiro = (
        fecha_retiro - fecha_accidente
    ).days

    assert 0 < dias_hasta_retiro < 180

    resultado = determinar_uso_peso_ventana(
        fecha_accidente,
        fecha_retiro,
    )

    assert resultado is True


def test_un_dia_antes_del_retiro_usa_peso_ventana():
    """
    Un accidente ocurrido un día antes del retiro
    pertenece a la ventana.
    """

    fecha_accidente = date(2025, 6, 29)
    fecha_retiro = date(2025, 6, 30)

    resultado = determinar_uso_peso_ventana(
        fecha_accidente,
        fecha_retiro,
    )

    assert resultado is True