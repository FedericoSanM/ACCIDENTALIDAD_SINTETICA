import numpy as np

from src.catalogos import DIAGNOSTICOS
from src.accidentalidad import (
    seleccionar_escenario_incapacidad,
    generar_dias_incapacidad,
)


CAMPOS_ESCENARIO = {
    "nivel",
    "dias_min",
    "dias_max",
    "peso_normal",
    "peso_ventana",
}


NIVELES_VALIDOS_POR_SEVERIDAD = {
    "muy_baja": {
        "muy_baja",
        "baja",
        "moderada",
    },
    "baja": {
        "muy_baja",
        "baja",
        "moderada",
    },
    "moderada": {
        "baja",
        "moderada",
        "alta",
    },
    "alta": {
        "moderada",
        "alta",
        "muy_alta",
    },
    "muy_alta": {
        "moderada",
        "alta",
        "muy_alta",
    },
}


def test_seleccion_escenario_normal_y_ventana():
    """
    Verifica que todos los diagnósticos puedan seleccionar
    un escenario tanto en condición NORMAL como VENTANA.
    """

    errores = []
    rng = np.random.default_rng(12345)

    for codigo, diagnostico in DIAGNOSTICOS.items():

        escenarios_configurados = diagnostico["escenarios"]
        niveles_configurados = {
            escenario["nivel"]
            for escenario in escenarios_configurados
        }

        for usar_ventana in (False, True):

            try:
                escenario = seleccionar_escenario_incapacidad(
                    codigo,
                    rng,
                    usar_ventana,
                )

                if not isinstance(escenario, dict):
                    errores.append(
                        f"{codigo} / "
                        f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                        "el resultado no es un diccionario."
                    )
                    continue

                faltantes = (
                    CAMPOS_ESCENARIO
                    - set(escenario.keys())
                )

                if faltantes:
                    errores.append(
                        f"{codigo} / "
                        f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                        f"faltan campos {sorted(faltantes)}."
                    )

                    continue

                if escenario["nivel"] not in niveles_configurados:
                    errores.append(
                        f"{codigo} / "
                        f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                        f"nivel '{escenario['nivel']}' "
                        "no pertenece a los escenarios configurados."
                    )

            except Exception as error:
                errores.append(
                    f"{codigo} / "
                    f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                    f"{type(error).__name__}: {error}"
                )

    assert not errores, (
        "Se encontraron errores en la selección de escenarios:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_severidad_clinica_y_niveles_escenario():
    """
    Verifica que los escenarios configurados para cada diagnóstico
    sean compatibles con su severidad clínica.
    """

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        severidad = diagnostico.get("severidad_clinica")

        permitidos = NIVELES_VALIDOS_POR_SEVERIDAD.get(
            severidad
        )

        if permitidos is None:
            errores.append(
                f"{codigo}: severidad_clinica inválida "
                f"'{severidad}'."
            )
            continue

        for escenario in diagnostico["escenarios"]:

            nivel = escenario["nivel"]

            if nivel not in permitidos:
                errores.append(
                    f"{codigo}: escenario '{nivel}' "
                    f"no corresponde a severidad clínica "
                    f"'{severidad}'."
                )

    assert not errores, (
        "Se encontraron incompatibilidades entre severidad "
        "clínica y escenarios:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_rangos_de_dias_de_escenarios():
    """
    Verifica que los rangos de días de todos los escenarios
    sean válidos para la generación de incapacidad.
    """

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        for escenario in diagnostico["escenarios"]:

            nivel = escenario["nivel"]
            dias_min = escenario["dias_min"]
            dias_max = escenario["dias_max"]

            if not isinstance(dias_min, int):
                errores.append(
                    f"{codigo} / {nivel}: "
                    "dias_min no es entero."
                )

            if not isinstance(dias_max, int):
                errores.append(
                    f"{codigo} / {nivel}: "
                    "dias_max no es entero."
                )

            if (
                isinstance(dias_min, int)
                and isinstance(dias_max, int)
            ):
                if dias_min < 1:
                    errores.append(
                        f"{codigo} / {nivel}: "
                        f"dias_min={dias_min}; "
                        "debe ser >= 1."
                    )

                if dias_max < dias_min:
                    errores.append(
                        f"{codigo} / {nivel}: "
                        f"dias_max={dias_max} < "
                        f"dias_min={dias_min}."
                    )

                if dias_max > 180:
                    errores.append(
                        f"{codigo} / {nivel}: "
                        f"dias_max={dias_max}; "
                        "debe ser <= 180."
                    )

    assert not errores, (
        "Se encontraron rangos de días inválidos:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_generacion_dias_incapacidad_normal_y_ventana():
    """
    Verifica que generar_dias_incapacidad() produzca un valor
    dentro del rango del escenario seleccionado.

    Se prueban los 92 diagnósticos en NORMAL y VENTANA.
    """

    errores = []
    rng = np.random.default_rng(12345)

    for codigo in DIAGNOSTICOS:

        for usar_ventana in (False, True):

            try:
                escenario = seleccionar_escenario_incapacidad(
                    codigo,
                    rng,
                    usar_ventana,
                )

                dias = generar_dias_incapacidad(
                    escenario,
                    rng,
                )

                dias_min = escenario["dias_min"]
                dias_max = escenario["dias_max"]

                if not isinstance(dias, (int, np.integer)):
                    errores.append(
                        f"{codigo} / "
                        f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                        f"días generados no son enteros: {dias!r}."
                    )

                    continue

                if not (
                    dias_min
                    <= dias
                    <= dias_max
                ):
                    errores.append(
                        f"{codigo} / "
                        f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                        f"{dias} días fuera del rango "
                        f"{dias_min}-{dias_max}."
                    )

            except Exception as error:
                errores.append(
                    f"{codigo} / "
                    f"{'VENTANA' if usar_ventana else 'NORMAL'}: "
                    f"{type(error).__name__}: {error}"
                )

    assert not errores, (
        "Se encontraron errores en la generación "
        "de días de incapacidad:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_pesos_de_escenarios_en_rango():
    """
    Verifica que los pesos utilizados por la selección de
    escenarios estén entre 0 y 1.
    """

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        for escenario in diagnostico["escenarios"]:

            nivel = escenario["nivel"]
            peso_normal = escenario["peso_normal"]
            peso_ventana = escenario["peso_ventana"]

            if not 0 <= peso_normal <= 1:
                errores.append(
                    f"{codigo} / {nivel}: "
                    f"peso_normal={peso_normal} fuera de [0, 1]."
                )

            if not 0 <= peso_ventana <= 1:
                errores.append(
                    f"{codigo} / {nivel}: "
                    f"peso_ventana={peso_ventana} fuera de [0, 1]."
                )

    assert not errores, (
        "Se encontraron pesos de escenarios fuera de rango:\n"
        + "\n".join(f"- {error}" for error in errores)
    )