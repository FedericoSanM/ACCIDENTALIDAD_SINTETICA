import numpy as np
import pytest

from datetime import date

from src.trabajadores import generar_trabajadores

from src.accidentalidad import (
    generar_accidentalidad_anual,
    validar_exposicion_accidentes,
)

from src.catalogos import (
        COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE,
        MECANISMOS,
        COMPATIBILIDAD_MECANISMO_AGENTE,
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO,
        DIAGNOSTICOS,
        CRITERIOS_GRAVEDAD_RES1401,
    )

from config.parametros import (
    FECHA_INICIO_EMPRESA,
    FECHA_CORTE,
    TOTAL_TRABAJADORES,
    SEED,
)


# ============================================================
# DATOS DE INTEGRACIÓN
# ============================================================

@pytest.fixture(scope="module")
def datos_integracion():
    """
    Genera una única población y una única accidentalidad
    para todas las pruebas de integración.
    """

    trabajadores = generar_trabajadores(
        cantidad=TOTAL_TRABAJADORES
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

    return trabajadores, accidentes


# ============================================================
# INTEGRACIÓN GENERAL
# ============================================================

def test_integracion_genera_la_poblacion_esperada(
    datos_integracion,
):
    trabajadores, _ = datos_integracion

    assert len(trabajadores) == TOTAL_TRABAJADORES


def test_integracion_accidentes_corresponden_a_trabajadores_existentes(
    datos_integracion,
):
    trabajadores, accidentes = datos_integracion

    ids_trabajadores = {
        trabajador["id_trabajador"]
        for trabajador in trabajadores
    }

    ids_accidentes = {
        accidente["id_trabajador"]
        for accidente in accidentes
    }

    assert ids_accidentes.issubset(
        ids_trabajadores
    )


def test_integracion_ids_accidentes_son_unicos(
    datos_integracion,
):
    _, accidentes = datos_integracion

    ids_accidentes = [
        accidente["id_accidente"]
        for accidente in accidentes
    ]

    assert len(ids_accidentes) == len(
        set(ids_accidentes)
    )


# ============================================================
# COHERENCIA DEL ACCIDENTE
# ============================================================

def test_integracion_caracteristicas_accidente_son_coherentes(
    datos_integracion,
):
    trabajadores, accidentes = datos_integracion

    trabajadores_por_id = {
        trabajador["id_trabajador"]: trabajador
        for trabajador in trabajadores
    }

    assert accidentes, (
        "No se generaron accidentes para realizar "
        "la validación de integración."
    )

    for accidente in accidentes:
        trabajador = trabajadores_por_id[
            accidente["id_trabajador"]
        ]

        cargo = trabajador["cargo"]
        tipo_accidente = accidente["tipo_accidente"]
        mecanismo = accidente["mecanismo"]
        agente = accidente["agente"]
        codigo = accidente["codigo_diagnostico"]

        tipos_permitidos = {
            tipo
            for tipo, _ in COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE[
                cargo
            ]
        }

        assert tipo_accidente in tipos_permitidos

        assert mecanismo in MECANISMOS[
            tipo_accidente
        ]

        assert agente in COMPATIBILIDAD_MECANISMO_AGENTE[
            mecanismo
        ]

        diagnosticos_permitidos = {
            codigo_diagnostico
            for codigo_diagnostico, _, _ in (
                COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO[
                    tipo_accidente
                ][mecanismo]
            )
        }

        assert codigo in diagnosticos_permitidos

        diagnostico = DIAGNOSTICOS[codigo]

        assert accidente["diagnostico"] == (
            diagnostico["descripcion"]
        )

        assert accidente["tipo_lesion"] == (
            diagnostico["tipo_lesion"]
        )

        assert accidente["parte_cuerpo"] == (
            diagnostico["parte_cuerpo"]
        )



# ============================================================
# EXPOSICIÓN DEL TRABAJADOR
# ============================================================

def test_integracion_accidentes_ocurren_durante_la_exposicion(
    datos_integracion,
):
    trabajadores, accidentes = datos_integracion

    errores = validar_exposicion_accidentes(
        trabajadores,
        accidentes,
    )

    assert not errores, (
        "Se encontraron accidentes fuera "
        "del período de exposición del trabajador:\n"
        + "\n".join(
            f"- {error}"
            for error in errores
        )
    )


# ============================================================
# INCAPACIDAD
# ============================================================

def test_integracion_incapacidades_son_coherentes(
    datos_integracion,
):
    trabajadores, accidentes = datos_integracion

    trabajadores_por_id = {
        trabajador["id_trabajador"]: trabajador
        for trabajador in trabajadores
    }

    assert accidentes, (
        "No se generaron accidentes para realizar "
        "la validación de incapacidades."
    )

    for accidente in accidentes:
        id_trabajador = accidente["id_trabajador"]
        fecha_accidente = accidente["fecha_accidente"]
        dias_incapacidad = accidente["dias_incapacidad"]

        trabajador = trabajadores_por_id[id_trabajador]

        # La incapacidad debe ser positiva.
        assert dias_incapacidad >= 1

        # No puede superar el máximo configurado.
        assert dias_incapacidad <= 180

        # Si existe fecha de retiro, la incapacidad
        # no puede extenderse más allá del retiro.
        fecha_retiro = trabajador["fecha_retiro"]

        if fecha_retiro is not None:
            dias_disponibles = (
                fecha_retiro - fecha_accidente
            ).days

            assert dias_incapacidad <= dias_disponibles


# ============================================================
# GRAVEDAD
# ============================================================

def test_integracion_gravedad_es_coherente_con_diagnostico(
    datos_integracion,
):
    _, accidentes = datos_integracion

    assert accidentes, (
        "No se generaron accidentes para realizar "
        "la validación de gravedad."
    )

    for accidente in accidentes:
        codigo_diagnostico = (
            accidente["codigo_diagnostico"]
        )

        gravedad = accidente["gravedad_accidente"]

        # La clasificación debe pertenecer a los
        # valores definidos por el modelo.
        assert gravedad in {
            "Leve",
            "Grave",
        }

        criterio = CRITERIOS_GRAVEDAD_RES1401.get(
            codigo_diagnostico
        )

        # ---------------------------------------------------------
        # SIN CRITERIO NORMATIVO
        # ---------------------------------------------------------

        if criterio is None:
            assert gravedad == "Leve"
            continue

        # ---------------------------------------------------------
        # CRITERIO DIRECTO
        # ---------------------------------------------------------

        if criterio["tipo"] == "DIRECTO":
            assert gravedad == "Grave"

        # ---------------------------------------------------------
        # CRITERIO CONDICIONAL
        # ---------------------------------------------------------

        elif criterio["tipo"] == "CONDICIONAL":
            assert gravedad in {
                "Leve",
                "Grave",
            }

        else:
            raise AssertionError(
                f"Tipo de criterio no reconocido: "
                f"{criterio['tipo']}"
            )

# ============================================================
# ESQUEMA MATRIZ ACCIDENTALIDAD
# ============================================================

def test_integracion_matriz_accidentalidad_tiene_esquema_publico(
    datos_integracion,
):
    _, accidentes = datos_integracion

    campos_publicos_esperados = {
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
    }

    campos_internos_no_exportables = {
        "accidente_grave",
        "criterio_gravedad",
        "escenario_incapacidad",
        "dias_incapacidad_originales",
        "usar_peso_ventana",
    }

    assert accidentes, (
        "No se generaron accidentes para validar "
        "el esquema público."
    )

    for accidente in accidentes:
        assert set(accidente.keys()) == campos_publicos_esperados

        assert not (
            set(accidente.keys())
            & campos_internos_no_exportables
        )