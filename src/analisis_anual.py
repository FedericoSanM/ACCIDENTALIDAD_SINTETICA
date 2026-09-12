from collections import Counter

from config.parametros import (
    FECHA_INICIO_ANALISIS,
    FECHA_CORTE,
    TOTAL_TRABAJADORES,
    SEED,
    DIAS_MAXIMOS_INCAPACIDAD,
    TASA_ANUAL_ACCIDENTALIDAD,
    ESTACIONALIDAD_MENSUAL,
)

from src.catalogos import DIAGNOSTICOS
from config.rutas import CARPETA_RESULTADOS

# ============================================================
# CONFIGURACIÓN DE SALIDA
# ============================================================

ARCHIVO_INFORME = (
    CARPETA_RESULTADOS
    / "validacion_anual.txt"
)

# ============================================================
# UTILIDADES
# ============================================================

def porcentaje(cantidad, total):
    """Calcula un porcentaje evitando división por cero."""
    if total == 0:
        return 0

    return cantidad / total * 100


def agregar_seccion(informe, titulo):
    """Agrega un encabezado de sección al informe."""
    informe.append("")
    informe.append("=" * 70)
    informe.append(titulo)
    informe.append("=" * 70)


def agregar_subseccion(informe, titulo):
    """Agrega un subtítulo al informe."""
    informe.append("")
    informe.append(titulo)
    informe.append("-" * len(titulo))


# ============================================================
# 1. RESUMEN GENERAL
# ============================================================

def analizar_resumen(trabajadores, accidentes):
    total_trabajadores = len(trabajadores)
    total_accidentes = len(accidentes)

    trabajadores_con_accidentes = len(
        {
            accidente["id_trabajador"]
            for accidente in accidentes
        }
    )

    trabajadores_sin_accidentes = (
        total_trabajadores
        - trabajadores_con_accidentes
    )

    return {
        "total_trabajadores": total_trabajadores,
        "total_accidentes": total_accidentes,
        "trabajadores_con_accidentes": (
            trabajadores_con_accidentes
        ),
        "trabajadores_sin_accidentes": (
            trabajadores_sin_accidentes
        ),
    }


# ============================================================
# 2. DISTRIBUCIÓN TEMPORAL
# ============================================================

def analizar_distribucion_temporal(accidentes):
    por_anio = Counter(
        accidente["fecha_accidente"].year
        for accidente in accidentes
    )

    por_mes = Counter(
        accidente["fecha_accidente"].month
        for accidente in accidentes
    )

    return por_anio, por_mes


# ============================================================
# 3. DISTRIBUCIONES DE ACCIDENTALIDAD
# ============================================================

def analizar_distribuciones(accidentes):
    total = len(accidentes)

    por_tipo = Counter(
        accidente["tipo_accidente"]
        for accidente in accidentes
    )

    por_mecanismo = Counter(
        accidente["mecanismo"]
        for accidente in accidentes
    )

    por_diagnostico = Counter(
        accidente["codigo_diagnostico"]
        for accidente in accidentes
    )

    por_gravedad = Counter(
        accidente["gravedad_accidente"]
        for accidente in accidentes
    )

    return {
        "tipo": por_tipo,
        "mecanismo": por_mecanismo,
        "diagnostico": por_diagnostico,
        "gravedad": por_gravedad,
        "total": total,
    }


# ============================================================
# 4. INCAPACIDAD
# ============================================================

def analizar_incapacidades(accidentes, trabajadores):
    trabajadores_por_id = {
        trabajador["id_trabajador"]: trabajador
        for trabajador in trabajadores
    }

    dias = [
        accidente["dias_incapacidad"]
        for accidente in accidentes
        if accidente["dias_incapacidad"] is not None
    ]

    casos_normal = 0
    casos_ventana = 0
    errores = []

    for accidente in accidentes:
        dias_incapacidad = accidente["dias_incapacidad"]

        if not isinstance(dias_incapacidad, int):
            errores.append(
                f"Accidente {accidente['id_accidente']}: "
                "días de incapacidad no entero."
            )
            continue

        if not 1 <= dias_incapacidad <= DIAS_MAXIMOS_INCAPACIDAD:
            errores.append(
                f"Accidente {accidente['id_accidente']}: "
                f"días de incapacidad fuera del rango "
                f"1-{DIAS_MAXIMOS_INCAPACIDAD}."
            )
            continue

        trabajador = trabajadores_por_id.get(
            accidente["id_trabajador"]
        )

        if trabajador is None:
            errores.append(
                f"Accidente {accidente['id_accidente']}: "
                "trabajador inexistente."
            )
            continue

        fecha_retiro = trabajador["fecha_retiro"]

        if fecha_retiro is None:
            casos_normal += 1
            continue

        dias_disponibles = (
            fecha_retiro
            - accidente["fecha_accidente"]
        ).days

        if dias_disponibles <= 180:
            casos_ventana += 1
        else:
            casos_normal += 1

        if dias_incapacidad > dias_disponibles:
            errores.append(
                f"Accidente {accidente['id_accidente']}: "
                f"{dias_incapacidad} días de incapacidad "
                f"superan los {dias_disponibles} días "
                "disponibles antes del retiro."
            )

    total_dias = sum(dias)

    return {
        "accidentes_analizados": len(accidentes),
        "accidentes_con_incapacidad": len(dias),
        "dias_totales": total_dias,
        "promedio": (
            total_dias / len(dias)
            if dias
            else 0
        ),
        "minimo": min(dias) if dias else 0,
        "maximo": max(dias) if dias else 0,
        "normal": casos_normal,
        "ventana": casos_ventana,
        "errores": errores,
    }


# ============================================================
# 5. REINCIDENCIA
# ============================================================

def analizar_reincidencia(trabajadores, accidentes):
    accidentes_por_trabajador = Counter(
        accidente["id_trabajador"]
        for accidente in accidentes
    )

    for trabajador in trabajadores:
        id_trabajador = trabajador["id_trabajador"]

        if id_trabajador not in accidentes_por_trabajador:
            accidentes_por_trabajador[id_trabajador] = 0

    distribucion = Counter(
        accidentes_por_trabajador.values()
    )

    trabajadores_accidentados = sum(
        1
        for cantidad in accidentes_por_trabajador.values()
        if cantidad > 0
    )

    trabajadores_reincidentes = sum(
        distribucion[cantidad]
        for cantidad in distribucion
        if cantidad >= 2
    )

    max_accidentes = max(
        accidentes_por_trabajador.values()
    )

    return {
        "accidentes_por_trabajador":
            accidentes_por_trabajador,
        "distribucion": distribucion,
        "trabajadores_accidentados":
            trabajadores_accidentados,
        "trabajadores_reincidentes":
            trabajadores_reincidentes,
        "max_accidentes": max_accidentes,
    }


# ============================================================
# 6. COBERTURA DE DIAGNÓSTICOS
# ============================================================

def analizar_cobertura_diagnosticos(accidentes):
    diagnosticos_generados = {
        accidente["codigo_diagnostico"]
        for accidente in accidentes
    }

    diagnosticos_configurados = set(DIAGNOSTICOS)

    utilizados = (
        diagnosticos_generados
        & diagnosticos_configurados
    )

    no_utilizados = (
        diagnosticos_configurados
        - diagnosticos_generados
    )

    diagnosticos_no_configurados = (
        diagnosticos_generados
        - diagnosticos_configurados
    )

    return {
        "configurados": len(diagnosticos_configurados),
        "utilizados": len(utilizados),
        "no_utilizados": no_utilizados,
        "no_configurados": diagnosticos_no_configurados,
    }


# ============================================================
# 7. PROBABILIDAD EFECTIVA DE DIAGNÓSTICOS
# ============================================================

def analizar_probabilidad_diagnosticos(accidentes):
    conteo = Counter(
        accidente["codigo_diagnostico"]
        for accidente in accidentes
    )

    total = len(accidentes)

    resultados = []

    for codigo, cantidad in conteo.most_common():
        resultados.append(
            {
                "codigo": codigo,
                "cantidad": cantidad,
                "porcentaje": porcentaje(
                    cantidad,
                    total,
                ),
            }
        )

    return resultados


# ============================================================
# 8. ANÁLISIS DE GRAVEDAD POR TIPO
# ============================================================

def analizar_gravedad_por_tipo(accidentes):
    resultado = {}

    tipos = {
        accidente["tipo_accidente"]
        for accidente in accidentes
    }

    for tipo in sorted(tipos):
        accidentes_tipo = [
            accidente
            for accidente in accidentes
            if accidente["tipo_accidente"] == tipo
        ]

        graves = sum(
            1
            for accidente in accidentes_tipo
            if accidente["gravedad_accidente"] == "Grave"
        )

        total = len(accidentes_tipo)

        resultado[tipo] = {
            "total": total,
            "graves": graves,
            "porcentaje_graves": porcentaje(
                graves,
                total,
            ),
        }

    return resultado


# ============================================================
# 9. CONSTRUCCIÓN DEL INFORME
# ============================================================

def construir_informe(
    trabajadores,
    accidentes,
):
    resumen = analizar_resumen(
        trabajadores,
        accidentes,
    )

    por_anio, por_mes = (
        analizar_distribucion_temporal(accidentes)
    )

    distribuciones = analizar_distribuciones(
        accidentes
    )

    incapacidades = analizar_incapacidades(
        accidentes,
        trabajadores,
    )

    reincidencia = analizar_reincidencia(
        trabajadores,
        accidentes,
    )

    cobertura = analizar_cobertura_diagnosticos(
        accidentes
    )

    probabilidades = analizar_probabilidad_diagnosticos(
        accidentes
    )

    gravedad_tipo = analizar_gravedad_por_tipo(
        accidentes
    )

    informe = []

    # --------------------------------------------------------
    # PORTADA
    # --------------------------------------------------------

    informe.append("=" * 70)
    informe.append(
        "VALIDACIÓN ANUAL Y ANÁLISIS ESTADÍSTICO"
    )
    informe.append("=" * 70)
    informe.append(
        f"Período de análisis: "
        f"{FECHA_INICIO_ANALISIS} a {FECHA_CORTE}"
    )
    informe.append(
        f"Semilla utilizada: {SEED}"
    )
    informe.append(
        f"Trabajadores configurados: "
        f"{TOTAL_TRABAJADORES}"
    )

    # --------------------------------------------------------
    # RESUMEN
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "1. RESUMEN GENERAL",
    )

    informe.append(
        f"Trabajadores generados: "
        f"{resumen['total_trabajadores']}"
    )

    informe.append(
        f"Accidentes generados: "
        f"{resumen['total_accidentes']}"
    )

    informe.append(
        f"Trabajadores con accidentes: "
        f"{resumen['trabajadores_con_accidentes']}"
    )

    informe.append(
        f"Trabajadores sin accidentes: "
        f"{resumen['trabajadores_sin_accidentes']}"
    )

    porcentaje_accidentados = porcentaje(
    resumen["trabajadores_con_accidentes"],
    resumen["total_trabajadores"],
    )

    informe.append(
        "Porcentaje de trabajadores accidentados: "
        f"{porcentaje_accidentados:.2f}%"
    )

    informe.append(
        "Promedio de accidentes por trabajador: "
        f"{resumen['total_accidentes'] / resumen['total_trabajadores']:.2f}"
    )

    if resumen["trabajadores_con_accidentes"]:
        informe.append(
            "Promedio de accidentes por trabajador "
            "accidentado: "
            f"{resumen['total_accidentes'] / resumen['trabajadores_con_accidentes']:.2f}"
        )

    # --------------------------------------------------------
    # DISTRIBUCIÓN ANUAL
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "2. ACCIDENTES POR AÑO",
    )

    for anio, cantidad in sorted(
        por_anio.items()
    ):
        informe.append(
            f"{anio}: "
            f"{cantidad} accidentes "
            f"({porcentaje(cantidad, len(accidentes)):.2f}%)"
        )

    # --------------------------------------------------------
    # DISTRIBUCIÓN MENSUAL
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "3. ACCIDENTES POR MES",
    )

    nombres_meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    for mes in range(1, 13):
        cantidad = por_mes.get(mes, 0)

        informe.append(
            f"{nombres_meses[mes]:12} "
            f"{cantidad:5d} "
            f"({porcentaje(cantidad, len(accidentes)):6.2f}%)"
        )

    # --------------------------------------------------------
    # TIPO
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "4. ACCIDENTES POR TIPO DE ACCIDENTE",
    )

    for tipo, cantidad in (
        distribuciones["tipo"].most_common()
    ):
        informe.append(
            f"{tipo}: "
            f"{cantidad} "
            f"({porcentaje(cantidad, len(accidentes)):.2f}%)"
        )

    # --------------------------------------------------------
    # MECANISMO
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "5. ACCIDENTES POR MECANISMO",
    )

    for mecanismo, cantidad in (
        distribuciones["mecanismo"].most_common()
    ):
        informe.append(
            f"{mecanismo}: "
            f"{cantidad} "
            f"({porcentaje(cantidad, len(accidentes)):.2f}%)"
        )

    # --------------------------------------------------------
    # DIAGNÓSTICO
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "6. ACCIDENTES POR DIAGNÓSTICO",
    )

    for resultado in probabilidades:
        codigo = resultado["codigo"]
        cantidad = resultado["cantidad"]
        porcentaje_diagnostico = (
            resultado["porcentaje"]
        )

        descripcion = DIAGNOSTICOS.get(
            codigo,
            {}
        ).get(
            "descripcion",
            "Sin descripción",
        )

        informe.append(
            f"{codigo:7} "
            f"{cantidad:5d} "
            f"({porcentaje_diagnostico:6.2f}%) | "
            f"{descripcion}"
        )

    # --------------------------------------------------------
    # GRAVEDAD
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "7. DISTRIBUCIÓN DE GRAVEDAD",
    )

    for gravedad, cantidad in (
        distribuciones["gravedad"].most_common()
    ):
        informe.append(
            f"{gravedad}: "
            f"{cantidad} "
            f"({porcentaje(cantidad, len(accidentes)):.2f}%)"
        )

    # --------------------------------------------------------
    # GRAVEDAD POR TIPO
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "8. ACCIDENTES GRAVES POR TIPO",
    )

    for tipo, datos in gravedad_tipo.items():
        informe.append(
            f"{tipo}: "
            f"{datos['graves']} graves de "
            f"{datos['total']} accidentes "
            f"({datos['porcentaje_graves']:.2f}%)"
        )

    # --------------------------------------------------------
    # INCAPACIDAD
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "9. INCAPACIDAD",
    )

    informe.append(
        f"Accidentes analizados: "
        f"{incapacidades['accidentes_analizados']}"
    )

    informe.append(
        f"Accidentes con incapacidad: "
        f"{incapacidades['accidentes_con_incapacidad']}"
    )

    informe.append(
        f"Días totales de incapacidad: "
        f"{incapacidades['dias_totales']}"
    )

    informe.append(
        f"Promedio de días: "
        f"{incapacidades['promedio']:.2f}"
    )

    informe.append(
        f"Mínimo de días: "
        f"{incapacidades['minimo']}"
    )

    informe.append(
        f"Máximo de días: "
        f"{incapacidades['maximo']}"
    )

    agregar_subseccion(
        informe,
        "Distribución NORMAL / VENTANA",
    )

    total_incapacidades = (
        incapacidades["normal"]
        + incapacidades["ventana"]
    )

    informe.append(
        f"NORMAL: "
        f"{incapacidades['normal']} "
        f"({porcentaje(incapacidades['normal'], total_incapacidades):.2f}%)"
    )

    informe.append(
        f"VENTANA: "
        f"{incapacidades['ventana']} "
        f"({porcentaje(incapacidades['ventana'], total_incapacidades):.2f}%)"
    )

    # --------------------------------------------------------
    # REINCIDENCIA
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "10. REINCIDENCIA",
    )

    informe.append(
        f"Trabajadores accidentados: "
        f"{reincidencia['trabajadores_accidentados']}"
    )

    informe.append(
        f"Trabajadores reincidentes: "
        f"{reincidencia['trabajadores_reincidentes']}"
    )

    informe.append(
        "Porcentaje de reincidencia entre "
        "trabajadores accidentados: "
        f"{porcentaje(
        reincidencia['trabajadores_reincidentes'],
        reincidencia['trabajadores_accidentados']
        ):.2f}%"
    )

    informe.append(
        f"Máximo de accidentes de un trabajador: "
        f"{reincidencia['max_accidentes']}"
    )

    agregar_subseccion(
        informe,
        "Distribución de accidentes por trabajador",
    )

    for cantidad in sorted(
        reincidencia["distribucion"]
    ):
        trabajadores_cantidad = (
            reincidencia["distribucion"][cantidad]
        )

        informe.append(
            f"{cantidad} accidente(s): "
            f"{trabajadores_cantidad} trabajadores "
            f"({porcentaje(
            trabajadores_cantidad,
            len(trabajadores)
            ):.2f}%)"
        )

    # --------------------------------------------------------
    # COBERTURA
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "11. COBERTURA DE DIAGNÓSTICOS",
    )

    informe.append(
        f"Diagnósticos configurados: "
        f"{cobertura['configurados']}"
    )

    informe.append(
        f"Diagnósticos utilizados: "
        f"{cobertura['utilizados']}"
    )

    informe.append(
        "Porcentaje de diagnósticos configurados "
        "utilizados: "
        f"{porcentaje(
        cobertura['utilizados'],
        cobertura['configurados']
        ):.2f}%"
    )

    informe.append(
        f"Diagnósticos configurados no observados: "
        f"{len(cobertura['no_utilizados'])}"
    )

    if cobertura["no_utilizados"]:
        informe.append(
            "Códigos no observados: "
            + ", ".join(
                sorted(cobertura["no_utilizados"])
            )
        )

    informe.append(
        f"Diagnósticos generados no configurados: "
        f"{len(cobertura['no_configurados'])}"
    )

    # --------------------------------------------------------
    # PROBABILIDAD EFECTIVA
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "12. PROBABILIDAD EFECTIVA DE DIAGNÓSTICOS",
    )

    informe.append(
        "La siguiente distribución muestra la frecuencia "
        "observada de cada diagnóstico en la corrida."
    )

    for resultado in probabilidades:
        informe.append(
            f"{resultado['codigo']:7} "
            f"{resultado['cantidad']:5d} "
            f"{resultado['porcentaje']:6.2f}%"
        )

    # --------------------------------------------------------
    # PARÁMETROS ESPERADOS
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "13. PARÁMETROS UTILIZADOS",
    )

    informe.append(
        "TASA ANUAL DE ACCIDENTALIDAD"
    )

    for anio, tasa in sorted(
        TASA_ANUAL_ACCIDENTALIDAD.items()
    ):
        informe.append(
            f"{anio}: {tasa:.2%}"
        )

    agregar_subseccion(
        informe,
        "ESTACIONALIDAD MENSUAL",
    )

    for mes in range(1, 13):
        informe.append(
            f"{nombres_meses[mes]:12} "
            f"{ESTACIONALIDAD_MENSUAL[mes]:.2f}"
        )

    # --------------------------------------------------------
    # CONCLUSIÓN
    # --------------------------------------------------------

    agregar_seccion(
        informe,
        "14. RESULTADO DEL ANÁLISIS",
    )

    if incapacidades["errores"]:
        informe.append(
            "Se encontraron inconsistencias en el "
            "análisis de incapacidades."
        )

        for error in incapacidades["errores"]:
            informe.append(
                f"- {error}"
            )
    else:
        informe.append(
            "No se encontraron inconsistencias "
            "en el análisis de incapacidades."
        )

    informe.append("")
    informe.append(
        "Este informe es descriptivo y muestra el "
        "comportamiento de una corrida del generador."
    )

    informe.append(
        "Las reglas de operación del generador son "
        "validadas mediante la suite de pruebas pytest."
    )

    informe.append("")
    informe.append("=" * 70)
    informe.append("FIN DEL INFORME")
    informe.append("=" * 70)

    return "\n".join(informe)


# ============================================================
# GENERACIÓN DEL INFORME
# ============================================================

def generar_informe_anual(
    trabajadores,
    accidentes,
):
    """
    Genera el informe anual utilizando los mismos datos
    recibidos desde el flujo principal del proyecto.

    No genera trabajadores ni accidentes nuevos.
    """

    if hasattr(trabajadores, "to_dict"):
        trabajadores = trabajadores.to_dict(
            orient = "records"
        )

    if hasattr(accidentes, "to_dict"):
        accidentes = accidentes.to_dict(
            orient = "records"
        )

    informe = construir_informe(
        trabajadores,
        accidentes,
    )

    CARPETA_RESULTADOS.mkdir(
        parents = True,
        exist_ok = True,
    )

    ARCHIVO_INFORME.write_text(
        informe,
        encoding = "utf-8",
    )

    return ARCHIVO_INFORME