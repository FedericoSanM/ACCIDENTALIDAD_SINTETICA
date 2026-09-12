from unittest.mock import Mock

from src.catalogos import (
    DIAGNOSTICOS,
    CRITERIOS_GRAVEDAD_RES1401,
)

from config.parametros import (
    PROBABILIDAD_CRITERIO_GRAVEDAD_RES1401,
)

from src.accidentalidad import determinar_gravedad_accidente


def test_criterios_gravedad_tienen_estructura_valida():
    """
    Verifica la estructura de CRITERIOS_GRAVEDAD_RES1401.

    Cada criterio debe:
    - tener un tipo válido;
    - tener una descripción del criterio;
    - corresponder a un diagnóstico existente;
    - incluir atributo cuando sea CONDICIONAL.
    """

    errores = []

    tipos_validos = {
        "DIRECTO",
        "CONDICIONAL",
    }

    for codigo, criterio in CRITERIOS_GRAVEDAD_RES1401.items():

        if codigo not in DIAGNOSTICOS:
            errores.append(
                f"{codigo}: no existe en DIAGNOSTICOS."
            )

        if not isinstance(criterio, dict):
            errores.append(
                f"{codigo}: el criterio no es un diccionario."
            )
            continue

        tipo = criterio.get("tipo")

        if tipo not in tipos_validos:
            errores.append(
                f"{codigo}: tipo de criterio inválido: {tipo!r}."
            )

        if not criterio.get("criterio"):
            errores.append(
                f"{codigo}: falta la descripción del criterio."
            )

        if tipo == "CONDICIONAL" and not criterio.get("atributo"):
            errores.append(
                f"{codigo}: criterio CONDICIONAL sin atributo."
            )

    assert not errores, (
        "Se encontraron errores en "
        "CRITERIOS_GRAVEDAD_RES1401:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_diagnosticos_directos_siempre_son_graves():
    """
    Todo diagnóstico con criterio DIRECTO debe producir
    un accidente Grave independientemente del valor aleatorio.
    """

    diagnosticos_directos = [
        codigo
        for codigo, criterio in CRITERIOS_GRAVEDAD_RES1401.items()
        if criterio["tipo"] == "DIRECTO"
    ]

    assert diagnosticos_directos, (
        "No existen diagnósticos con criterio DIRECTO."
    )

    rng = Mock()
    rng.random.return_value = 0.999999

    errores = []

    for codigo in diagnosticos_directos:

        resultado = determinar_gravedad_accidente(
            codigo,
            rng,
        )

        if resultado["gravedad_accidente"] != "Grave":
            errores.append(
                f"{codigo}: se esperaba 'Grave', "
                f"se obtuvo {resultado['gravedad_accidente']!r}."
            )

        if resultado["accidente_grave"] is not True:
            errores.append(
                f"{codigo}: accidente_grave debe ser True."
            )

        criterio_esperado = (
            CRITERIOS_GRAVEDAD_RES1401[codigo]["criterio"]
        )

        if resultado["criterio_gravedad"] != criterio_esperado:
            errores.append(
                f"{codigo}: criterio_gravedad incorrecto."
            )

    assert not errores, (
        "Se encontraron errores en los criterios DIRECTOS:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_diagnosticos_sin_criterio_son_leves():
    """
    Un diagnóstico que no esté configurado en
    CRITERIOS_GRAVEDAD_RES1401 debe clasificarse como Leve.
    """

    diagnosticos_sin_criterio = (
        set(DIAGNOSTICOS)
        - set(CRITERIOS_GRAVEDAD_RES1401)
    )

    assert diagnosticos_sin_criterio, (
        "Todos los diagnósticos tienen criterio de gravedad. "
        "La prueba necesita al menos uno sin criterio."
    )

    rng = Mock()
    rng.random.return_value = 0.0

    errores = []

    for codigo in sorted(diagnosticos_sin_criterio):

        resultado = determinar_gravedad_accidente(
            codigo,
            rng,
        )

        if resultado["gravedad_accidente"] != "Leve":
            errores.append(
                f"{codigo}: se esperaba 'Leve', "
                f"se obtuvo {resultado['gravedad_accidente']!r}."
            )

        if resultado["accidente_grave"] is not False:
            errores.append(
                f"{codigo}: accidente_grave debe ser False."
            )

        if resultado["criterio_gravedad"] != "No aplica":
            errores.append(
                f"{codigo}: criterio_gravedad debe ser "
                "'No aplica'."
            )

    assert not errores, (
        "Se encontraron errores en diagnósticos "
        "sin criterio de gravedad:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_criterios_condicionales_pueden_ser_graves():
    """
    Un criterio CONDICIONAL debe producir Grave cuando
    el valor aleatorio está por debajo de la probabilidad
    configurada.

    Se utiliza random() = 0.0, que debe cumplir cualquier
    probabilidad mayor que cero.
    """

    diagnosticos_condicionales = [
        codigo
        for codigo, criterio in CRITERIOS_GRAVEDAD_RES1401.items()
        if criterio["tipo"] == "CONDICIONAL"
    ]

    assert diagnosticos_condicionales, (
        "No existen diagnósticos con criterio CONDICIONAL."
    )

    assert PROBABILIDAD_CRITERIO_GRAVEDAD_RES1401 > 0

    rng = Mock()
    rng.random.return_value = 0.0

    errores = []

    for codigo in diagnosticos_condicionales:

        resultado = determinar_gravedad_accidente(
            codigo,
            rng,
        )

        if resultado["gravedad_accidente"] != "Grave":
            errores.append(
                f"{codigo}: se esperaba 'Grave' "
                "con random() = 0.0."
            )

        if resultado["accidente_grave"] is not True:
            errores.append(
                f"{codigo}: accidente_grave debe ser True."
            )

        criterio_esperado = (
            CRITERIOS_GRAVEDAD_RES1401[codigo]["criterio"]
        )

        if resultado["criterio_gravedad"] != criterio_esperado:
            errores.append(
                f"{codigo}: criterio_gravedad incorrecto."
            )

    assert not errores, (
        "Se encontraron errores en criterios CONDICIONALES "
        "cuando la condición se cumple:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_criterios_condicionales_pueden_ser_leves():
    """
    Un criterio CONDICIONAL debe producir Leve cuando
    random() está por encima de la probabilidad configurada.
    """

    diagnosticos_condicionales = [
        codigo
        for codigo, criterio in CRITERIOS_GRAVEDAD_RES1401.items()
        if criterio["tipo"] == "CONDICIONAL"
    ]

    assert diagnosticos_condicionales

    assert PROBABILIDAD_CRITERIO_GRAVEDAD_RES1401 < 1

    rng = Mock()
    rng.random.return_value = 1.0

    errores = []

    for codigo in diagnosticos_condicionales:

        resultado = determinar_gravedad_accidente(
            codigo,
            rng,
        )

        if resultado["gravedad_accidente"] != "Leve":
            errores.append(
                f"{codigo}: se esperaba 'Leve' "
                "con random() = 1.0."
            )

        if resultado["accidente_grave"] is not False:
            errores.append(
                f"{codigo}: accidente_grave debe ser False."
            )

        if resultado["criterio_gravedad"] != "No aplica":
            errores.append(
                f"{codigo}: criterio_gravedad debe ser "
                "'No aplica'."
            )

    assert not errores, (
        "Se encontraron errores en criterios CONDICIONALES "
        "cuando la condición no se cumple:\n"
        + "\n".join(f"- {error}" for error in errores)
    )