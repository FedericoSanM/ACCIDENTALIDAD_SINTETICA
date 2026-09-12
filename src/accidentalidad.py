import numpy as np
from calendar import monthrange
from datetime import date
from src.trabajadores import contar_activos

from config.parametros import (
    ESTACIONALIDAD_MENSUAL,
    FECHA_CORTE,
    FECHA_INICIO_ANALISIS,
    FECHA_INICIO_EMPRESA,
    PROBABILIDAD_CRITERIO_GRAVEDAD_RES1401,
    SEED,
    TASA_ANUAL_ACCIDENTALIDAD,
    DIAS_MAXIMOS_INCAPACIDAD,
    INCREMENTO_SALARIAL_ANUAL,
)

from src.catalogos import (
    SALARIOS_BASE_2016,
    AGENTES_LESION,
    CARGOS,
    COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE,
    COMPATIBILIDAD_MECANISMO_AGENTE,
    COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO,
    COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD,
    COMPATIBILIDAD_CARGO_AREA_ACCIDENTE,
    CRITERIOS_GRAVEDAD_RES1401,
    DIAGNOSTICOS,
    MECANISMOS,
    PARTES_CUERPO,
    TIPOS_ACCIDENTE,
    TIPOS_LESION,
)


def crear_generador_aleatorio():
    """Crea un generador NumPy reproducible."""

    return np.random.default_rng(SEED)


def construir_salarios_por_cargo_anio(
    anio_inicial,
    anio_final,
    incremento_anual=0.06,
):
    """
    Construye el catálogo histórico de salarios por
    cargo y año.

    Cada salario parte del valor base configurado para
    2016 y aumenta de forma compuesta según el porcentaje
    anual establecido.
    """

    salarios = {}

    for cargo, salario_base in (
        SALARIOS_BASE_2016.items()
    ):

        for anio in range(
            anio_inicial,
            anio_final + 1,
        ):

            anios_transcurridos = (
                anio - 2016
            )

            salario = (
                salario_base
                * (1 + incremento_anual)
                ** anios_transcurridos
            )

            salarios[
                (cargo, anio)
            ] = round(salario)

    return salarios


SALARIOS_POR_CARGO_ANIO = (
    construir_salarios_por_cargo_anio(
        anio_inicial = date.fromisoformat(FECHA_INICIO_EMPRESA).year,
        anio_final = date.fromisoformat(FECHA_CORTE).year,
        incremento_anual = INCREMENTO_SALARIAL_ANUAL,
    )
)


def calcular_accidentes_esperados_mes(
    trabajadores,
    fecha,
    factor_extraordinario = 1.0,
):
    """
    Calcula la cantidad esperada de accidentes para un mes.

    La tasa anual define el nivel general de accidentalidad.
    La estacionalidad redistribuye ese nivel durante los meses.
    El factor extraordinario permite incorporar posteriormente
    eventos puntuales o temporales.
    """

    if fecha.day != 1:
        raise ValueError(
            "La fecha debe corresponder al primer día del mes."
        )

    año = fecha.year
    mes = fecha.month

    if año not in TASA_ANUAL_ACCIDENTALIDAD:
        raise ValueError(
            f"No existe una tasa de accidentalidad "
            f"configurada para el año {año}."
        )

    if mes not in ESTACIONALIDAD_MENSUAL:
        raise ValueError(
            f"No existe un factor de estacionalidad "
            f"configurado para el mes {mes}."
        )

    tasa_anual = TASA_ANUAL_ACCIDENTALIDAD[año]

    factor_estacional = ESTACIONALIDAD_MENSUAL[mes]

    dias_mes = monthrange(
        año,
        mes,
    )[1]

    poblacion_diaria = []

    for dia in range(1, dias_mes + 1):

        fecha_dia = date(
            año,
            mes,
            dia,
        )

        activos = contar_activos(
            trabajadores,
            fecha_dia,
        )

        poblacion_diaria.append(
            activos
        )

    exposicion_mensual = (
        sum(poblacion_diaria)
        / dias_mes
    )

    tasa_mensual_base = (
        tasa_anual / 12
    )

    tasa_mensual_ajustada = (
        tasa_mensual_base
        * factor_estacional
        * factor_extraordinario
    )

    accidentes_esperados = (
        exposicion_mensual
        * tasa_mensual_ajustada
    )

    return accidentes_esperados


def generar_cantidad_accidentes(
    accidentes_esperados,
    rng,
):
    """
    Genera una cantidad observada de accidentes
    utilizando una distribución de Poisson.
    """

    if accidentes_esperados < 0:
        raise ValueError(
            "La cantidad esperada de accidentes "
            "no puede ser negativa."
        )

    return int(
        rng.poisson(
            accidentes_esperados
        )
    )


def calcular_accidentalidad_anual(
    trabajadores,
    accidentes,
    año,
):
    """
    Calcula el resumen mensual de accidentalidad
    a partir de los accidentes individuales generados.
    """

    resultados = []

    for mes in range(1, 13):

        fecha = date(
            año,
            mes,
            1,
        )

        accidentes_esperados = (
            calcular_accidentes_esperados_mes(
                trabajadores,
                fecha,
            )
        )

        accidentes_observados = sum(
            1
            for accidente in accidentes
            if accidente["fecha_accidente"].year == año
            and accidente["fecha_accidente"].month == mes
        )

        resultados.append(
            {
                "fecha": fecha,
                "accidentes_esperados": accidentes_esperados,
                "accidentes_observados": accidentes_observados,
            }
        )

    return resultados


def obtener_trabajadores_expuestos(
    trabajadores,
    fecha,
):
    """Obtiene los trabajadores activos en una fecha."""

    trabajadores_expuestos = [
        trabajador
        for trabajador in trabajadores
        if trabajador["fecha_ingreso"] <= fecha
        and (
            trabajador["fecha_retiro"] is None
            or trabajador["fecha_retiro"] > fecha
        )
    ]

    return trabajadores_expuestos


def obtener_salario(
    cargo,
    fecha_accidente,
):
    """
    Obtiene el salario mensual correspondiente al cargo
    del trabajador en el año del accidente.

    El salario se consulta en SALARIOS_POR_CARGO_ANIO.
    """

    if fecha_accidente is None:
        raise ValueError(
            "No se puede obtener el salario "
            "sin fecha de accidente."
        )

    anio = fecha_accidente.year

    clave = (
        cargo,
        anio,
    )

    if clave not in SALARIOS_POR_CARGO_ANIO:
        raise ValueError(
            f"No existe salario configurado "
            f"para el cargo '{cargo}' "
            f"en el año {anio}."
        )

    return SALARIOS_POR_CARGO_ANIO[clave]


def seleccionar_trabajador_accidentado(
    trabajadores_expuestos,
    rng,
):
    """Selecciona aleatoriamente un trabajador expuesto."""

    if not trabajadores_expuestos:
        raise ValueError(
            "No existen trabajadores expuestos "
            "para seleccionar un accidente."
        )

    indice = rng.integers(
        0,
        len(trabajadores_expuestos),
    )

    return trabajadores_expuestos[indice]


def generar_fecha_accidente(
    año,
    mes,
    rng,
):
    """Genera aleatoriamente una fecha dentro del mes."""

    dias_mes = monthrange(
        año,
        mes,
    )[1]

    dia = rng.integers(
        1,
        dias_mes + 1,
    )

    return date(
        año,
        mes,
        int(dia),
    )


def generar_accidentalidad_anual(
    trabajadores,
    fecha_inicio,
    fecha_corte,
    rng,
):
    """
    Genera la accidentalidad detallada de un año completo.

    La función calcula la accidentalidad esperada de cada mes,
    genera una única realización observada mediante Poisson
    y construye los accidentes individuales correspondientes.
    """

    accidentes_anuales = []

    id_accidente = 1


    fecha_actual = date(
        fecha_inicio.year,
        fecha_inicio.month,
        1,
    )

    fecha_fin = date(
        fecha_corte.year,
        fecha_corte.month,
        1,
    )

    while fecha_actual <= fecha_fin:

        accidentes_esperados = (
        calcular_accidentes_esperados_mes(
            trabajadores,
            fecha_actual,
        )
    )

        accidentes_mes = (
            generar_accidentes_mes(
                trabajadores = trabajadores,
                año = fecha_actual.year,
                mes = fecha_actual.month,
                rng = rng,
                id_accidente_inicial = id_accidente,
                accidentes_esperados = accidentes_esperados,
            )
        )

        accidentes_anuales.extend(
            accidentes_mes
        )

        id_accidente += len(
            accidentes_mes
        )

        if fecha_actual.month == 12:

            fecha_actual = date(
                fecha_actual.year + 1,
                1,
                1,
            )

        else:

            fecha_actual = date(
                fecha_actual.year,
                fecha_actual.month + 1,
                1,
            )
        
    return accidentes_anuales


def validar_accidentes(
    trabajadores,
    accidentes,
):
    """Valida la coherencia básica de los accidentes."""

    errores = []

    trabajadores_por_id = {
        trabajador["id_trabajador"]: trabajador
        for trabajador in trabajadores
    }

    fecha_inicio = date.fromisoformat(
        FECHA_INICIO_ANALISIS
    )

    fecha_corte = date.fromisoformat(
        FECHA_CORTE
    )

    for accidente in accidentes:

        id_accidente = accidente["id_accidente"]
        id_trabajador = accidente["id_trabajador"]
        fecha_accidente = accidente["fecha_accidente"]

        # 1. El trabajador debe existir.
        trabajador = trabajadores_por_id.get(
            id_trabajador
        )

        if trabajador is None:
            errores.append(
                f"Accidente {id_accidente}: "
                f"no existe el trabajador "
                f"{id_trabajador}."
            )
            continue

        # 2. El accidente debe estar dentro
        #    del período de análisis.
        if not (
            fecha_inicio
            <= fecha_accidente
            <= fecha_corte
        ):
            errores.append(
                f"Accidente {id_accidente}: "
                f"fecha {fecha_accidente} "
                f"fuera del período de análisis."
            )

        # 3. El trabajador debe estar activo
        #    en la fecha del accidente.
        fecha_ingreso = trabajador["fecha_ingreso"]
        fecha_retiro = trabajador["fecha_retiro"]

        if fecha_accidente < fecha_ingreso:
            errores.append(
                f"Accidente {id_accidente}: "
                "ocurre antes del ingreso "
                f"del trabajador {id_trabajador}."
            )

        if (
            fecha_retiro is not None
            and fecha_accidente > fecha_retiro
        ):
            errores.append(
                f"Accidente {id_accidente}: "
                "ocurre después del retiro "
                f"del trabajador {id_trabajador}."
            )

    return errores


def validar_catalogos_accidentalidad():
    """Valida las relaciones entre los catálogos de accidentalidad."""

    errores = []

    tipos_accidente = set(TIPOS_ACCIDENTE)
    cargos = set(CARGOS.keys())
    tipos_lesion = set(TIPOS_LESION)
    partes_cuerpo = set(PARTES_CUERPO)
    diagnosticos = set(DIAGNOSTICOS.keys())

    # ---------------------------------------------------------
    # 1. MECANISMOS → TIPOS_ACCIDENTE
    # ---------------------------------------------------------

    for tipo_accidente in MECANISMOS:

        if tipo_accidente not in tipos_accidente:
            errores.append(
                f"MECANISMOS: el tipo de accidente "
                f"'{tipo_accidente}' no existe en "
                "TIPOS_ACCIDENTE."
            )

    # ---------------------------------------------------------
    # 2. CARGO → TIPO_ACCIDENTE
    # ---------------------------------------------------------

    cargos_relacionados = set(
        COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE.keys()
    )

    cargos_sin_relacion = (
        cargos
        - cargos_relacionados
    )

    for cargo in sorted(cargos_sin_relacion):
        errores.append(
            f"CARGO sin compatibilidad: "
            f"'{cargo}'."
        )

    cargos_inexistentes = (
        cargos_relacionados
        - cargos
    )

    for cargo in sorted(cargos_inexistentes):
        errores.append(
            f"CARGO inexistente en CARGOS: "
            f"'{cargo}'."
        )

    for cargo, relaciones in (
        COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE.items()
    ):

        tipos_vistos = set()
        suma_pesos = 0.0

        for tipo_accidente, peso in relaciones:

            if tipo_accidente in tipos_vistos:
                errores.append(
                    f"CARGO '{cargo}': "
                    f"tipo de accidente repetido "
                    f"'{tipo_accidente}'."
                )

            tipos_vistos.add(
                tipo_accidente
            )

            if tipo_accidente not in tipos_accidente:
                errores.append(
                    f"CARGO '{cargo}': "
                    f"tipo de accidente inexistente "
                    f"'{tipo_accidente}'."
                )

            if not isinstance(
                peso,
                (int, float)
            ):
                errores.append(
                    f"CARGO '{cargo}': "
                    f"peso no numérico para "
                    f"'{tipo_accidente}'."
                )
                continue

            if peso < 0 or peso > 1:
                errores.append(
                    f"CARGO '{cargo}': "
                    f"peso fuera de rango para "
                    f"'{tipo_accidente}': {peso}."
                )

            suma_pesos += peso

        if abs(suma_pesos - 1.0) > 1e-9:
            errores.append(
                f"CARGO '{cargo}': "
                f"los pesos suman "
                f"{suma_pesos:.6f} "
                "y deben sumar 1.000000."
            )

    # ---------------------------------------------------------
    # 3. TIPO_ACCIDENTE → MECANISMO
    # ---------------------------------------------------------

    for tipo_accidente, mecanismos in MECANISMOS.items():

        for mecanismo in mecanismos:

            if mecanismo not in (
                COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.get(
                    tipo_accidente,
                    {}
                )
            ):
                errores.append(
                    f"TIPO '{tipo_accidente}': "
                    f"mecanismo '{mecanismo}' "
                    "sin compatibilidad de diagnósticos."
                )

    # ---------------------------------------------------------
    # 4. TIPO_ACCIDENTE → MECANISMO → DIAGNÓSTICO
    # ---------------------------------------------------------

    for tipo_accidente, mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.items()
    ):

        if tipo_accidente not in tipos_accidente:
            errores.append(
                f"Compatibilidad: tipo de accidente "
                f"inexistente '{tipo_accidente}'."
            )
            continue

        for mecanismo, relaciones in (
            mecanismos.items()
        ):

            if mecanismo not in MECANISMOS.get(
                tipo_accidente,
                []
            ):
                errores.append(
                    f"TIPO '{tipo_accidente}': "
                    f"mecanismo '{mecanismo}' "
                    "no pertenece a MECANISMOS."
                )

            if not relaciones:
                errores.append(
                    f"TIPO '{tipo_accidente}' / "
                    f"MECANISMO '{mecanismo}': "
                    "sin diagnósticos."
                )
                continue

            suma_pesos_normal = 0.0
            suma_pesos_ventana = 0.0

            diagnosticos_vistos = set()

            for (
                codigo,
                peso_normal,
                peso_ventana,
            ) in relaciones:

                # -------------------------------------------------
                # Diagnósticos duplicados
                # -------------------------------------------------

                if codigo in diagnosticos_vistos:

                    errores.append(
                        f"TIPO '{tipo_accidente}' / "
                        f"MECANISMO '{mecanismo}': "
                        f"diagnóstico repetido "
                        f"'{codigo}'."
                    )

                diagnosticos_vistos.add(codigo)

                # -------------------------------------------------
                # Diagnóstico existente
                # -------------------------------------------------

                if codigo not in diagnosticos:

                    errores.append(
                        f"TIPO '{tipo_accidente}' / "
                        f"MECANISMO '{mecanismo}': "
                        f"diagnóstico inexistente "
                        f"'{codigo}'."
                    )

                # -------------------------------------------------
                # Validar peso NORMAL
                # -------------------------------------------------

                if not isinstance(
                    peso_normal,
                    (int, float)
                ):

                    errores.append(
                        f"TIPO '{tipo_accidente}' / "
                        f"MECANISMO '{mecanismo}': "
                        f"peso_normal no numérico "
                        f"para '{codigo}'."
                    )

                else:

                    if (
                        peso_normal < 0
                        or peso_normal > 1
                    ):

                        errores.append(
                            f"TIPO '{tipo_accidente}' / "
                            f"MECANISMO '{mecanismo}': "
                            f"peso_normal fuera de rango "
                            f"para '{codigo}': "
                            f"{peso_normal}."
                        )

                    suma_pesos_normal += peso_normal

                # -------------------------------------------------
                # Validar peso VENTANA
                # -------------------------------------------------

                if not isinstance(
                    peso_ventana,
                    (int, float)
                ):

                    errores.append(
                        f"TIPO '{tipo_accidente}' / "
                        f"MECANISMO '{mecanismo}': "
                        f"peso_ventana no numérico "
                        f"para '{codigo}'."
                    )

                else:

                    if (
                        peso_ventana < 0
                        or peso_ventana > 1
                    ):

                        errores.append(
                            f"TIPO '{tipo_accidente}' / "
                            f"MECANISMO '{mecanismo}': "
                            f"peso_ventana fuera de rango "
                            f"para '{codigo}': "
                            f"{peso_ventana}."
                        )

                    suma_pesos_ventana += peso_ventana

            # -----------------------------------------------------
            # Validar suma NORMAL
            # -----------------------------------------------------

            if abs(
                suma_pesos_normal - 1.0
            ) > 1e-9:

                errores.append(
                    f"TIPO '{tipo_accidente}' / "
                    f"MECANISMO '{mecanismo}': "
                    f"los peso_normal suman "
                    f"{suma_pesos_normal:.6f} "
                    "y deben sumar 1.000000."
                )

            # -----------------------------------------------------
            # Validar suma VENTANA
            # -----------------------------------------------------

            if abs(
                suma_pesos_ventana - 1.0
            ) > 1e-9:

                errores.append(
                    f"TIPO '{tipo_accidente}' / "
                    f"MECANISMO '{mecanismo}': "
                    f"los peso_ventana suman "
                    f"{suma_pesos_ventana:.6f} "
                    "y deben sumar 1.000000."
                )

    # ---------------------------------------------------------
    # 5. DIAGNÓSTICOS → TIPO_LESION + PARTE_CUERPO
    # ---------------------------------------------------------

    for codigo, diagnostico in DIAGNOSTICOS.items():

        tipo_lesion = diagnostico.get(
            "tipo_lesion"
        )

        parte_cuerpo = diagnostico.get(
            "parte_cuerpo"
        )

        if tipo_lesion not in tipos_lesion:
            errores.append(
                f"Diagnóstico '{codigo}': "
                f"tipo de lesión '{tipo_lesion}' "
                "no existe en TIPOS_LESION."
            )

        if parte_cuerpo not in partes_cuerpo:
            errores.append(
                f"Diagnóstico '{codigo}': "
                f"parte del cuerpo '{parte_cuerpo}' "
                "no existe en PARTES_CUERPO."
            )

        # ---------------------------------------------------------
    # 6. DIAGNÓSTICO → MORTALIDAD
    # ---------------------------------------------------------

    for codigo, probabilidad in (
        COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD.items()
    ):

        if codigo not in DIAGNOSTICOS:
            errores.append(
                f"COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD: "
                f"el diagnóstico '{codigo}' no existe "
                f"en DIAGNOSTICOS."
            )

        if not (
            0 <= probabilidad <= 1
        ):
            errores.append(
                f"COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD: "
                f"la probabilidad de '{codigo}' "
                f"debe estar entre 0 y 1."
            )

    return errores


def seleccionar_tipo_accidente(
    cargo,
    rng,
):
    """Selecciona un tipo de accidente compatible con el cargo."""

    relaciones = (
        COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE.get(
            cargo
        )
    )

    if not relaciones:
        raise ValueError(
            "No existen tipos de accidente configurados "
            f"para el cargo '{cargo}'."
        )

    tipos = [
        tipo_accidente
        for tipo_accidente, _ in relaciones
    ]

    pesos = [
        peso
        for _, peso in relaciones
    ]
    
    return str(
        rng.choice(
            tipos,
            p = pesos,
        )
    )


def seleccionar_mecanismo(
    tipo_accidente,
    rng,
):
    """Selecciona un mecanismo compatible con el tipo de accidente."""

    mecanismos_disponibles = MECANISMOS.get(
        tipo_accidente
    )

    if not mecanismos_disponibles:
        raise ValueError(
            f"No existen mecanismos configurados "
            f"para '{tipo_accidente}'."
        )

    indice = rng.integers(
        0,
        len(mecanismos_disponibles),
    )

    return mecanismos_disponibles[indice]


def seleccionar_agente(
    mecanismo,
    rng,
):
    """Selecciona un agente compatible con el mecanismo."""

    agentes_disponibles = (
        COMPATIBILIDAD_MECANISMO_AGENTE.get(
            mecanismo
        )
    )

    if not agentes_disponibles:
        raise ValueError(
            f"No existen agentes configurados "
            f"para el mecanismo '{mecanismo}'."
        )

    indice = rng.integers(
        0,
        len(agentes_disponibles),
    )

    return agentes_disponibles[indice]


def validar_compatibilidad_mecanismo_agente():
    """Valida la relación mecanismo → agente."""

    errores = []

    mecanismos_catalogo = {
        mecanismo
        for mecanismos in MECANISMOS.values()
        for mecanismo in mecanismos
    }

    agentes_catalogo = set(
        AGENTES_LESION
    )

    mecanismos_relacionados = set(
        COMPATIBILIDAD_MECANISMO_AGENTE.keys()
    )

    # Mecanismos sin relación
    mecanismos_sin_relacion = (
        mecanismos_catalogo
        - mecanismos_relacionados
    )

    for mecanismo in sorted(mecanismos_sin_relacion):
        errores.append(
            f"Mecanismo sin compatibilidad: "
            f"'{mecanismo}'."
        )

    # Relaciones con mecanismos inexistentes
    mecanismos_inexistentes = (
        mecanismos_relacionados
        - mecanismos_catalogo
    )

    for mecanismo in sorted(mecanismos_inexistentes):
        errores.append(
            f"Mecanismo inexistente en catálogo: "
            f"'{mecanismo}'."
        )

    # Agentes inexistentes
    for mecanismo, agentes in (
        COMPATIBILIDAD_MECANISMO_AGENTE.items()
    ):

        for agente in agentes:

            if agente not in agentes_catalogo:
                errores.append(
                    f"Mecanismo '{mecanismo}': "
                    f"agente inexistente "
                    f"'{agente}'."
                )

    return errores


def determinar_uso_peso_ventana(
    fecha_accidente,
    fecha_retiro,
):
    """
    Determina si el accidente ocurre dentro de la
    ventana previa al retiro del trabajador.

    Se considera ventana cuando faltan
    180 días o menos para el retiro.

    Trabajadores sin fecha de retiro permanecen
    siempre en distribución NORMAL.
    """

    # Trabajador activo sin fecha de retiro
    if fecha_retiro is None:
        return False

    dias_hasta_retiro = (
        fecha_retiro - fecha_accidente
    ).days

    # Menos de 180 días hasta el retiro
    if dias_hasta_retiro <= DIAS_MAXIMOS_INCAPACIDAD:
        return True

    return False


def seleccionar_diagnostico(
    tipo_accidente,
    mecanismo,
    rng,
    usar_peso_ventana = False,
):
    """
    Selecciona un diagnóstico compatible con el tipo de accidente
    y mecanismo, utilizando el peso normal o el peso de ventana.

    La estructura esperada del catálogo es:

        (codigo, peso_normal, peso_ventana)

    Parámetros
    ----------
    tipo_accidente : str
        Tipo de accidente seleccionado.

    mecanismo : str
        Mecanismo seleccionado para el tipo de accidente.

    rng : numpy.random.Generator
        Generador aleatorio utilizado por el sistema.

    usar_peso_ventana : bool, default = False
        False -> utiliza peso_normal.
        True  -> utiliza peso_ventana.
    """

    mecanismos_tipo = (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.get(
            tipo_accidente
        )
    )

    if not mecanismos_tipo:
        raise ValueError(
            f"No existen diagnósticos configurados "
            f"para el tipo de accidente "
            f"'{tipo_accidente}'."
        )

    opciones = mecanismos_tipo.get(
        mecanismo
    )

    if not opciones:
        raise ValueError(
            f"No existen diagnósticos configurados "
            f"para el mecanismo '{mecanismo}' "
            f"del tipo '{tipo_accidente}'."
        )

    # ---------------------------------------------------------
    # Validar estructura del catálogo
    # ---------------------------------------------------------

    for opcion in opciones:

        if len(opcion) != 3:
            raise ValueError(
                f"La configuración del diagnóstico "
                f"en '{tipo_accidente}' / '{mecanismo}' "
                f"debe tener la estructura "
                "(codigo, peso_normal, peso_ventana). "
                f"Valor encontrado: {opcion}"
            )

    # ---------------------------------------------------------
    # Separar códigos y pesos
    # ---------------------------------------------------------

    codigos = [
        codigo
        for codigo, _, _ in opciones
    ]

    indice_peso = 2 if usar_peso_ventana else 1

    pesos = np.array(
        [
            opcion[indice_peso]
            for opcion in opciones
        ],
        dtype = float,
    )

    # ---------------------------------------------------------
    # Validar pesos
    # ---------------------------------------------------------

    if np.any(pesos < 0):
        raise ValueError(
            f"Existen pesos negativos en el mecanismo "
            f"'{mecanismo}' del tipo "
            f"'{tipo_accidente}'."
        )

    suma_pesos = pesos.sum()

    if not np.isclose(
        suma_pesos,
        1.0,
    ):
        tipo_peso = (
            "peso_ventana"
            if usar_peso_ventana
            else "peso_normal"
        )

        raise ValueError(
            f"Los {tipo_peso} del mecanismo "
            f"'{mecanismo}' del tipo "
            f"'{tipo_accidente}' no suman 1.0. "
            f"Suma actual: {suma_pesos:.6f}"
        )

    # ---------------------------------------------------------
    # Selección ponderada
    # ---------------------------------------------------------
    
    codigo = str(
        rng.choice(
            codigos,
            p = pesos,
        )
    )

    # ---------------------------------------------------------
    # Obtener información del diagnóstico
    # ---------------------------------------------------------

    diagnostico = DIAGNOSTICOS.get(
        codigo
    )

    if diagnostico is None:
        raise ValueError(
            f"El diagnóstico '{codigo}' "
            "no existe en DIAGNOSTICOS."
        )

    return {
        "codigo": codigo,
        "diagnostico": diagnostico["descripcion"],
        "tipo_lesion": diagnostico["tipo_lesion"],
        "parte_cuerpo": diagnostico["parte_cuerpo"],
    }


def seleccionar_escenario_incapacidad(
    codigo_diagnostico,
    rng,
    usar_peso_ventana = False,
):
    """
    Selecciona uno de los escenarios de incapacidad
    definidos para el diagnóstico.

    Cada diagnóstico debe contener exactamente tres
    escenarios, cada uno con:

        nivel
        dias_min
        dias_max
        peso_normal
        peso_ventana
    """

    diagnostico = DIAGNOSTICOS.get(
        codigo_diagnostico
    )

    if diagnostico is None:
        raise ValueError(
            f"El diagnóstico '{codigo_diagnostico}' "
            "no existe en DIAGNOSTICOS."
        )

    escenarios = diagnostico.get(
        "escenarios"
    )

    if not escenarios:
        raise ValueError(
            f"El diagnóstico '{codigo_diagnostico}' "
            "no tiene escenarios de incapacidad."
        )

    if len(escenarios) != 3:
        raise ValueError(
            f"El diagnóstico '{codigo_diagnostico}' "
            f"debe tener exactamente 3 escenarios. "
            f"Encontrados: {len(escenarios)}."
        )

    # ---------------------------------------------------------
    # Seleccionar el tipo de peso
    # ---------------------------------------------------------

    campo_peso = (
        "peso_ventana"
        if usar_peso_ventana
        else "peso_normal"
    )

    pesos = np.array(
        [
            escenario[campo_peso]
            for escenario in escenarios
        ],
        dtype = float,
    )

    # ---------------------------------------------------------
    # Validar pesos
    # ---------------------------------------------------------

    if np.any(pesos < 0):
        raise ValueError(
            f"El diagnóstico '{codigo_diagnostico}' "
            f"contiene pesos negativos."
        )

    suma_pesos = pesos.sum()

    if not np.isclose(
        suma_pesos,
        1.0,
    ):
        raise ValueError(
            f"Los pesos '{campo_peso}' del diagnóstico "
            f"'{codigo_diagnostico}' no suman 1.0. "
            f"Suma actual: {suma_pesos:.6f}"
        )

    # ---------------------------------------------------------
    # Selección ponderada
    # ---------------------------------------------------------

    indice = rng.choice(
        len(escenarios),
        p = pesos,
    )

    escenario = escenarios[indice]

    return escenario


def seleccionar_area_accidente(
    cargo,
    rng,
):
    """
    Selecciona el área física donde puede ocurrir
    el accidente, de acuerdo con las áreas compatibles
    con el cargo del trabajador.
    """

    areas = COMPATIBILIDAD_CARGO_AREA_ACCIDENTE.get(
        cargo
    )

    if not areas:
        raise ValueError(
            f"No existen áreas de accidente configuradas "
            f"para el cargo '{cargo}'."
        )

    return rng.choice(areas)


def generar_dias_incapacidad(
    escenario,
    rng,
):
    """
    Genera los días de incapacidad dentro del rango
    definido por el escenario seleccionado.
    """

    dias_min = escenario["dias_min"]
    dias_max = escenario["dias_max"]

    if dias_min < 1:
        raise ValueError(
            f"dias_min inválido: {dias_min}"
        )

    if dias_max > 180:
        raise ValueError(
            f"dias_max inválido: {dias_max}"
        )

    if dias_min > dias_max:
        raise ValueError(
            f"dias_min ({dias_min}) no puede ser "
            f"mayor que dias_max ({dias_max})."
        )

    return int(
        rng.integers(
            dias_min,
            dias_max + 1,
        )
    )


def ajustar_dias_por_fecha_retiro(
    fecha_accidente,
    fecha_retiro,
    dias_incapacidad,
):
    """
    Ajusta los días de incapacidad cuando el trabajador
    tiene una fecha de retiro.

    Regla:
        La incapacidad puede extenderse hasta el día
        anterior a la fecha de retiro.

    Si el trabajador está activo (fecha_retiro=None),
    no se aplica ningún recorte.
    """

    if dias_incapacidad < 1:
        raise ValueError(
            "Los días de incapacidad deben ser "
            "mayores o iguales a 1."
        )

    # ---------------------------------------------------------
    # Trabajador activo
    # ---------------------------------------------------------

    if fecha_retiro is None:
        return dias_incapacidad

    # ---------------------------------------------------------
    # Validación de fechas
    # ---------------------------------------------------------

    if fecha_retiro <= fecha_accidente:
        raise ValueError(
            "La fecha de retiro debe ser posterior "
            "a la fecha del accidente."
        )

    # ---------------------------------------------------------
    # Máximo de días permitido
    # ---------------------------------------------------------

    dias_hasta_retiro = (
        fecha_retiro - fecha_accidente
    ).days

    # ---------------------------------------------------------
    # Aplicar recorte
    # ---------------------------------------------------------

    return min(
        dias_incapacidad,
        dias_hasta_retiro,
    )


def determinar_gravedad_accidente(
    codigo_diagnostico,
    rng,
):
    """
    Determina la clasificación normativa del accidente
    como grave o leve según los criterios configurados
    para la Resolución 1401 de 2007.

    La gravedad clínica del diagnóstico se mantiene
    separada de la gravedad normativa del accidente.
    """

    criterio = CRITERIOS_GRAVEDAD_RES1401.get(
        codigo_diagnostico
    )

    # ---------------------------------------------------------
    # DIAGNÓSTICO SIN CRITERIO DE GRAVEDAD
    # ---------------------------------------------------------

    if criterio is None:

        return {
            "accidente_grave": False,
            "gravedad_accidente": "Leve",
            "criterio_gravedad": "No aplica",
        }

    tipo_criterio = criterio["tipo"]

    # ---------------------------------------------------------
    # CRITERIO DIRECTO
    # ---------------------------------------------------------

    if tipo_criterio == "DIRECTO":

        return {
            "accidente_grave": True,
            "gravedad_accidente": "Grave",
            "criterio_gravedad": (
                criterio["criterio"]
            ),
        }

    # ---------------------------------------------------------
    # CRITERIO CONDICIONAL
    # ---------------------------------------------------------

    if tipo_criterio == "CONDICIONAL":

        probabilidad = (
            PROBABILIDAD_CRITERIO_GRAVEDAD_RES1401
        )

        condicion_cumplida = (
            rng.random() < probabilidad
        )

        if condicion_cumplida:

            return {
                "accidente_grave": True,
                "gravedad_accidente": "Grave",
                "criterio_gravedad": (
                    criterio["criterio"]
                ),
            }

        return {
            "accidente_grave": False,
            "gravedad_accidente": "Leve",
            "criterio_gravedad": "No aplica",
        }

    # ---------------------------------------------------------
    # CRITERIO NO CONFIGURADO
    # ---------------------------------------------------------

    raise ValueError(
        f"Tipo de criterio de gravedad "
        f"no reconocido para el diagnóstico "
        f"'{codigo_diagnostico}': "
        f"'{tipo_criterio}'."
    )


def determinar_accidente_mortal(
    codigo_diagnostico,
    accidente_grave,
    rng,
):
    """
    Determina si un accidente grave resulta mortal.
    """

    if not accidente_grave:
        return False

    probabilidad_mortalidad = (
        COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD.get(
            codigo_diagnostico,
            0.0,
        )
    )

    return (
        rng.random()
        < probabilidad_mortalidad
    )


def generar_caracteristicas_accidente(
    cargo,
    fecha_accidente,
    fecha_retiro,
    rng,
):
    """
    Genera las características coherentes de un accidente.

    Determina primero si el accidente ocurre dentro
    de la ventana previa al retiro y, con base en ello,
    selecciona el peso NORMAL o VENTANA para el diagnóstico.
    """

    tipo_accidente = seleccionar_tipo_accidente(
        cargo,
        rng,
    )

    mecanismo = seleccionar_mecanismo(
        tipo_accidente,
        rng,
    )

    agente = seleccionar_agente(
        mecanismo,
        rng,
    )

    area_accidente = seleccionar_area_accidente(
        cargo,
        rng,
    )

    # ---------------------------------------------------------
    # Determinar distribución NORMAL / VENTANA
    # ---------------------------------------------------------

    usar_peso_ventana = (
        determinar_uso_peso_ventana(
            fecha_accidente,
            fecha_retiro,
        )
    )

    diagnostico = seleccionar_diagnostico(
        tipo_accidente,
        mecanismo,
        rng,
        usar_peso_ventana,
    )

    escenario = seleccionar_escenario_incapacidad(
        diagnostico["codigo"],
        rng,
        usar_peso_ventana,
    )

    dias_incapacidad_originales = (
        generar_dias_incapacidad(
            escenario,
            rng,
        )
    )

    dias_incapacidad = (
        ajustar_dias_por_fecha_retiro(
            fecha_accidente,
            fecha_retiro,
            dias_incapacidad_originales,
        )
    )

    gravedad = determinar_gravedad_accidente(
        diagnostico["codigo"],
        rng,
    )

    return {
        "tipo_accidente": tipo_accidente,
        "mecanismo": mecanismo,
        "agente": agente,
        "area_accidente": area_accidente,
        "codigo_diagnostico": diagnostico["codigo"],
        "diagnostico": diagnostico["diagnostico"],
        "tipo_lesion": diagnostico["tipo_lesion"],
        "parte_cuerpo": diagnostico["parte_cuerpo"],
        "accidente_grave": gravedad["accidente_grave"],
        "gravedad_accidente": gravedad["gravedad_accidente"],
        "criterio_gravedad": gravedad["criterio_gravedad"],
        "escenario_incapacidad": escenario["nivel"],
        "dias_incapacidad_originales": (dias_incapacidad_originales),
        "dias_incapacidad": (dias_incapacidad),
        "usar_peso_ventana": usar_peso_ventana,
    }


def generar_accidentes_mes(
    trabajadores,
    año,
    mes,
    rng,
    id_accidente_inicial = 1,
    accidentes_esperados = None,
):
    """Genera los accidentes individuales de un mes."""

    fecha_mes = date(
        año,
        mes,
        1,
    )

    if accidentes_esperados is None:
        accidentes_esperados = (
            calcular_accidentes_esperados_mes(
                trabajadores,
                fecha_mes,
            )
        )

    cantidad_accidentes = (
        generar_cantidad_accidentes(
            accidentes_esperados,
            rng,
        )
    )

    accidentes = []

    for i in range(cantidad_accidentes):

        fecha_accidente = generar_fecha_accidente(
            año,
            mes,
            rng,
        )

        trabajadores_expuestos = (
            obtener_trabajadores_expuestos(
                trabajadores,
                fecha_accidente,
            )
        )

        trabajador = seleccionar_trabajador_accidentado(
            trabajadores_expuestos,
            rng,
        )

        caracteristicas = (
            generar_caracteristicas_accidente(
                trabajador["cargo"],
                fecha_accidente,
                trabajador["fecha_retiro"],
                rng,
            )
        )

        salario = obtener_salario(
            trabajador["cargo"],
            fecha_accidente,
        )

        accidente = {
            "id_accidente": (
                id_accidente_inicial + i
            ),
            "id_trabajador": (
                trabajador["id_trabajador"]
            ),
            "fecha_accidente": fecha_accidente,
            "tipo_accidente": (
                caracteristicas["tipo_accidente"]
            ),
            "mecanismo": (
                caracteristicas["mecanismo"]
            ),
            "agente": (
                caracteristicas["agente"]
            ),
            "area_accidente": (
                caracteristicas["area_accidente"]
            ),
            "codigo_diagnostico": (
                caracteristicas["codigo_diagnostico"]
            ),
            "diagnostico": (
                caracteristicas["diagnostico"]
            ),
            "tipo_lesion": (
                caracteristicas["tipo_lesion"]
            ),
            "parte_cuerpo": (
                caracteristicas["parte_cuerpo"]
            ),
            "gravedad_accidente": (
                caracteristicas["gravedad_accidente"]
            ),
            "dias_incapacidad": (
                caracteristicas["dias_incapacidad"]
            ),
            "salario": salario,
        }

        accidentes.append(
            accidente
        )

    return accidentes


def validar_compatibilidad_tipo_mecanismo_diagnostico():
    """Valida TIPO_ACCIDENTE → MECANISMO → DIAGNÓSTICO + PESO."""

    errores = []

    tipos_accidente = set(TIPOS_ACCIDENTE)
    diagnosticos = set(DIAGNOSTICOS.keys())

    tipos_relacionados = set(
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.keys()
    )

    # Tipos de accidente sin relación
    for tipo in sorted(
        tipos_accidente - tipos_relacionados
    ):
        errores.append(
            f"Tipo de accidente sin compatibilidad "
            f"tipo-mecanismo-diagnóstico: '{tipo}'."
        )

    # Tipos de accidente inexistentes
    for tipo in sorted(
        tipos_relacionados - tipos_accidente
    ):
        errores.append(
            f"Tipo de accidente inexistente: '{tipo}'."
        )

    for tipo, mecanismos in (
        COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO.items()
    ):
        mecanismos_permitidos = set(
            MECANISMOS.get(tipo, [])
        )
        mecanismos_relacionados = set(
            mecanismos.keys()
        )

        # Mecanismos definidos en MECANISMOS pero ausentes
        # en la relación tipo → mecanismo → diagnóstico.
        for mecanismo in sorted(
            mecanismos_permitidos - mecanismos_relacionados
        ):
            errores.append(
                f"Tipo '{tipo}': mecanismo sin diagnósticos "
                f"compatibles: '{mecanismo}'."
            )

        # Mecanismos inexistentes para el tipo.
        for mecanismo in sorted(
            mecanismos_relacionados - mecanismos_permitidos
        ):
            errores.append(
                f"Tipo '{tipo}': mecanismo inexistente "
                f"o no compatible: '{mecanismo}'."
            )

        for mecanismo, opciones in mecanismos.items():

            if len(opciones) != 8:
                errores.append(
                    f"Tipo '{tipo}', mecanismo '{mecanismo}': "
                    f"se esperaban 8 diagnósticos y se encontraron "
                    f"{len(opciones)}."
                )

            codigos = []
            pesos = []

            for opcion in opciones:

                if (
                    not isinstance(opcion, tuple)
                    or len(opcion) != 2
                ):
                    errores.append(
                        f"Tipo '{tipo}', mecanismo '{mecanismo}': "
                        f"formato de diagnóstico inválido: {opcion}."
                    )
                    continue

                codigo, peso = opcion
                codigos.append(codigo)
                pesos.append(peso)

                if codigo not in diagnosticos:
                    errores.append(
                        f"Tipo '{tipo}', mecanismo '{mecanismo}': "
                        f"diagnóstico inexistente '{codigo}'."
                    )

                if not isinstance(
                    peso,
                    (int, float, np.integer, np.floating),
                ):
                    errores.append(
                        f"Tipo '{tipo}', mecanismo '{mecanismo}': "
                        f"peso inválido para '{codigo}': {peso}."
                    )

            if len(codigos) != len(set(codigos)):
                errores.append(
                    f"Tipo '{tipo}', mecanismo '{mecanismo}': "
                    "existen diagnósticos repetidos."
                )

            if pesos:
                suma_pesos = sum(
                    float(peso)
                    for peso in pesos
                    if isinstance(
                        peso,
                        (int, float, np.integer, np.floating),
                    )
                )

                if not np.isclose(
                    suma_pesos,
                    1.0,
                ):
                    errores.append(
                        f"Tipo '{tipo}', mecanismo '{mecanismo}': "
                        f"los pesos no suman 1.0. "
                        f"Suma={suma_pesos:.6f}."
                    )

    return errores


def validar_accidentes_generados(
    accidentes,
):
    """Valida la coherencia de las características de los accidentes."""

    errores = []

    for accidente in accidentes:

        id_accidente = accidente["id_accidente"]
        cargo = accidente["cargo"]
        tipo_accidente = accidente["tipo_accidente"]
        mecanismo = accidente["mecanismo"]
        agente = accidente["agente"]
        codigo_diagnostico = accidente["codigo_diagnostico"]
        diagnostico = accidente["diagnostico"]
        tipo_lesion = accidente["tipo_lesion"]
        parte_cuerpo = accidente["parte_cuerpo"]

        # -----------------------------------------------------
        # 1. Cargo
        # -----------------------------------------------------

        if cargo not in CARGOS:
            errores.append(
                f"AT {id_accidente}: "
                f"cargo inexistente '{cargo}'."
            )
            continue

        # -----------------------------------------------------
        # 2. Cargo → tipo de accidente
        # -----------------------------------------------------

        tipos_permitidos = [
            tipo
            for tipo, _ in (
                COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE.get(
                    cargo,
                    []
                )
            )
        ]

        if tipo_accidente not in tipos_permitidos:
            errores.append(
                f"AT {id_accidente}: "
                f"tipo de accidente '{tipo_accidente}' "
                f"no es compatible con el cargo "
                f"'{cargo}'."
            )

        # -----------------------------------------------------
        # 3. Tipo de accidente
        # -----------------------------------------------------

        if tipo_accidente not in TIPOS_ACCIDENTE:
            errores.append(
                f"AT {id_accidente}: "
                f"tipo de accidente inexistente "
                f"'{tipo_accidente}'."
            )
            continue

        # -----------------------------------------------------
        # 4. Tipo de accidente → mecanismo
        # -----------------------------------------------------

        mecanismos_permitidos = MECANISMOS.get(
            tipo_accidente,
            [],
        )

        if mecanismo not in mecanismos_permitidos:
            errores.append(
                f"AT {id_accidente}: "
                f"mecanismo '{mecanismo}' no es compatible "
                f"con '{tipo_accidente}'."
            )

        # -----------------------------------------------------
        # 5. Mecanismo → agente
        # -----------------------------------------------------

        agentes_permitidos = (
            COMPATIBILIDAD_MECANISMO_AGENTE.get(
                mecanismo,
                [],
            )
        )

        if agente not in agentes_permitidos:
            errores.append(
                f"AT {id_accidente}: "
                f"agente '{agente}' no es compatible "
                f"con el mecanismo '{mecanismo}'."
            )

        # -----------------------------------------------------
        # 6. Tipo → mecanismo → diagnóstico
        # -----------------------------------------------------

        relaciones_diagnostico = (
            COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO
            .get(
                tipo_accidente,
                {}
            )
            .get(
                mecanismo,
                []
            )
        )

        diagnosticos_permitidos = [
            codigo
            for codigo, _, _ in relaciones_diagnostico
        ]

        if codigo_diagnostico not in (
            diagnosticos_permitidos
        ):
            errores.append(
                f"AT {id_accidente}: "
                f"diagnóstico '{codigo_diagnostico}' "
                f"no es compatible con "
                f"'{tipo_accidente}' / "
                f"'{mecanismo}'."
            )

        # -----------------------------------------------------
        # 7. Código diagnóstico → diagnóstico
        # -----------------------------------------------------

        diagnostico_catalogo = DIAGNOSTICOS.get(
            codigo_diagnostico
        )

        if diagnostico_catalogo is None:

            errores.append(
                f"AT {id_accidente}: "
                f"código diagnóstico "
                f"'{codigo_diagnostico}' "
                "no existe en DIAGNOSTICOS."
            )

            continue

        if diagnostico != (
            diagnostico_catalogo["descripcion"]
        ):
            errores.append(
                f"AT {id_accidente}: "
                f"la información del diagnóstico "
                f"'{codigo_diagnostico}' "
                "no coincide con el catálogo."
            )

        # -----------------------------------------------------
        # 8. Diagnóstico → tipo de lesión
        # -----------------------------------------------------

        if tipo_lesion != (
            diagnostico_catalogo["tipo_lesion"]
        ):
            errores.append(
                f"AT {id_accidente}: "
                f"tipo de lesión '{tipo_lesion}' "
                f"no coincide con el diagnóstico "
                f"'{codigo_diagnostico}'."
            )

        # -----------------------------------------------------
        # 9. Diagnóstico → parte del cuerpo
        # -----------------------------------------------------

        if parte_cuerpo != (
            diagnostico_catalogo["parte_cuerpo"]
        ):
            errores.append(
                f"AT {id_accidente}: "
                f"parte del cuerpo '{parte_cuerpo}' "
                f"no coincide con el diagnóstico "
                f"'{codigo_diagnostico}'."
            )

    return errores


def validar_gravedad_accidentes(
    accidentes,
):
    """
    Valida la coherencia entre diagnóstico y clasificación
    de accidente grave según los criterios configurados.
    """

    errores = []

    for accidente in accidentes:

        id_accidente = accidente["id_accidente"]
        codigo_diagnostico = (
            accidente["codigo_diagnostico"]
        )
        accidente_grave = (
            accidente["accidente_grave"]
        )
        gravedad_accidente = (
            accidente["gravedad_accidente"]
        )
        criterio_gravedad = (
            accidente["criterio_gravedad"]
        )

        criterio = (
            CRITERIOS_GRAVEDAD_RES1401.get(
                codigo_diagnostico
            )
        )

        # -----------------------------------------------------
        # 1. Diagnóstico con criterio directo
        # -----------------------------------------------------

        if (
            criterio is not None
            and criterio["tipo"] == "DIRECTO"
        ):

            if accidente_grave is not True:
                errores.append(
                    f"AT {id_accidente}: "
                    f"el diagnóstico '{codigo_diagnostico}' "
                    "tiene criterio DIRECTO de accidente grave "
                    "pero accidente_grave no es True."
                )

            if gravedad_accidente != "Grave":
                errores.append(
                    f"AT {id_accidente}: "
                    f"el diagnóstico '{codigo_diagnostico}' "
                    "debe tener gravedad_accidente = 'Grave'."
                )

            if criterio_gravedad != criterio["criterio"]:
                errores.append(
                    f"AT {id_accidente}: "
                    "el criterio de gravedad no coincide "
                    "con la matriz normativa."
                )

            continue

        # -----------------------------------------------------
        # 2. Diagnóstico con criterio condicional
        # -----------------------------------------------------

        if (
            criterio is not None
            and criterio["tipo"] == "CONDICIONAL"
        ):

            if accidente_grave:

                if gravedad_accidente != "Grave":
                    errores.append(
                        f"AT {id_accidente}: "
                        "accidente_grave = True requiere "
                        "gravedad_accidente = 'Grave'."
                    )

                if criterio_gravedad != criterio["criterio"]:
                    errores.append(
                        f"AT {id_accidente}: "
                        "el criterio de gravedad no coincide "
                        "con el criterio configurado."
                    )

            else:

                if gravedad_accidente != "Leve":
                    errores.append(
                        f"AT {id_accidente}: "
                        "accidente_grave = False requiere "
                        "gravedad_accidente = 'Leve'."
                    )

                if criterio_gravedad is not None:
                    errores.append(
                        f"AT {id_accidente}: "
                        "un accidente condicional no grave "
                        "no debe registrar criterio_gravedad."
                    )

            continue

        # -----------------------------------------------------
        # 3. Diagnóstico sin criterio normativo
        # -----------------------------------------------------

        if accidente_grave:
            errores.append(
                f"AT {id_accidente}: "
                f"el diagnóstico '{codigo_diagnostico}' "
                "no tiene criterio configurado para "
                "accidente grave."
            )

        if gravedad_accidente != "Leve":
            errores.append(
                f"AT {id_accidente}: "
                f"el diagnóstico '{codigo_diagnostico}' "
                "sin criterio normativo debe ser Leve."
            )

        if criterio_gravedad is not None:
            errores.append(
                f"AT {id_accidente}: "
                f"el diagnóstico '{codigo_diagnostico}' "
                "no tiene criterio normativo, por lo que "
                "criterio_gravedad debe ser None."
            )

    return errores


def validar_accidentalidad_anual(
    trabajadores,
    accidentes,
    resultados_anuales,
    año,
):
    """
    Valida la coherencia integral de la accidentalidad anual.

    Comprueba:
    - que existan exactamente 12 meses;
    - que todos los accidentes correspondan al año;
    - que no existan IDs duplicados;
    - que los IDs sean consecutivos;
    - que los accidentes individuales sean coherentes;
    - que los accidentes estén asociados a trabajadores válidos;
    - que el resumen mensual coincida con los registros individuales;
    - que los accidentes esperados del resumen coincidan
      con el cálculo correspondiente.
    """

    errores = []

    # ---------------------------------------------------------
    # 1. Validar estructura del resumen anual
    # ---------------------------------------------------------

    if len(resultados_anuales) != 12:
        errores.append(
            "El resumen anual no contiene exactamente "
            f"12 registros mensuales. "
            f"Registros encontrados: {len(resultados_anuales)}."
        )

    fechas_resumen = [
        resultado.get("fecha")
        for resultado in resultados_anuales
    ]

    fechas_esperadas = [
        date(
            año,
            mes,
            1,
        )
        for mes in range(1, 13)
    ]

    if fechas_resumen != fechas_esperadas:
        errores.append(
            "Las fechas del resumen anual "
            "no corresponden exactamente "
            "a los 12 meses del año."
        )

    # ---------------------------------------------------------
    # 2. Validar que todos los accidentes pertenezcan al año
    # ---------------------------------------------------------

    for accidente in accidentes:

        fecha_accidente = accidente.get(
            "fecha_accidente"
        )

        if fecha_accidente is None:
            errores.append(
                f"Accidente {accidente.get('id_accidente')}: "
                "no tiene fecha_accidente."
            )
            continue

        if fecha_accidente.year != año:
            errores.append(
                f"Accidente {accidente.get('id_accidente')}: "
                f"fecha {fecha_accidente} "
                f"no pertenece al año {año}."
            )

    # ---------------------------------------------------------
    # 3. Validar IDs de accidentes
    # ---------------------------------------------------------

    ids_accidentes = [
        accidente.get("id_accidente")
        for accidente in accidentes
    ]

    ids_validos = [
        id_accidente
        for id_accidente in ids_accidentes
        if id_accidente is not None
    ]

    if len(ids_validos) != len(set(ids_validos)):
        errores.append(
            "Existen IDs de accidente duplicados."
        )

    ids_esperados = list(
        range(
            1,
            len(accidentes) + 1,
        )
    )

    if sorted(ids_validos) != ids_esperados:
        errores.append(
            "Los IDs de accidente no son "
            "consecutivos desde 1."
        )

    # ---------------------------------------------------------
    # 4. Validar coherencia de los accidentes individuales
    # ---------------------------------------------------------

    errores_basicos = validar_accidentes(
        trabajadores,
        accidentes,
    )

    errores_caracteristicas = (
        validar_accidentes_generados(
            accidentes
        )
    )

    errores_exposicion = (
        validar_exposicion_accidentes(
            trabajadores,
            accidentes,
        )
    )

    errores_gravedad = (
        validar_gravedad_accidentes(
            accidentes
        )
    )

    errores.extend(
        errores_basicos
    )

    errores.extend(
        errores_caracteristicas
    )

    errores.extend(
    errores_exposicion
    )

    errores.extend(
    errores_gravedad
    )

    # ---------------------------------------------------------
    # 5. Comparar registros individuales
    #    contra accidentes observados por mes
    # ---------------------------------------------------------

    for mes in range(1, 13):

        observados_generados = sum(
            1
            for accidente in accidentes
            if (
                accidente.get("fecha_accidente") is not None
                and accidente["fecha_accidente"].year == año
                and accidente["fecha_accidente"].month == mes
            )
        )

        resultados_mes = [
            resultado
            for resultado in resultados_anuales
            if (
                resultado.get("fecha")
                == date(año, mes, 1)
            )
        ]

        if not resultados_mes:
            errores.append(
                f"No existe resultado para "
                f"{año}-{mes:02d}."
            )
            continue

        resultado = resultados_mes[0]

        observados_resumen = resultado.get(
            "accidentes_observados"
        )

        if observados_resumen != observados_generados:
            errores.append(
                f"{año}-{mes:02d}: "
                f"el resumen registra "
                f"{observados_resumen} accidentes, "
                f"pero existen "
                f"{observados_generados} registros individuales."
            )

        # -----------------------------------------------------
        # 6. Validar accidentes esperados
        # -----------------------------------------------------

        accidentes_esperados = (
            calcular_accidentes_esperados_mes(
                trabajadores,
                date(año, mes, 1),
            )
        )

        esperado_resumen = resultado.get(
            "accidentes_esperados"
        )

        if not np.isclose(
            esperado_resumen,
            accidentes_esperados,
        ):
            errores.append(
                f"{año}-{mes:02d}: "
                f"accidentes_esperados inconsistente. "
                f"Esperado={accidentes_esperados}, "
                f"obtenido={esperado_resumen}."
            )

    return errores


def validar_exposicion_accidentes(
    trabajadores,
    accidentes,
):
    """
    Valida que cada accidente esté asociado a un trabajador
    que se encontraba activo y expuesto en la fecha del accidente.
    """

    errores = []

    trabajadores_por_id = {
        trabajador["id_trabajador"]: trabajador
        for trabajador in trabajadores
    }

    for accidente in accidentes:

        id_accidente = accidente["id_accidente"]
        id_trabajador = accidente["id_trabajador"]
        fecha_accidente = accidente["fecha_accidente"]

        trabajador = trabajadores_por_id.get(
            id_trabajador
        )

        if trabajador is None:
            errores.append(
                f"Accidente {id_accidente}: "
                f"el trabajador {id_trabajador} "
                "no existe en la población."
            )
            continue

        fecha_ingreso = trabajador["fecha_ingreso"]
        fecha_retiro = trabajador["fecha_retiro"]

        if fecha_accidente < fecha_ingreso:
            errores.append(
                f"Accidente {id_accidente}: "
                f"el trabajador {id_trabajador} "
                f"tuvo el accidente el {fecha_accidente}, "
                f"pero ingresó el {fecha_ingreso}."
            )

        if (
            fecha_retiro is not None
            and fecha_accidente >= fecha_retiro
        ):
            errores.append(
                f"Accidente {id_accidente}: "
                f"el trabajador {id_trabajador} "
                f"tuvo el accidente el {fecha_accidente}, "
                f"pero su retiro fue el {fecha_retiro}."
            )

    return errores


def validar_incapacidad_generada(
    accidentes,
    trabajadores,
):
    """
    Valida la coherencia de la incapacidad generada
    para cada accidente.

    Verifica:

    1. Escenario existente en DIAGNOSTICOS.
    2. Escenario permitido para el diagnóstico.
    3. Días de incapacidad válidos.
    4. Días dentro del rango del escenario.
    5. Coherencia NORMAL / VENTANA con la fecha de retiro.
    6. Aplicación correcta del límite por retiro.
    """

    errores = []

    trabajadores_por_id = {
        trabajador["id_trabajador"]: trabajador
        for trabajador in trabajadores
    }

    for accidente in accidentes:

        id_accidente = accidente["id_accidente"]

        id_trabajador = accidente["id_trabajador"]

        fecha_accidente = accidente["fecha_accidente"]

        codigo_diagnostico = (
            accidente["codigo_diagnostico"]
        )

        escenario_nivel = (
            accidente["escenario_incapacidad"]
        )

        dias_incapacidad = (
            accidente["dias_incapacidad"]
        )

        usar_peso_ventana = (
            accidente["usar_peso_ventana"]
        )

        # -----------------------------------------------------
        # 1. Trabajador existente
        # -----------------------------------------------------

        trabajador = trabajadores_por_id.get(
            id_trabajador
        )

        if trabajador is None:

            errores.append(
                f"AT {id_accidente}: "
                f"trabajador '{id_trabajador}' "
                "no existe."
            )

            continue

        fecha_retiro = trabajador.get(
            "fecha_retiro"
        )

        # -----------------------------------------------------
        # 2. Diagnóstico existente
        # -----------------------------------------------------

        diagnostico = DIAGNOSTICOS.get(
            codigo_diagnostico
        )

        if diagnostico is None:

            errores.append(
                f"AT {id_accidente}: "
                f"diagnóstico '{codigo_diagnostico}' "
                "no existe en DIAGNOSTICOS."
            )

            continue

        escenarios = diagnostico.get(
            "escenarios",
            []
        )

        # -----------------------------------------------------
        # 3. Escenario existente
        # -----------------------------------------------------

        escenario = next(
            (
                escenario
                for escenario in escenarios
                if escenario["nivel"]
                == escenario_nivel
            ),
            None,
        )

        if escenario is None:

            errores.append(
                f"AT {id_accidente}: "
                f"el escenario '{escenario_nivel}' "
                f"no está permitido para el diagnóstico "
                f"'{codigo_diagnostico}'."
            )

            continue

        # -----------------------------------------------------
        # 4. Validar días
        # -----------------------------------------------------

        if not isinstance(
            dias_incapacidad,
            int
        ):

            errores.append(
                f"AT {id_accidente}: "
                f"dias_incapacidad debe ser entero. "
                f"Valor: {dias_incapacidad!r}."
            )

            continue

        if dias_incapacidad < 1:

            errores.append(
                f"AT {id_accidente}: "
                f"dias_incapacidad debe ser >= 1. "
                f"Valor: {dias_incapacidad}."
            )

        dias_min = escenario["dias_min"]
        dias_max = escenario["dias_max"]

        # -----------------------------------------------------
        # 5. NORMAL / VENTANA
        # -----------------------------------------------------

        dias_hasta_retiro = None

        if fecha_retiro is not None:

            dias_hasta_retiro = (
                fecha_retiro
                - fecha_accidente
            ).days

        ventana_esperada = (
            dias_hasta_retiro is not None
            and 0 <= dias_hasta_retiro <= 180
        )

        if usar_peso_ventana != ventana_esperada:

            errores.append(
                f"AT {id_accidente}: "
                f"usar_peso_ventana="
                f"{usar_peso_ventana}, "
                f"pero según las fechas debería ser "
                f"{ventana_esperada}."
            )

        # -----------------------------------------------------
        # 6. Validar que los días estén dentro
        #    del escenario
        # -----------------------------------------------------

        # Si NO existe retiro o el retiro permite
        # completar el escenario, el rango normal aplica.

        if not ventana_esperada:

            if not (
                dias_min
                <= dias_incapacidad
                <= dias_max
            ):

                errores.append(
                    f"AT {id_accidente}: "
                    f"{dias_incapacidad} días "
                    f"fuera del rango del escenario "
                    f"'{escenario_nivel}' "
                    f"({dias_min}-{dias_max})."
                )

        # -----------------------------------------------------
        # 7. VENTANA DE RETIRO
        # -----------------------------------------------------

        else:

            # Si la incapacidad original cabe antes
            # del retiro, debe respetar el rango normal
            # del escenario.

            if dias_incapacidad > dias_hasta_retiro:

                errores.append(
                    f"AT {id_accidente}: "
                    f"días de incapacidad "
                    f"({dias_incapacidad}) "
                    f"superan el límite disponible "
                    f"hasta el retiro "
                    f"({dias_hasta_retiro})."
                )

            # El valor final debe ser positivo.
            if dias_incapacidad < 1:

                errores.append(
                    f"AT {id_accidente}: "
                    "la incapacidad quedó en "
                    "0 días después del ajuste por retiro."
                )

    return errores

