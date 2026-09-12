from src.catalogos import DIAGNOSTICOS


def test_cantidad_diagnosticos():
    """Verifica que el catálogo contenga exactamente 92 diagnósticos."""

    cantidad = len(DIAGNOSTICOS)

    assert cantidad == 92, (
        f"Se esperaban 92 diagnósticos y se encontraron {cantidad}."
    )


def test_campos_obligatorios_diagnosticos():
    """Verifica que cada diagnóstico tenga todos los campos obligatorios."""

    campos_obligatorios = {
        "descripcion",
        "severidad_clinica",
        "tipo_lesion",
        "parte_cuerpo",
        "escenarios",
    }

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        faltantes = campos_obligatorios - set(diagnostico.keys())

        if faltantes:
            errores.append(
                f"{codigo}: faltan campos {sorted(faltantes)}"
            )

    assert not errores, (
        "Se encontraron diagnósticos con campos obligatorios faltantes:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_tres_escenarios_por_diagnostico():
    """Verifica que cada diagnóstico tenga exactamente tres escenarios."""

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        escenarios = diagnostico["escenarios"]

        if len(escenarios) != 3:
            errores.append(
                f"{codigo}: tiene {len(escenarios)} escenarios; "
                "deben ser exactamente 3."
            )

    assert not errores, (
        "Se encontraron diagnósticos con una cantidad incorrecta "
        "de escenarios:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_campos_obligatorios_escenarios():
    """Verifica los campos obligatorios de cada escenario."""

    campos_escenario = {
        "nivel",
        "dias_min",
        "dias_max",
        "peso_normal",
        "peso_ventana",
    }

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        for escenario in diagnostico["escenarios"]:

            faltantes = campos_escenario - set(escenario.keys())

            if faltantes:
                errores.append(
                    f"{codigo}: escenario con campos faltantes "
                    f"{sorted(faltantes)}"
                )

    assert not errores, (
        "Se encontraron escenarios con campos obligatorios faltantes:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_rangos_dias_escenarios():
    """Verifica que los rangos de días estén entre 1 y 180."""

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        for escenario in diagnostico["escenarios"]:

            dias_min = escenario["dias_min"]
            dias_max = escenario["dias_max"]
            nivel = escenario["nivel"]

            if dias_min < 1:
                errores.append(
                    f"{codigo} / {nivel}: "
                    f"dias_min={dias_min}; debe ser >= 1."
                )

            if dias_max > 180:
                errores.append(
                    f"{codigo} / {nivel}: "
                    f"dias_max={dias_max}; debe ser <= 180."
                )

            if dias_min > dias_max:
                errores.append(
                    f"{codigo} / {nivel}: "
                    f"dias_min ({dias_min}) > dias_max ({dias_max})."
                )

    assert not errores, (
        "Se encontraron rangos de días inválidos:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_pesos_normal():
    """Verifica que los pesos NORMAL de cada diagnóstico sumen 1."""

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        suma = sum(
            escenario["peso_normal"]
            for escenario in diagnostico["escenarios"]
        )

        if not abs(suma - 1.0) < 0.000001:
            errores.append(
                f"{codigo}: pesos NORMAL suman "
                f"{suma:.6f}; deben sumar 1.0."
            )

    assert not errores, (
        "Se encontraron pesos NORMAL inválidos:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_pesos_ventana():
    """Verifica que los pesos VENTANA de cada diagnóstico sumen 1."""

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        suma = sum(
            escenario["peso_ventana"]
            for escenario in diagnostico["escenarios"]
        )

        if not abs(suma - 1.0) < 0.000001:
            errores.append(
                f"{codigo}: pesos VENTANA suman "
                f"{suma:.6f}; deben sumar 1.0."
            )

    assert not errores, (
        "Se encontraron pesos VENTANA inválidos:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_pesos_no_negativos():
    """Verifica que ningún peso de escenario sea negativo."""

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        for escenario in diagnostico["escenarios"]:

            nivel = escenario["nivel"]
            peso_normal = escenario["peso_normal"]
            peso_ventana = escenario["peso_ventana"]

            if peso_normal < 0:
                errores.append(
                    f"{codigo} / {nivel}: peso_normal negativo."
                )

            if peso_ventana < 0:
                errores.append(
                    f"{codigo} / {nivel}: peso_ventana negativo."
                )

    assert not errores, (
        "Se encontraron pesos negativos:\n"
        + "\n".join(f"- {error}" for error in errores)
    )


def test_escenarios_sin_duplicados():
    """Verifica que cada diagnóstico tenga niveles de escenario únicos."""

    errores = []

    for codigo, diagnostico in DIAGNOSTICOS.items():

        niveles = [
            escenario["nivel"]
            for escenario in diagnostico["escenarios"]
        ]

        if len(niveles) != len(set(niveles)):
            errores.append(
                f"{codigo}: existen escenarios duplicados."
            )

    assert not errores, (
        "Se encontraron diagnósticos con escenarios duplicados:\n"
        + "\n".join(f"- {error}" for error in errores)
    )