SEED = 42

FECHA_INICIO_EMPRESA = "2016-07-01"

FECHA_INICIO_ANALISIS = "2021-07-01"

FECHA_CORTE = "2026-06-30"

ANIO_BASE_SALARIAL = 2016

INCREMENTO_SALARIAL_ANUAL = 0.06

TOTAL_TRABAJADORES = 800

DIAS_MAXIMOS_INCAPACIDAD = 180

TASA_ANUAL_ACCIDENTALIDAD = {
    2016: 0.06,
    2017: 0.07,
    2018: 0.05,
    2019: 0.08,
    2020: 0.09,
    2021: 0.15,
    2022: 0.19,
    2023: 0.24,
    2024: 0.31,
    2025: 0.26,
    2026: 0.20,
}

ESTACIONALIDAD_MENSUAL = {
    1: 0.85,
    2: 0.90,
    3: 1.00,
    4: 0.95,
    5: 1.10,
    6: 1.15,
    7: 1.05,
    8: 0.95,
    9: 1.20,
    10: 1.10,
    11: 0.90,
    12: 0.85,
}

CONFIG_EVENTOS_EXTRAORDINARIOS = {
    "habilitada": True,

    # Probabilidad de que exista al menos un evento
    # extraordinario durante un año.
    "probabilidad_anual": 0.25,

    # Máximo de eventos extraordinarios que pueden
    # ocurrir en un mismo año.
    "max_eventos_anuales": 1,

    # Evento puntual:
    # ocurre en un solo día y puede afectar
    # simultáneamente a varios trabajadores.
    "puntual": {
        "duracion_dias": 1,
        "afectados_min": 5,
        "afectados_max": 20,
    },

    # Evento temporal:
    # fenómeno extraordinario que puede mantenerse
    # durante varios días o semanas.
    "temporal": {
        "duracion_min_dias": 7,
        "duracion_max_dias": 30,
        "afectados_min": 5,
        "afectados_max": 20,
    },
}

PROBABILIDAD_CRITERIO_GRAVEDAD_RES1401 = 0.02