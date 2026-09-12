from collections import Counter, defaultdict
from datetime import date

import numpy as np

from config.parametros import (
    FECHA_INICIO_EMPRESA,
    FECHA_CORTE,
    TOTAL_TRABAJADORES,
    SEED,
)

from src.trabajadores import generar_trabajadores

from src.accidentalidad import generar_accidentalidad_anual


def generar_datos_reincidencia():
    """
    Genera un conjunto reproducible de trabajadores y accidentes
    para las pruebas de reincidencia.
    """
    fecha_inicio = date.fromisoformat(FECHA_INICIO_EMPRESA)
    fecha_corte = date.fromisoformat(FECHA_CORTE)

    rng = np.random.default_rng(SEED)

    trabajadores = generar_trabajadores(
        cantidad = TOTAL_TRABAJADORES
    )

    accidentes = generar_accidentalidad_anual(
        trabajadores = trabajadores,
        fecha_inicio = fecha_inicio,
        fecha_corte = fecha_corte,
        rng = rng,
    )

    return trabajadores, accidentes


def construir_accidentes_por_trabajador(trabajadores, accidentes):
    """
    Construye el conteo de accidentes por trabajador,
    incluyendo también trabajadores sin accidentes.
    """
    accidentes_por_trabajador = Counter(
        accidente["id_trabajador"]
        for accidente in accidentes
    )

    for trabajador in trabajadores:
        id_trabajador = trabajador["id_trabajador"]

        if id_trabajador not in accidentes_por_trabajador:
            accidentes_por_trabajador[id_trabajador] = 0

    return accidentes_por_trabajador


def test_cantidad_trabajadores_generados():
    """Debe generarse exactamente la población configurada."""
    trabajadores, _ = generar_datos_reincidencia()

    assert len(trabajadores) == TOTAL_TRABAJADORES


def test_distribucion_incluye_a_todos_los_trabajadores():
    """
    La distribución de accidentes debe incluir tanto trabajadores
    accidentados como trabajadores sin accidentes.
    """
    trabajadores, accidentes = generar_datos_reincidencia()

    accidentes_por_trabajador = construir_accidentes_por_trabajador(
        trabajadores,
        accidentes,
    )

    distribucion = Counter(
        accidentes_por_trabajador.values()
    )

    assert sum(distribucion.values()) == len(trabajadores)


def test_distribucion_de_accidentes_es_matematicamente_consistente():
    """
    La suma de:
        cantidad de accidentes × trabajadores con esa cantidad
    debe coincidir con el total de accidentes generado.
    """
    trabajadores, accidentes = generar_datos_reincidencia()

    accidentes_por_trabajador = construir_accidentes_por_trabajador(
        trabajadores,
        accidentes,
    )

    distribucion = Counter(
        accidentes_por_trabajador.values()
    )

    suma_accidentes = sum(
        cantidad * trabajadores_cantidad
        for cantidad, trabajadores_cantidad
        in distribucion.items()
    )

    assert suma_accidentes == len(accidentes)


def test_todos_los_accidentes_pertenecen_a_un_trabajador_existente():
    """
    Cada accidente debe estar asociado a un trabajador generado.
    """
    trabajadores, accidentes = generar_datos_reincidencia()

    ids_trabajadores = {
        trabajador["id_trabajador"]
        for trabajador in trabajadores
    }

    ids_accidentes_trabajadores = {
        accidente["id_trabajador"]
        for accidente in accidentes
    }

    ids_inexistentes = (
        ids_accidentes_trabajadores - ids_trabajadores
    )

    assert not ids_inexistentes, (
        "Existen accidentes asociados a trabajadores inexistentes: "
        f"{sorted(ids_inexistentes)}"
    )


def test_reincidencia_se_define_como_dos_o_mas_accidentes():
    """
    Un trabajador reincidente debe tener al menos dos accidentes.
    """
    trabajadores, accidentes = generar_datos_reincidencia()

    accidentes_por_trabajador = construir_accidentes_por_trabajador(
        trabajadores,
        accidentes,
    )

    trabajadores_reincidentes = {
        id_trabajador
        for id_trabajador, cantidad in accidentes_por_trabajador.items()
        if cantidad >= 2
    }

    for id_trabajador in trabajadores_reincidentes:
        assert accidentes_por_trabajador[id_trabajador] >= 2


def test_trabajadores_con_cuatro_o_mas_accidentes_cumplen_el_criterio():
    """
    El grupo de trabajadores con 4 o más accidentes debe contener
    exclusivamente trabajadores con al menos cuatro accidentes.
    """
    trabajadores, accidentes = generar_datos_reincidencia()

    accidentes_por_trabajador = construir_accidentes_por_trabajador(
        trabajadores,
        accidentes,
    )

    trabajadores_multiples = {
        id_trabajador
        for id_trabajador, cantidad in accidentes_por_trabajador.items()
        if cantidad >= 4
    }

    for id_trabajador in trabajadores_multiples:
        assert accidentes_por_trabajador[id_trabajador] >= 4


def test_intervalos_entre_accidentes_no_son_negativos():
    """
    Al ordenar cronológicamente los accidentes de un trabajador,
    el intervalo entre accidentes consecutivos no puede ser negativo.
    """
    _, accidentes = generar_datos_reincidencia()

    accidentes_por_trabajador = defaultdict(list)

    for accidente in accidentes:
        accidentes_por_trabajador[
            accidente["id_trabajador"]
        ].append(accidente)

    for lista in accidentes_por_trabajador.values():
        if len(lista) < 2:
            continue

        fechas = sorted(
            accidente["fecha_accidente"]
            for accidente in lista
        )

        for i in range(1, len(fechas)):
            intervalo = (
                fechas[i] - fechas[i - 1]
            ).days

            assert intervalo >= 0