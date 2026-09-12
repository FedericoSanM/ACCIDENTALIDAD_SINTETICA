from src.catalogos import (
    CARGOS,
    AREAS_ACCIDENTE,
    DIAGNOSTICOS,
    COMPATIBILIDAD_CARGO_AREA_ACCIDENTE,
    COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO,
)

from src.accidentalidad import seleccionar_area_accidente


TOLERANCIA = 0.000001


def test_cobertura_cargos_area_accidente():
    """
    Verifica la relación CARGO → AREA_ACCIDENTE.

    Comprueba que:
    - todos los cargos tengan configuración;
    - no existan cargos inexistentes en la configuración;
    - las listas de áreas no estén vacías;
    - todas las áreas sean válidas;
    - no existan áreas repetidas.
    """

    cargos = set(CARGOS)
    areas_validas = set(AREAS_ACCIDENTE)
    cargos_configurados = set(
        COMPATIBILIDAD_CARGO_AREA_ACCIDENTE
    )

    errores = []

    # Cargos sin configuración
    cargos_sin_configuracion = (
        cargos - cargos_configurados
    )

    for cargo in sorted(cargos_sin_configuracion):
        errores.append(
            f"Cargo '{cargo}' no tiene áreas de accidente configuradas."
        )

    # Cargos inexistentes
    cargos_inexistentes = (
        cargos_configurados - cargos
    )

    for cargo in sorted(cargos_inexistentes):
        errores.append(
            f"Cargo '{cargo}' en "
            "COMPATIBILIDAD_CARGO_AREA_ACCIDENTE "
            "no existe en CARGOS."
        )

    # Listas vacías
    for cargo, areas in (
        COMPATIBILIDAD_CARGO_AREA_ACCIDENTE.items()
    ):
        if not areas:
            errores.append(
                f"Cargo '{cargo}' tiene una lista de áreas vacía."
            )

    # Áreas inexistentes
    for cargo, areas in (
        COMPATIBILIDAD_CARGO_AREA_ACCIDENTE.items()
    ):
        for area in areas:
            if area not in areas_validas:
                errores.append(
                    f"Cargo '{cargo}': área inexistente '{area}'."
                )

    # Áreas repetidas
    for cargo, areas in (
        COMPATIBILIDAD_CARGO_AREA_ACCIDENTE.items()
    ):
        if len(areas) != len(set(areas)):
            errores.append(
                f"Cargo '{cargo}' tiene áreas repetidas."
            )

    assert not errores, (
        "Se encontraron errores en la relación "
        "CARGO → AREA_ACCIDENTE:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_seleccionar_area_accidente():
    """
    Verifica funcionalmente que seleccionar_area_accidente()
    siempre devuelva un área válida para el cargo suministrado.
    """

    import random

    rng = random.Random(42)

    errores = []
    casos_funcionales = 0

    for cargo in sorted(CARGOS):

        areas_configuradas = (
            COMPATIBILIDAD_CARGO_AREA_ACCIDENTE.get(
                cargo,
                []
            )
        )

        if not areas_configuradas:
            continue

        for _ in range(10):

            try:
                area = seleccionar_area_accidente(
                    cargo,
                    rng,
                )

                casos_funcionales += 1

                if area is None:
                    errores.append(
                        f"Cargo '{cargo}': "
                        "seleccionar_area_accidente() "
                        "devolvió None."
                    )

                elif area not in areas_configuradas:
                    errores.append(
                        f"Cargo '{cargo}': "
                        "seleccionar_area_accidente() "
                        f"devolvió área inválida '{area}'."
                    )

            except Exception as error:
                errores.append(
                    f"Cargo '{cargo}': "
                    "error al seleccionar área: "
                    f"{type(error).__name__}: {error}"
                )

    assert casos_funcionales > 0, (
        "No se ejecutó ningún caso funcional de "
        "seleccionar_area_accidente()."
    )

    assert not errores, (
        "Se encontraron errores al seleccionar áreas:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_estructura_compatibilidad_mecanismo_diagnostico():
    """
    Verifica la estructura de:

    TIPO_ACCIDENTE
        → MECANISMO
        → DIAGNÓSTICOS

    Cada registro de diagnóstico debe contener:

    (codigo_diagnostico, peso_normal, peso_ventana)
    """

    errores = []

    for tipo_accidente, mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.items()
    ):

        if not mecanismos:
            errores.append(
                f"Tipo de accidente '{tipo_accidente}' "
                "no tiene mecanismos configurados."
            )
            continue

        for mecanismo, diagnosticos in mecanismos.items():

            if not diagnosticos:
                errores.append(
                    f"{tipo_accidente} → {mecanismo}: "
                    "no tiene diagnósticos."
                )
                continue

            for registro in diagnosticos:

                if len(registro) != 3:
                    errores.append(
                        f"{tipo_accidente} → {mecanismo}: "
                        f"registro inválido {registro}. "
                        "Debe contener código, peso_normal "
                        "y peso_ventana."
                    )

    assert not errores, (
        "Se encontraron errores estructurales en "
        "COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_diagnosticos_existentes_en_compatibilidades():
    """
    Verifica que todo diagnóstico utilizado por las
    compatibilidades exista en el catálogo DIAGNOSTICOS.
    """

    diagnosticos_configurados = set()
    errores = []

    for tipo_accidente, mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.items()
    ):

        for mecanismo, diagnosticos in mecanismos.items():

            for registro in diagnosticos:

                codigo = registro[0]
                diagnosticos_configurados.add(codigo)

                if codigo not in DIAGNOSTICOS:
                    errores.append(
                        f"{tipo_accidente} → {mecanismo}: "
                        f"diagnóstico '{codigo}' no existe "
                        "en DIAGNOSTICOS."
                    )

    assert not errores, (
        "Se encontraron diagnósticos inexistentes "
        "en las compatibilidades:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_alcanzabilidad_de_los_92_diagnosticos():
    """
    Verifica la cobertura estructural completa del catálogo
    de diagnósticos.

    Cada diagnóstico definido en DIAGNOSTICOS debe aparecer
    al menos una vez en COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.

    Esta prueba NO evalúa si el diagnóstico apareció en una
    simulación concreta. Evalúa exclusivamente que exista
    una ruta configurada que permita generarlo.
    """

    diagnosticos_catalogo = set(DIAGNOSTICOS)
    diagnosticos_configurados = set()

    for mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.values()
    ):

        for diagnosticos in mecanismos.values():

            for registro in diagnosticos:
                codigo = registro[0]
                diagnosticos_configurados.add(codigo)

    diagnosticos_no_alcanzables = (
        diagnosticos_catalogo
        - diagnosticos_configurados
    )

    assert not diagnosticos_no_alcanzables, (
        "Existen diagnósticos del catálogo sin ninguna "
        "ruta de generación configurada:\n"
        + "\n".join(
            f"- {codigo}"
            for codigo in sorted(diagnosticos_no_alcanzables)
        )
    )


def test_diagnosticos_sin_duplicados_por_mecanismo():
    """
    Verifica que un mismo diagnóstico no aparezca repetido
    dentro de un mismo mecanismo.
    """

    errores = []

    for tipo_accidente, mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.items()
    ):

        for mecanismo, diagnosticos in mecanismos.items():

            codigos = [
                registro[0]
                for registro in diagnosticos
            ]

            if len(codigos) != len(set(codigos)):
                errores.append(
                    f"{tipo_accidente} → {mecanismo}: "
                    "existen diagnósticos duplicados."
                )

    assert not errores, (
        "Se encontraron diagnósticos duplicados:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_pesos_mecanismos():
    """
    Verifica que los pesos NORMAL y VENTANA de cada mecanismo:

    - no sean negativos;
    - sumen 1.0 dentro de la tolerancia definida.
    """

    errores = []

    for tipo_accidente, mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.items()
    ):

        for mecanismo, diagnosticos in mecanismos.items():

            if not diagnosticos:
                continue

            pesos_normal = [
                float(registro[1])
                for registro in diagnosticos
            ]

            pesos_ventana = [
                float(registro[2])
                for registro in diagnosticos
            ]

            # Pesos NORMAL
            for codigo, peso in zip(
                [registro[0] for registro in diagnosticos],
                pesos_normal,
            ):

                if peso < 0:
                    errores.append(
                        f"{tipo_accidente} → {mecanismo} → "
                        f"{codigo}: "
                        f"peso_normal negativo ({peso})."
                    )

            # Pesos VENTANA
            for codigo, peso in zip(
                [registro[0] for registro in diagnosticos],
                pesos_ventana,
            ):

                if peso < 0:
                    errores.append(
                        f"{tipo_accidente} → {mecanismo} → "
                        f"{codigo}: "
                        f"peso_ventana negativo ({peso})."
                    )

            suma_normal = sum(pesos_normal)
            suma_ventana = sum(pesos_ventana)

            if abs(suma_normal - 1.0) > TOLERANCIA:
                errores.append(
                    f"{tipo_accidente} → {mecanismo}: "
                    f"peso_normal = {suma_normal:.6f}; "
                    "debe sumar 1.0."
                )

            if abs(suma_ventana - 1.0) > TOLERANCIA:
                errores.append(
                    f"{tipo_accidente} → {mecanismo}: "
                    f"peso_ventana = {suma_ventana:.6f}; "
                    "debe sumar 1.0."
                )

    assert not errores, (
        "Se encontraron errores en los pesos de los mecanismos:\n"
        + "\n".join(f"- {error}" for error in errores)
    )