from src.accidentalidad import validar_catalogos_accidentalidad


def test_catalogos_accidentalidad():
    """
    Verifica la integridad de los catálogos utilizados
    por el generador de accidentalidad.

    La prueba falla automáticamente si la función de
    validación devuelve uno o más errores.
    """

    errores = validar_catalogos_accidentalidad()

    assert not errores, (
        "Se encontraron errores en los catálogos de accidentalidad:\n"
        + "\n".join(f"- {error}" for error in errores)
    )