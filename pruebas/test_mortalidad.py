from unittest.mock import Mock

from src.accidentalidad import determinar_accidente_mortal

from src.catalogos import (
    COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD,
    DIAGNOSTICOS,
)


def test_catalogo_mortalidad_tiene_probabilidades_validas():
    """Cada diagnóstico configurado debe tener una probabilidad válida."""
    assert COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD

    for codigo, probabilidad in COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD.items():
        assert isinstance(codigo, str)
        assert isinstance(probabilidad, (int, float))
        assert 0 <= probabilidad <= 1


def test_diagnosticos_mortalidad_existen_en_catalogo_diagnosticos():
    """Todo diagnóstico con probabilidad de mortalidad debe existir en DIAGNOSTICOS."""

    for codigo in COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD:
        assert codigo in DIAGNOSTICOS, (
            f"El diagnóstico {codigo} tiene probabilidad de mortalidad "
            "pero no existe en DIAGNOSTICOS."
        )


def test_accidente_no_grave_nunca_es_mortal():
    """
    La mortalidad depende primero de que el accidente sea grave.
    Un accidente no grave nunca puede clasificarse como mortal.
    """
    rng = Mock()
    rng.random.return_value = 0.0

    for codigo in COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD:
        resultado = determinar_accidente_mortal(
            codigo_diagnostico=codigo,
            accidente_grave=False,
            rng=rng,
        )

        assert resultado is False


def test_diagnostico_configurado_puede_ser_mortal():
    """
    Si el accidente es grave y el número aleatorio cae dentro
    de la probabilidad configurada, debe clasificarse como mortal.
    """
    for codigo, probabilidad in COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD.items():
        rng = Mock()
        rng.random.return_value = 0.0

        resultado = determinar_accidente_mortal(
            codigo_diagnostico=codigo,
            accidente_grave=True,
            rng=rng,
        )

        assert resultado is True, (
            f"{codigo}: con random=0.0 y probabilidad={probabilidad}, "
            "el accidente debería ser mortal."
        )


def test_diagnostico_configurado_puede_no_ser_mortal():
    """
    Si el número aleatorio supera la probabilidad configurada,
    un accidente grave debe resultar no mortal.
    """
    for codigo, probabilidad in COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD.items():
        rng = Mock()
        rng.random.return_value = 1.0

        resultado = determinar_accidente_mortal(
            codigo_diagnostico=codigo,
            accidente_grave=True,
            rng=rng,
        )

        assert resultado is False, (
            f"{codigo}: con random=1.0 y probabilidad={probabilidad}, "
            "el accidente no debería ser mortal."
        )


def test_diagnostico_sin_probabilidad_de_mortalidad_no_es_mortal():
    """
    Un diagnóstico que no está configurado en el catálogo de mortalidad
    tiene probabilidad 0 y, por tanto, no puede producir mortalidad.
    """

    diagnosticos_sin_mortalidad = (
        set(DIAGNOSTICOS) - set(COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD)
    )

    rng = Mock()
    rng.random.return_value = 0.0

    for codigo in diagnosticos_sin_mortalidad:
        resultado = determinar_accidente_mortal(
            codigo_diagnostico=codigo,
            accidente_grave=True,
            rng=rng,
        )

        assert resultado is False, (
            f"{codigo}: no tiene probabilidad configurada de mortalidad."
        )