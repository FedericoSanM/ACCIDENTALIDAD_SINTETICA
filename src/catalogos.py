GENEROS = [
    "Masculino",
    "Femenino",
    "LGTBIQ+",
    "No especificado"
]

CIUDADES_DEPARTAMENTOS = {
    "Bogotá D.C.": "Bogotá D.C.",
    "Medellín": "Antioquia",
    "Cali": "Valle del Cauca",
    "Barranquilla": "Atlántico",
    "Cartagena": "Bolívar",
    "Bucaramanga": "Santander",
    "Pereira": "Risaralda",
    "Manizales": "Caldas",
    "Ibagué": "Tolima",
    "Villavicencio": "Meta",
    "Cúcuta": "Norte de Santander",
    "Pasto": "Nariño",
    "Neiva": "Huila",
    "Armenia": "Quindío",
    "Santa Marta": "Magdalena",
}

CARGOS = {
    "Gerente General": {
        "nivel": "Directivo",
        "areas": ["Dirección y Planeación"],
    },
    "Director Operativo": {
        "nivel": "Directivo",
        "areas": ["Dirección y Planeación", "Operaciones"],
    },
    "Director Comercial": {
        "nivel": "Directivo",
        "areas": ["Dirección y Planeación", "Comercial"],
    },
    "Coordinador Administrativo": {
        "nivel": "Coordinador",
        "areas": ["Administración y Finanzas"],
    },
    "Coordinador SST": {
        "nivel": "Coordinador",
        "areas": ["SST y Gestión Integral"],
    },
    "Coordinador Logístico": {
        "nivel": "Coordinador",
        "areas": ["Operaciones", "Proyectos"],
    },
    "Coordinador de Proyectos": {
        "nivel": "Coordinador",
        "areas": ["Proyectos"],
    },
    "Profesional de Recursos Humanos": {
        "nivel": "Profesional",
        "areas": ["Gestión Humana"],
    },
    "Profesional de Compras": {
        "nivel": "Profesional",
        "areas": ["Administración y Finanzas", "Proyectos"],
    },
    "Profesional de Calidad": {
        "nivel": "Profesional",
        "areas": ["SST y Gestión Integral", "Proyectos"],
    },
    "Ingeniero de Proyectos": {
        "nivel": "Profesional",
        "areas": ["Proyectos", "Operaciones"],
    },
    "Vendedor": {
        "nivel": "Comercial",
        "areas": ["Comercial"],
    },
    "Técnico de Mantenimiento": {
        "nivel": "Técnico",
        "areas": ["Operaciones", "Proyectos"],
    },
    "Técnico de Seguridad Industrial": {
        "nivel": "Técnico",
        "areas": ["SST y Gestión Integral", "Operaciones"],
    },
    "Conductor": {
        "nivel": "Operativo",
        "areas": ["Operaciones", "Proyectos"],
    },
    "Operador de Máquina": {
        "nivel": "Operativo",
        "areas": ["Operaciones"],
    },
    "Ayudante de Obra": {
        "nivel": "Operativo",
        "areas": ["Proyectos", "Operaciones"],
    },
    "Auxiliar Contable": {
        "nivel": "Auxiliar",
        "areas": ["Administración y Finanzas"],
    },
    "Auxiliar Administrativo": {
        "nivel": "Auxiliar",
        "areas": ["Administración y Finanzas", "Gestión Humana"],
    },
    "Auxiliar de Bodega": {
        "nivel": "Auxiliar",
        "areas": ["Operaciones", "Proyectos"],
    },
}

SALARIOS_BASE_POR_CARGO = {

    # -----------------------------------------------------
    # DIRECTIVOS
    # -----------------------------------------------------

    "Gerente General": 8_000_000,

    "Director Operativo": 6_000_000,

    "Director Comercial": 5_500_000,


    # -----------------------------------------------------
    # COORDINADORES
    # -----------------------------------------------------

    "Coordinador Administrativo": 3_500_000,

    "Coordinador SST": 3_800_000,

    "Coordinador Logístico": 3_300_000,

    "Coordinador de Proyectos": 4_000_000,


    # -----------------------------------------------------
    # PROFESIONALES
    # -----------------------------------------------------

    "Profesional de Recursos Humanos": 3_000_000,

    "Profesional de Compras": 2_800_000,

    "Profesional de Calidad": 3_200_000,

    "Ingeniero de Proyectos": 4_000_000,


    # -----------------------------------------------------
    # COMERCIAL
    # -----------------------------------------------------

    "Vendedor": 2_000_000,


    # -----------------------------------------------------
    # TÉCNICOS
    # -----------------------------------------------------

    "Técnico de Mantenimiento": 2_200_000,

    "Técnico de Seguridad Industrial": 2_300_000,


    # -----------------------------------------------------
    # OPERATIVOS
    # -----------------------------------------------------

    "Conductor": 1_500_000,

    "Operador de Máquina": 1_600_000,

    "Ayudante de Obra": 1_350_000,


    # -----------------------------------------------------
    # AUXILIARES
    # -----------------------------------------------------

    "Auxiliar Contable": 1_500_000,

    "Auxiliar Administrativo": 1_400_000,

    "Auxiliar de Bodega": 1_350_000,
}

AREAS_PROCESOS = [
    "Dirección y Planeación",
    "Comercial",
    "Operaciones",
    "Proyectos",
    "Gestión Humana",
    "Administración y Finanzas",
    "SST y Gestión Integral",
]

TIPOS_VINCULACION = [
    "Término Indefinido",
    "Fijo a 3 meses",
    "Fijo a 6 meses",
    "Fijo a 1 año",
    "Obra / Labor",
    "Prestación de Servicios",
    "En Misión",
    "Aprendizaje",    
]

TIPOS_ACCIDENTE = [
    "Caída de persona",
    "Caída de objeto",
    "Pisada o golpe",
    "Atrapamiento",
    "Sobreesfuerzo",
    "Temperatura extrema",
    "Contacto con electricidad",
    "Sustancias nocivas",
    "Elemento cortopunzante",
    "Otro",
    "Accidente de tránsito",
    "Violencia",
    "Mordedura o picadura",
    "Exposición o contacto con agente biológico",    
]

MECANISMOS = {
    "Caída de persona": [
        "Caída a nivel",
        "Caída a diferente nivel",
        "Resbalón o tropiezo",
    ],
    "Caída de objeto": [
        "Caída de objeto desde altura",
        "Desprendimiento de objeto",
        "Golpe por objeto en movimiento",
    ],
    "Pisada o golpe": [
        "Golpe contra objeto",
        "Golpeado por objeto",
        "Pisada sobre superficie u objeto",
    ],
    "Atrapamiento": [
        "Atrapamiento entre objetos",
        "Atrapamiento en máquina o equipo",
        "Aplastamiento",
    ],
    "Sobreesfuerzo": [
        "Levantamiento de carga",
        "Empuje o tracción",
        "Movimiento repetitivo",
        "Postura forzada",
    ],
    "Temperatura extrema": [
        "Contacto con superficie caliente",
        "Contacto con superficie fría",
        "Exposición a calor",
        "Exposición a frío",
    ],
    "Contacto con electricidad": [
        "Contacto directo",
        "Contacto indirecto",
        "Arco eléctrico",
    ],
    "Sustancias nocivas": [
        "Contacto con sustancia química",
        "Inhalación",
        "Ingestión",
        "Salpicadura",
    ],
    "Elemento cortopunzante": [
        "Corte",
        "Punción",
        "Perforación",
    ],
    "Otro": [
        "Mecanismo no especificado",
        "Otro mecanismo",
    ],
    "Accidente de tránsito": [
        "Colisión",
        "Atropellamiento",
        "Volcamiento",
        "Caída de vehículo",
    ],
    "Violencia": [
        "Agresión física",
        "Agresión con objeto",
    ],
    "Mordedura o picadura": [
        "Mordedura",
        "Picadura",
    ],
    "Exposición o contacto con agente biológico": [
        "Contacto con material biológico",
        "Exposición a agente biológico",
        "Pinchazo con material contaminado",
    ],
}

AGENTES_LESION = [
    "Ambiente de trabajo",
    "Superficies de tránsito",
    "Escaleras",
    "Andamios o plataformas",
    "Materiales o sustancias",
    "Máquinas o equipos",
    "Herramientas o utensilios",
    "Otros agentes",
    "Aparatos",
    "Instalaciones eléctricas",
    "Agentes químicos",
    "Agentes no clasificados",
    "Medios de transporte",
    "Animales",
    "Agentes biológicos",
]

COMPATIBILIDAD_MECANISMO_AGENTE = {

    "Caída a nivel": [
        "Ambiente de trabajo",
        "Superficies de tránsito",
    ],

    "Caída a diferente nivel": [
        "Ambiente de trabajo",
        "Escaleras",
        "Andamios o plataformas",
    ],

    "Resbalón o tropiezo": [
        "Ambiente de trabajo",
        "Superficies de tránsito",
    ],

    "Caída de objeto desde altura": [
        "Materiales o sustancias",
        "Máquinas o equipos",
        "Herramientas o utensilios",
    ],

    "Desprendimiento de objeto": [
        "Materiales o sustancias",
        "Máquinas o equipos",
        "Herramientas o utensilios",
    ],

    "Golpe por objeto en movimiento": [
        "Materiales o sustancias",
        "Máquinas o equipos",
        "Herramientas o utensilios",
    ],

    "Golpe contra objeto": [
        "Ambiente de trabajo",
        "Máquinas o equipos",
        "Materiales o sustancias",
        "Herramientas o utensilios",
    ],

    "Golpeado por objeto": [
        "Máquinas o equipos",
        "Materiales o sustancias",
        "Herramientas o utensilios",
    ],

    "Pisada sobre superficie u objeto": [
        "Ambiente de trabajo",
        "Materiales o sustancias",
    ],

    "Atrapamiento entre objetos": [
        "Máquinas o equipos",
        "Herramientas o utensilios",
        "Materiales o sustancias",
    ],

    "Atrapamiento en máquina o equipo": [
        "Máquinas o equipos",
        "Herramientas o utensilios",
    ],

    "Aplastamiento": [
        "Máquinas o equipos",
        "Materiales o sustancias",
        "Herramientas o utensilios",
    ],

    "Levantamiento de carga": [
        "Materiales o sustancias",
        "Herramientas o utensilios",
    ],

    "Empuje o tracción": [
        "Materiales o sustancias",
        "Herramientas o utensilios",
    ],

    "Movimiento repetitivo": [
        "Herramientas o utensilios",
        "Máquinas o equipos",
        "Ambiente de trabajo",
    ],

    "Postura forzada": [
        "Ambiente de trabajo",
        "Herramientas o utensilios",
        "Máquinas o equipos",
    ],

    "Contacto con superficie caliente": [
        "Ambiente de trabajo",
        "Materiales o sustancias",
    ],

    "Contacto con superficie fría": [
        "Ambiente de trabajo",
        "Materiales o sustancias",
    ],

    "Exposición a calor": [
        "Ambiente de trabajo",
    ],

    "Exposición a frío": [
        "Ambiente de trabajo",
    ],

    "Contacto directo": [
        "Instalaciones eléctricas",
        "Aparatos",
        "Máquinas o equipos",
    ],

    "Contacto indirecto": [
        "Instalaciones eléctricas",
        "Aparatos",
        "Máquinas o equipos",
    ],

    "Arco eléctrico": [
        "Instalaciones eléctricas",
        "Aparatos",
    ],

    "Contacto con sustancia química": [
        "Agentes químicos",
        "Materiales o sustancias",
    ],

    "Inhalación": [
        "Agentes químicos",
        "Materiales o sustancias",
    ],

    "Ingestión": [
        "Materiales o sustancias",
        "Agentes químicos",
    ],

    "Salpicadura": [
        "Agentes químicos",
        "Materiales o sustancias",
    ],

    "Corte": [
        "Herramientas o utensilios",
        "Máquinas o equipos",
        "Materiales o sustancias",
    ],

    "Punción": [
        "Herramientas o utensilios",
        "Materiales o sustancias",
    ],

    "Perforación": [
        "Herramientas o utensilios",
        "Máquinas o equipos",
        "Materiales o sustancias",
    ],

    "Mecanismo no especificado": [
        "Otros agentes",
        "Agentes no clasificados",
    ],

    "Otro mecanismo": [
        "Otros agentes",
        "Agentes no clasificados",
    ],

    "Colisión": [
        "Medios de transporte",
        "Ambiente de trabajo",
    ],

    "Atropellamiento": [
        "Medios de transporte",
        "Ambiente de trabajo",
    ],

    "Volcamiento": [
        "Medios de transporte",
    ],

    "Caída de vehículo": [
        "Medios de transporte",
        "Ambiente de trabajo",
    ],

    "Agresión física": [
        "Otros agentes",
        "Agentes no clasificados",
    ],

    "Agresión con objeto": [
        "Otros agentes",
        "Agentes no clasificados",
    ],

    "Mordedura": [
        "Animales",
        "Otros agentes",
    ],

    "Picadura": [
        "Animales",
        "Otros agentes",
    ],

    "Contacto con material biológico": [
        "Materiales o sustancias",
        "Agentes biológicos",
    ],

    "Exposición a agente biológico": [
        "Materiales o sustancias",
        "Agentes biológicos",
    ],

    "Pinchazo con material contaminado": [
        "Materiales o sustancias",
        "Agentes biológicos",
    ],
}

TIPOS_LESION = [
    "Fractura",
    "Luxación",
    "Esguince",
    "Trauma interno",
    "Amputación",
    "Herida",
    "Trauma superficial",
    "Contusión",
    "Quemadura",
    "Envenenamiento",
    "Efecto del tiempo o clima",
    "Asfixia",
    "Efecto de la electricidad",
    "Efecto de la radiación",
    "Lesiones múltiples",
    "Aplastamiento",
    "Congelación",
    "Efecto del calor",
    "Shock",
    "Reacción sistémica",
    "Otro",
]

PARTES_CUERPO = [
    "Cabeza",
    "Ojo",
    "Cuello",
    "Tronco",
    "Tórax",
    "Abdomen",
    "Miembros superiores",
    "Manos",
    "Miembros inferiores",
    "Pies",
    "Ubicaciones múltiples",
    "Lesiones generales",
]

DIAGNOSTICOS = {
    "S00.0": {
        "descripcion": 'Lesión superficial del cuero cabelludo',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Trauma superficial",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "S00.8": {
        "descripcion": 'Lesiones superficiales de otras partes de la cabeza',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Trauma superficial",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "S01.0": {
        "descripcion": 'Herida abierta del cuero cabelludo',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "S01.8": {
        "descripcion": 'Herida abierta de otras partes de la cabeza',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "S13.4": {
        "descripcion": 'Esguince y distensión de la columna cervical',
        "severidad_clinica": "baja",
        "tipo_lesion": "Esguince",
        "parte_cuerpo": "Cuello",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S16.1": {
        "descripcion": 'Lesión de músculo y tendón a nivel del cuello',
        "severidad_clinica": "baja",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Cuello",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S20.2": {
        "descripcion": 'Contusión del tórax',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Tórax",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S30.0": {
        "descripcion": 'Contusión de la región lumbar y pelvis',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Tronco",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S40.0": {
        "descripcion": 'Contusión del hombro y brazo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S41.1": {
        "descripcion": 'Herida abierta del brazo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S50.0": {
        "descripcion": 'Contusión del codo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S51.8": {
        "descripcion": 'Herida abierta del antebrazo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S60.0": {
        "descripcion": 'Contusión de los dedos de la mano',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S61.0": {
        "descripcion": 'Herida abierta de un dedo de la mano',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S70.0": {
        "descripcion": 'Contusión de la cadera y muslo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S71.1": {
        "descripcion": 'Herida abierta del muslo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S80.0": {
        "descripcion": 'Contusión de la rodilla',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S81.0": {
        "descripcion": 'Herida abierta de la pierna',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S90.3": {
        "descripcion": 'Contusión del pie',
        "severidad_clinica": "baja",
        "tipo_lesion": "Contusión",
        "parte_cuerpo": "Pies",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S91.3": {
        "descripcion": 'Herida abierta de otras partes del pie',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Pies",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S62.6": {
        "descripcion": 'Fractura de otros dedos de la mano',
        "severidad_clinica": "baja",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S52.5": {
        "descripcion": 'Fractura de la epífisis inferior del radio',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S42.2": {
        "descripcion": 'Fractura de la parte superior del húmero',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S43.0": {
        "descripcion": 'Luxación de la articulación del hombro',
        "severidad_clinica": "baja",
        "tipo_lesion": "Luxación",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S53.0": {
        "descripcion": 'Luxación de la articulación del codo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Luxación",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S83.0": {
        "descripcion": 'Luxación de la rótula',
        "severidad_clinica": "baja",
        "tipo_lesion": "Luxación",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S92.3": {
        "descripcion": 'Fractura de los huesos del metatarso',
        "severidad_clinica": "baja",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Pies",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "T14.0": {
        "descripcion": 'Traumatismo superficial de región no especificada',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Trauma superficial",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "T14.1": {
        "descripcion": 'Herida de región no especificada',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "T14.8": {
        "descripcion": 'Otros traumatismos de región no especificada',
        "severidad_clinica": "baja",
        "tipo_lesion": "Otro",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S02.9": {
        "descripcion": 'Fractura del cráneo y de los huesos faciales, parte no especificada',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S05.9": {
        "descripcion": 'Traumatismo del ojo y de la órbita, no especificado',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Ojo",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S06.0": {
        "descripcion": 'Conmoción cerebral',
        "severidad_clinica": "alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S06.5": {
        "descripcion": 'Hemorragia subdural traumática',
        "severidad_clinica": "alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S06.6": {
        "descripcion": 'Hemorragia subaracnoidea traumática',
        "severidad_clinica": "alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S22.3": {
        "descripcion": 'Fractura de costilla',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Tórax",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S27.0": {
        "descripcion": 'Neumotórax traumático',
        "severidad_clinica": "alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Tórax",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S32.0": {
        "descripcion": 'Fractura de vértebra lumbar',
        "severidad_clinica": "alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Tronco",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S36.0": {
        "descripcion": 'Traumatismo del bazo',
        "severidad_clinica": "alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Abdomen",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S36.1": {
        "descripcion": 'Traumatismo del hígado',
        "severidad_clinica": "alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Abdomen",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S42.3": {
        "descripcion": 'Fractura de la diáfisis del húmero',
        "severidad_clinica": "alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S52.3": {
        "descripcion": 'Fractura de la diáfisis del radio',
        "severidad_clinica": "alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S62.3": {
        "descripcion": 'Fractura de otros huesos de la mano',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S68.1": {
        "descripcion": 'Amputación traumática de un dedo',
        "severidad_clinica": "alta",
        "tipo_lesion": "Amputación",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S72.3": {
        "descripcion": 'Fractura de la diáfisis del fémur',
        "severidad_clinica": "alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S82.2": {
        "descripcion": 'Fractura de la diáfisis de la tibia',
        "severidad_clinica": "alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T20.2": {
        "descripcion": 'Quemadura de segundo grado de cabeza y cuello',
        "severidad_clinica": "alta",
        "tipo_lesion": "Quemadura",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T21.2": {
        "descripcion": 'Quemadura de segundo grado del tronco',
        "severidad_clinica": "alta",
        "tipo_lesion": "Quemadura",
        "parte_cuerpo": "Tronco",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T22.2": {
        "descripcion": 'Quemadura de segundo grado del hombro y miembro superior',
        "severidad_clinica": "alta",
        "tipo_lesion": "Quemadura",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T23.2": {
        "descripcion": 'Quemadura de segundo grado de la muñeca y mano',
        "severidad_clinica": "alta",
        "tipo_lesion": "Quemadura",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S06.9": {
        "descripcion": 'Traumatismo intracraneal, no especificado',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "S27.1": {
        "descripcion": 'Hemotórax traumático',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Tórax",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "S32.8": {
        "descripcion": 'Fracturas de otras partes de la columna lumbar y pelvis',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Tronco",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "S36.8": {
        "descripcion": 'Traumatismo de otros órganos intraabdominales',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Abdomen",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "S72.0": {
        "descripcion": 'Fractura del cuello del fémur',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "S78.9": {
        "descripcion": 'Amputación traumática de la cadera y muslo, nivel no especificado',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Amputación",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "T17.9": {
        "descripcion": 'Cuerpo extraño en las vías respiratorias, parte no especificada',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Asfixia",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "T57.0": {
        "descripcion": 'Efecto tóxico del arsénico y sus compuestos',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "T75.0": {
        "descripcion": 'Efectos de la descarga eléctrica',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Efecto de la electricidad",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "T71.9": {
        "descripcion": 'Asfixia y estrangulamiento, no especificados',
        "severidad_clinica": "muy_alta",
        "tipo_lesion": "Asfixia",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.10, "peso_ventana": 0.20},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.30, "peso_ventana": 0.40},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.60, "peso_ventana": 0.40},
        ],
    },
    "T67.0": {
        "descripcion": 'Golpe de calor e insolación',
        "severidad_clinica": "alta",
        "tipo_lesion": "Efecto del calor",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T67.9": {
        "descripcion": 'Efectos del calor y de la luz, no especificados',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Efecto del calor",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "T33.0": {
        "descripcion": 'Congelación superficial de la cabeza',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Congelación",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "T34.4": {
        "descripcion": 'Congelación con necrosis tisular del brazo',
        "severidad_clinica": "alta",
        "tipo_lesion": "Congelación",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T35.1": {
        "descripcion": 'Congelación con necrosis tisular que afecta múltiples regiones corporales',
        "severidad_clinica": "alta",
        "tipo_lesion": "Congelación",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T78.2": {
        "descripcion": 'Shock anafiláctico, no especificado',
        "severidad_clinica": "alta",
        "tipo_lesion": "Reacción sistémica",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "S33.5": {
        "descripcion": 'Esguince y distensión de ligamentos de la columna lumbar',
        "severidad_clinica": "baja",
        "tipo_lesion": "Otro",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S43.4": {
        "descripcion": 'Esguince y distensión de la articulación del hombro',
        "severidad_clinica": "baja",
        "tipo_lesion": "Luxación",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S63.5": {
        "descripcion": 'Esguince y distensión de la muñeca',
        "severidad_clinica": "baja",
        "tipo_lesion": "Esguince",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S73.0": {
        "descripcion": 'Luxación de la articulación de la cadera',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Luxación",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S83.5": {
        "descripcion": 'Esguince y distensión de ligamentos de la rodilla',
        "severidad_clinica": "baja",
        "tipo_lesion": "Esguince",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S93.4": {
        "descripcion": 'Esguince y distensión del tobillo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Esguince",
        "parte_cuerpo": "Pies",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S02.2": {
        "descripcion": 'Fractura de los huesos nasales',
        "severidad_clinica": "baja",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Cabeza",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S11.9": {
        "descripcion": 'Herida abierta del cuello, parte no especificada',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Cuello",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S31.0": {
        "descripcion": 'Herida abierta de la región lumbar y pelvis',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Tronco",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S51.0": {
        "descripcion": 'Herida abierta del codo',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Miembros superiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S81.8": {
        "descripcion": 'Herida abierta de otras partes de la pierna',
        "severidad_clinica": "baja",
        "tipo_lesion": "Herida",
        "parte_cuerpo": "Miembros inferiores",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S22.4": {
        "descripcion": 'Fracturas múltiples de las costillas',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Tórax",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S32.1": {
        "descripcion": 'Fractura del sacro',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Fractura",
        "parte_cuerpo": "Tronco",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S37.0": {
        "descripcion": 'Traumatismo del riñón',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Trauma interno",
        "parte_cuerpo": "Abdomen",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "S67.0": {
        "descripcion": 'Lesión por aplastamiento del pulgar y otros dedos',
        "severidad_clinica": "moderada",
        "tipo_lesion": "Aplastamiento",
        "parte_cuerpo": "Manos",
        "escenarios": [
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.65, "peso_ventana": 0.55},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "T30.0": {
        "descripcion": 'Quemadura y corrosión de región del cuerpo no especificada, grado no especificado',
        "severidad_clinica": "baja",
        "tipo_lesion": "Quemadura",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
    "T35.0": {
        "descripcion": 'Congelación superficial que afecta múltiples regiones corporales',
        "severidad_clinica": "muy_baja",
        "tipo_lesion": "Congelación",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.65, "peso_ventana": 0.80},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.30, "peso_ventana": 0.18},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.05, "peso_ventana": 0.02},
        ],
    },
    "T51.9": {
        "descripcion": 'Efecto tóxico del alcohol, no especificado',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T54.9": {
        "descripcion": 'Efecto tóxico de sustancia corrosiva, no especificada',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T58.0": {
        "descripcion": 'Efecto tóxico del monóxido de carbono',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T59.9": {
        "descripcion": 'Efecto tóxico de gases, humos y vapores, no especificado',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T60.9": {
        "descripcion": 'Efecto tóxico de plaguicida, no especificado',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T63.0": {
        "descripcion": 'Efecto tóxico del veneno de serpiente',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T63.2": {
        "descripcion": 'Efecto tóxico del veneno de escorpión',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T63.3": {
        "descripcion": 'Efecto tóxico del veneno de araña',
        "severidad_clinica": "alta",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.20, "peso_ventana": 0.35},
            {"nivel": "alta", "dias_min": 60, "dias_max": 120, "peso_normal": 0.60, "peso_ventana": 0.55},
            {"nivel": "muy_alta", "dias_min": 120, "dias_max": 180, "peso_normal": 0.20, "peso_ventana": 0.10},
        ],
    },
    "T63.4": {
        "descripcion": 'Efecto tóxico del veneno de otros artrópodos',
        "severidad_clinica": "baja",
        "tipo_lesion": "Envenenamiento",
        "parte_cuerpo": "Lesiones generales",
        "escenarios": [
            {"nivel": "muy_baja", "dias_min": 1, "dias_max": 5, "peso_normal": 0.15, "peso_ventana": 0.30},
            {"nivel": "baja", "dias_min": 5, "dias_max": 20, "peso_normal": 0.70, "peso_ventana": 0.60},
            {"nivel": "moderada", "dias_min": 20, "dias_max": 60, "peso_normal": 0.15, "peso_ventana": 0.10},
        ],
    },
}

AREAS_ACCIDENTE = [
    "Área administrativa",
    "Oficina",
    "Bodega",
    "Taller",
    "Planta",
    "Zona de producción",
    "Obra / Frente de trabajo",
    "Área de mantenimiento",
    "Zona de almacenamiento",
    "Patio / Zona externa",
    "Vía pública",
    "Vehículo",
    "Pasillos",
    "Escaleras",
    "Baños",
    "Cafetería",
    "Zona de cargue y descargue",
    "Otro lugar",
]

CRITERIOS_GRAVEDAD_RES1401 = {
    # ---------------------------------------------------------
    # Criterios que permiten determinar directamente
    # accidente grave según la Resolución 1401 de 2007.
    # ---------------------------------------------------------

    # Trauma craneoencefálico
    "S06.0": {
        "tipo": "DIRECTO",
        "criterio": "Trauma craneoencefálico",
    },
    "S06.5": {
        "tipo": "DIRECTO",
        "criterio": "Trauma craneoencefálico",
    },
    "S06.6": {
        "tipo": "DIRECTO",
        "criterio": "Trauma craneoencefálico",
    },
    "S06.9": {
        "tipo": "DIRECTO",
        "criterio": "Trauma craneoencefálico",
    },

    # Fractura de huesos largos
    "S42.2": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de húmero",
    },
    "S42.3": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de húmero",
    },
    "S52.3": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de radio",
    },
    "S52.5": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de radio",
    },
    "S72.0": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de fémur",
    },
    "S72.3": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de fémur",
    },
    "S82.2": {
        "tipo": "DIRECTO",
        "criterio": "Fractura de tibia",
    },

    # Amputación
    "S68.1": {
        "tipo": "DIRECTO",
        "criterio": "Amputación de segmento corporal",
    },
    "S78.9": {
        "tipo": "DIRECTO",
        "criterio": "Amputación de segmento corporal",
    },

    # Quemaduras de segundo grado
    "T20.2": {
        "tipo": "DIRECTO",
        "criterio": "Quemadura de segundo grado",
    },
    "T21.2": {
        "tipo": "DIRECTO",
        "criterio": "Quemadura de segundo grado",
    },
    "T22.2": {
        "tipo": "DIRECTO",
        "criterio": "Quemadura de segundo grado",
    },
    "T23.2": {
        "tipo": "DIRECTO",
        "criterio": "Quemadura de segundo grado",
    },

    # ---------------------------------------------------------
    # Diagnósticos que requieren una condición adicional.
    # La condición se simula posteriormente con la
    # probabilidad configurada en parametros.py.
    # ---------------------------------------------------------

    "S02.9": {
        "tipo": "CONDICIONAL",
        "criterio": "Trauma craneoencefálico",
        "atributo": "trauma_craneoencefalico",
    },
    "S05.9": {
        "tipo": "CONDICIONAL",
        "criterio": "Compromiso de agudeza o campo visual",
        "atributo": "compromiso_visual",
    },
    "S32.0": {
        "tipo": "CONDICIONAL",
        "criterio": "Compromiso de médula espinal",
        "atributo": "compromiso_medular",
    },
    "S32.8": {
        "tipo": "CONDICIONAL",
        "criterio": "Compromiso de médula espinal",
        "atributo": "compromiso_medular",
    },
    "S62.3": {
        "tipo": "CONDICIONAL",
        "criterio": "Lesión severa de mano",
        "atributo": "lesion_severa_mano",
    },
}

COMPATIBILIDAD_TIPO_MECANISMO_DIAGNOSTICO = {

    # =========================================================
    # CAÍDA DE PERSONA
    # =========================================================

    'Caída de persona': {

        'Caída a nivel': [
            ('S13.4', 0.18, 0.23),
            ('S16.1', 0.18, 0.21),
            ('S20.2', 0.16, 0.18),
            ('S30.0', 0.12, 0.11),
            ('S40.0', 0.12, 0.1),
            ('S80.0', 0.1, 0.07),
            ('S93.4', 0.07, 0.04),
            ('S52.5', 0.03, 0.02),
            ('S43.0', 0.01, 0.01),
            ('S63.5', 0.01, 0.01),
            ('S73.0', 0.01, 0.01),
            ('S83.5', 0.01, 0.01)
        ],

        'Caída a diferente nivel': [
            ('S40.0', 0.09, 0.23),
            ('S70.0', 0.14, 0.17),
            ('S72.3', 0.14, 0.09),
            ('S82.2', 0.14, 0.1),
            ('S42.3', 0.14, 0.1),
            ('S06.0', 0.11, 0.08),
            ('S32.0', 0.11, 0.1),
            ('S72.0', 0.05, 0.05),
            ('S02.9', 0.01, 0.01),
            ('S06.5', 0.01, 0.01),
            ('S06.6', 0.01, 0.01),
            ('S32.1', 0.01, 0.01),
            ('S32.8', 0.01, 0.01),
            ('S42.2', 0.01, 0.01),
            ('S52.3', 0.01, 0.01),
            ('S73.0', 0.01, 0.01)
            ],

        'Resbalón o tropiezo': [
            ('S13.4', 0.22, 0.27),
            ('S16.1', 0.18, 0.21),
            ('S20.2', 0.15, 0.18),
            ('S30.0', 0.12, 0.11),
            ('S40.0', 0.12, 0.1),
            ('S80.0', 0.1, 0.07),
            ('S93.4', 0.08, 0.04),
            ('S52.5', 0.03, 0.02)
        ]
    },

    # =========================================================
    # CAÍDA DE OBJETO
    # =========================================================

    'Caída de objeto': {

        'Caída de objeto desde altura': [
            ('S00.0', 0.13, 0.15),
            ('S20.2', 0.13, 0.16),
            ('S40.0', 0.13, 0.14),
            ('S50.0', 0.13, 0.12),
            ('S60.0', 0.1, 0.11),
            ('S22.3', 0.14, 0.12),
            ('S42.3', 0.15, 0.11),
            ('S06.0', 0.08, 0.08),
            ('S22.4', 0.01, 0.01)
        ],

        'Desprendimiento de objeto': [
            ('S00.8', 0.14, 0.17),
            ('S20.2', 0.14, 0.16),
            ('S40.0', 0.12, 0.14),
            ('S50.0', 0.12, 0.12),
            ('S60.0', 0.1, 0.11),
            ('S22.3', 0.14, 0.11),
            ('S42.3', 0.14, 0.1),
            ('S06.0', 0.1, 0.09)
        ],

        'Golpe por objeto en movimiento': [
            ('S00.8', 0.12, 0.15),
            ('S01.8', 0.13, 0.15),
            ('S20.2', 0.15, 0.16),
            ('S40.0', 0.13, 0.13),
            ('S50.0', 0.13, 0.12),
            ('S42.3', 0.15, 0.1),
            ('S72.3', 0.1, 0.08),
            ('S06.0', 0.06, 0.08),
            ('S02.2', 0.01, 0.01),
            ('S05.9', 0.01, 0.01),
            ('S42.2', 0.01, 0.01)
        ]
    },

    # =========================================================
    # PISADA O GOLPE
    # =========================================================

    'Pisada o golpe': {

        'Golpe contra objeto': [
            ('S00.8', 0.18, 0.22),
            ('S01.8', 0.16, 0.19),
            ('S20.2', 0.16, 0.18),
            ('S40.0', 0.16, 0.15),
            ('S50.0', 0.13, 0.11),
            ('S60.0', 0.11, 0.08),
            ('S80.0', 0.07, 0.05),
            ('S42.3', 0.03, 0.02)
        ],

        'Golpeado por objeto': [
            ('S00.8', 0.15, 0.18),
            ('S01.8', 0.13, 0.16),
            ('S20.2', 0.15, 0.17),
            ('S40.0', 0.13, 0.14),
            ('S50.0', 0.13, 0.11),
            ('S42.3', 0.17, 0.11),
            ('S72.3', 0.1, 0.07),
            ('S06.0', 0.03, 0.05),
            ('S05.9', 0.01, 0.01)
        ],

        'Pisada sobre superficie u objeto': [
            ('S60.0', 0.17, 0.21),
            ('S61.0', 0.16, 0.19),
            ('S80.0', 0.15, 0.17),
            ('S90.3', 0.14, 0.14),
            ('S93.4', 0.14, 0.12),
            ('S70.0', 0.1, 0.07),
            ('S92.3', 0.1, 0.06),
            ('S52.5', 0.03, 0.03),
            ('S62.6', 0.01, 0.01)
        ]
    },

    # =========================================================
    # ATRAPAMIENTO
    # =========================================================

    'Atrapamiento': {

        'Atrapamiento entre objetos': [
            ('S40.0', 0.09, 0.13),
            ('S50.0', 0.09, 0.12),
            ('S60.0', 0.09, 0.15),
            ('S70.0', 0.09, 0.14),
            ('S80.0', 0.09, 0.13),
            ('S42.3', 0.18, 0.1),
            ('S68.1', 0.2, 0.1),
            ('S72.3', 0.17, 0.13)
        ],

        'Atrapamiento en máquina o equipo': [
            ('S41.1', 0.07, 0.18),
            ('S51.8', 0.07, 0.1),
            ('S61.0', 0.07, 0.12),
            ('S67.0', 0.13, 0.14),
            ('S42.3', 0.16, 0.12),
            ('S68.1', 0.2, 0.15),
            ('S72.3', 0.17, 0.1),
            ('S78.9', 0.11, 0.07),
            ('S62.3', 0.01, 0.01),
            ('S62.6', 0.01, 0.01)
        ],

        'Aplastamiento': [
            ('S50.0', 0.07, 0.2),
            ('S60.0', 0.07, 0.12),
            ('S67.0', 0.11, 0.13),
            ('S68.1', 0.2, 0.12),
            ('S42.3', 0.16, 0.12),
            ('S72.3', 0.16, 0.14),
            ('S82.2', 0.13, 0.1),
            ('S78.9', 0.1, 0.07)
        ]
    },

    # =========================================================
    # SOBRESFUERZO
    # =========================================================

    'Sobreesfuerzo': {

        'Levantamiento de carga': [
            ('S13.4', 0.15, 0.19),
            ('S16.1', 0.16, 0.2),
            ('S33.5', 0.16, 0.17),
            ('S43.4', 0.12, 0.12),
            ('S53.0', 0.1, 0.09),
            ('S83.0', 0.1, 0.08),
            ('S93.4', 0.1, 0.07),
            ('S32.0', 0.1, 0.07),
            ('S43.0', 0.01, 0.01)
        ],

        'Empuje o tracción': [
            ('S13.4', 0.16, 0.2),
            ('S16.1', 0.18, 0.22),
            ('S33.5', 0.16, 0.17),
            ('S43.4', 0.12, 0.12),
            ('S53.0', 0.1, 0.09),
            ('S83.0', 0.1, 0.08),
            ('S93.4', 0.1, 0.07),
            ('S32.0', 0.08, 0.05)
        ],

        'Movimiento repetitivo': [
            ('S16.1', 0.16, 0.2),
            ('S33.5', 0.18, 0.2),
            ('S43.4', 0.14, 0.14),
            ('S53.0', 0.12, 0.1),
            ('S83.0', 0.12, 0.1),
            ('S93.4', 0.12, 0.09),
            ('S13.4', 0.08, 0.08),
            ('S40.0', 0.06, 0.07),
            ('S63.5', 0.01, 0.01),
            ('S83.5', 0.01, 0.01)
        ],

        'Postura forzada': [
            ('S16.1', 0.2, 0.24),
            ('S13.4', 0.16, 0.19),
            ('S33.5', 0.16, 0.18),
            ('S43.4', 0.12, 0.12),
            ('S53.0', 0.1, 0.09),
            ('S83.0', 0.1, 0.07),
            ('S93.4', 0.1, 0.06),
            ('S40.0', 0.06, 0.05)
        ]
    },

    # =========================================================
    # TEMPERATURA EXTREMA
    # =========================================================

    'Temperatura extrema': {

        'Contacto con superficie caliente': [
            ('T20.2', 0.16, 0.2),
            ('T21.2', 0.14, 0.16),
            ('T22.2', 0.18, 0.18),
            ('T23.2', 0.18, 0.17),
            ('T30.0', 0.14, 0.12),
            ('S40.0', 0.08, 0.07),
            ('S50.0', 0.06, 0.05),
            ('T67.0', 0.06, 0.05)
        ],

        'Contacto con superficie fría': [
            ('T33.0', 0.24, 0.28),
            ('T35.0', 0.16, 0.18),
            ('T14.0', 0.14, 0.15),
            ('T14.8', 0.12, 0.12),
            ('S60.0', 0.1, 0.09),
            ('S90.3', 0.1, 0.07),
            ('T34.4', 0.1, 0.07),
            ('T35.1', 0.04, 0.04)
        ],

        'Exposición a calor': [
            ('T67.9', 0.3, 0.33),
            ('T67.0', 0.12, 0.14),
            ('T14.8', 0.14, 0.15),
            ('T14.0', 0.12, 0.13),
            ('S16.1', 0.1, 0.09),
            ('S40.0', 0.08, 0.06),
            ('S80.0', 0.08, 0.06),
            ('T22.2', 0.06, 0.04)
        ],

        'Exposición a frío': [
            ('T33.0', 0.22, 0.26),
            ('T35.0', 0.18, 0.2),
            ('T14.8', 0.14, 0.15),
            ('T14.0', 0.12, 0.12),
            ('S90.3', 0.1, 0.09),
            ('S80.0', 0.08, 0.07),
            ('T34.4', 0.12, 0.07),
            ('T35.1', 0.04, 0.04)
        ]
    },

    # =========================================================
    # CONTACTO CON ELECTRICIDAD
    # =========================================================

    'Contacto con electricidad': {

        'Contacto directo': [
            ('T75.0', 0.11, 0.14),
            ('T20.2', 0.16, 0.18),
            ('T22.2', 0.18, 0.17),
            ('T23.2', 0.16, 0.16),
            ('T30.0', 0.18, 0.14),
            ('S40.0', 0.13, 0.1),
            ('T71.9', 0.05, 0.06),
            ('S06.9', 0.03, 0.05)
        ],

        'Contacto indirecto': [
            ('T75.0', 0.11, 0.14),
            ('T20.2', 0.16, 0.18),
            ('T22.2', 0.18, 0.17),
            ('T23.2', 0.16, 0.16),
            ('T30.0', 0.18, 0.14),
            ('S40.0', 0.13, 0.1),
            ('T71.9', 0.05, 0.06),
            ('S06.9', 0.03, 0.05)
        ],

        'Arco eléctrico': [
            ('T20.2', 0.18, 0.21),
            ('T21.2', 0.13, 0.15),
            ('T22.2', 0.18, 0.17),
            ('T23.2', 0.18, 0.15),
            ('T30.0', 0.11, 0.1),
            ('T75.0', 0.11, 0.09),
            ('S06.0', 0.09, 0.08),
            ('T71.9', 0.02, 0.05)
        ]
    },

    # =========================================================
    # SUSTANCIAS NOCIVAS
    # =========================================================

    'Sustancias nocivas': {

        'Contacto con sustancia química': [
            ('T14.0', 0.13, 0.16),
            ('T14.8', 0.13, 0.16),
            ('T20.2', 0.13, 0.14),
            ('T22.2', 0.13, 0.13),
            ('T23.2', 0.13, 0.12),
            ('T54.9', 0.18, 0.14),
            ('T78.2', 0.09, 0.08),
            ('T57.0', 0.08, 0.07)
        ],

        'Inhalación': [
            ('T14.8', 0.17, 0.2),
            ('T57.0', 0.1, 0.11),
            ('T58.0', 0.2, 0.2),
            ('T59.9', 0.2, 0.18),
            ('T60.9', 0.12, 0.12),
            ('T78.2', 0.12, 0.1),
            ('T71.9', 0.07, 0.05),
            ('S06.9', 0.02, 0.04)
        ],

        'Ingestión': [
            ('T14.8', 0.16, 0.19),
            ('T51.9', 0.11, 0.12),
            ('T54.9', 0.13, 0.14),
            ('T57.0', 0.09, 0.1),
            ('T58.0', 0.13, 0.14),
            ('T60.9', 0.13, 0.12),
            ('T78.2', 0.11, 0.1),
            ('T71.9', 0.14, 0.09)
        ],

        'Salpicadura': [
            ('T14.0', 0.16, 0.18),
            ('T14.8', 0.13, 0.15),
            ('T20.2', 0.16, 0.16),
            ('T22.2', 0.16, 0.15),
            ('T23.2', 0.16, 0.13),
            ('T54.9', 0.13, 0.1),
            ('T78.2', 0.08, 0.08),
            ('T57.0', 0.02, 0.05)
        ]
    },

    # =========================================================
    # ELEMENTO CORTOPUNZANTE
    # =========================================================

    'Elemento cortopunzante': {

        'Corte': [
            ('S01.0', 0.14, 0.13),
            ('S41.1', 0.14, 0.16),
            ('S51.8', 0.14, 0.15),
            ('S61.0', 0.11, 0.16),
            ('S71.1', 0.12, 0.11),
            ('S81.0', 0.1, 0.09),
            ('S68.1', 0.14, 0.09),
            ('S42.3', 0.06, 0.06),
            ('S11.9', 0.01, 0.01),
            ('S31.0', 0.01, 0.01),
            ('S51.0', 0.01, 0.01),
            ('S81.8', 0.01, 0.01),
            ('S91.3', 0.01, 0.01)
        ],

        'Punción': [
            ('S01.0', 0.12, 0.16),
            ('S41.1', 0.14, 0.15),
            ('S51.8', 0.14, 0.15),
            ('S61.0', 0.18, 0.18),
            ('S71.1', 0.12, 0.11),
            ('S81.0', 0.1, 0.09),
            ('S68.1', 0.08, 0.07),
            ('T78.2', 0.12, 0.09)
        ],

        'Perforación': [
            ('S01.0', 0.1, 0.14),
            ('S41.1', 0.12, 0.14),
            ('S51.8', 0.14, 0.15),
            ('S61.0', 0.1, 0.11),
            ('S71.1', 0.12, 0.11),
            ('S81.0', 0.1, 0.09),
            ('S68.1', 0.14, 0.1),
            ('S42.3', 0.12, 0.1),
            ('S31.0', 0.01, 0.01),
            ('S51.0', 0.01, 0.01),
            ('S52.3', 0.01, 0.01),
            ('S62.3', 0.01, 0.01),
            ('S81.8', 0.01, 0.01),
            ('S91.3', 0.01, 0.01)
        ]
    },

    # =========================================================
    # OTRO
    # =========================================================

    'Otro': {

        'Mecanismo no especificado': [
            ('T14.0', 0.19, 0.23),
            ('T14.1', 0.18, 0.2),
            ('T14.8', 0.18, 0.19),
            ('S20.2', 0.12, 0.11),
            ('S40.0', 0.1, 0.09),
            ('S50.0', 0.08, 0.07),
            ('S42.3', 0.1, 0.06),
            ('S06.0', 0.04, 0.04),
            ('T17.9', 0.01, 0.01)
        ],

        'Otro mecanismo': [
            ('T14.0', 0.19, 0.23),
            ('T14.1', 0.18, 0.2),
            ('T14.8', 0.18, 0.19),
            ('S20.2', 0.12, 0.11),
            ('S40.0', 0.1, 0.09),
            ('S50.0', 0.08, 0.07),
            ('S42.3', 0.1, 0.06),
            ('S06.0', 0.04, 0.04),
            ('T17.9', 0.01, 0.01)
        ]
    },

    # =========================================================
    # ACCIDENTE DE TRÁNSITO
    # =========================================================

    'Accidente de tránsito': {

        'Colisión': [
            ('S00.8', 0.11, 0.1),
            ('S20.2', 0.11, 0.14),
            ('S40.0', 0.11, 0.13),
            ('S42.3', 0.12, 0.13),
            ('S22.3', 0.14, 0.13),
            ('S06.0', 0.16, 0.11),
            ('S72.3', 0.16, 0.12),
            ('S06.9', 0.05, 0.1),
            ('S02.9', 0.01, 0.01),
            ('S22.4', 0.01, 0.01),
            ('S36.0', 0.01, 0.01),
            ('S36.1', 0.01, 0.01)
        ],

        'Atropellamiento': [
            ('S00.8', 0.1, 0.14),
            ('S20.2', 0.1, 0.13),
            ('S40.0', 0.08, 0.11),
            ('S42.3', 0.15, 0.13),
            ('S22.3', 0.13, 0.12),
            ('S06.0', 0.15, 0.11),
            ('S72.3', 0.18, 0.13),
            ('S06.9', 0.11, 0.13)
        ],

        'Volcamiento': [
            ('S20.2', 0.08, 0.11),
            ('S22.3', 0.1, 0.12),
            ('S27.0', 0.13, 0.13),
            ('S32.0', 0.13, 0.12),
            ('S42.3', 0.13, 0.12),
            ('S72.3', 0.15, 0.13),
            ('S06.0', 0.09, 0.06),
            ('S06.9', 0.11, 0.13),
            ('S06.5', 0.01, 0.01),
            ('S06.6', 0.01, 0.01),
            ('S27.1', 0.01, 0.01),
            ('S32.8', 0.01, 0.01),
            ('S36.0', 0.01, 0.01),
            ('S36.1', 0.01, 0.01),
            ('S36.8', 0.01, 0.01),
            ('S37.0', 0.01, 0.01)
        ],

        'Caída de vehículo': [
            ('S00.8', 0.1, 0.13),
            ('S20.2', 0.1, 0.12),
            ('S22.3', 0.13, 0.12),
            ('S27.0', 0.13, 0.12),
            ('S32.0', 0.13, 0.12),
            ('S42.3', 0.13, 0.12),
            ('S72.3', 0.11, 0.13),
            ('S06.9', 0.13, 0.1),
            ('S27.1', 0.01, 0.01),
            ('S32.1', 0.01, 0.01),
            ('S36.8', 0.01, 0.01),
            ('S37.0', 0.01, 0.01)
        ]
    },

    # =========================================================
    # VIOLENCIA
    # =========================================================

    'Violencia': {

        'Agresión física': [
            ('S00.8', 0.2, 0.23),
            ('S01.8', 0.16, 0.18),
            ('S20.2', 0.16, 0.17),
            ('S40.0', 0.13, 0.13),
            ('S50.0', 0.11, 0.1),
            ('S42.3', 0.09, 0.07),
            ('S06.0', 0.09, 0.07),
            ('S06.9', 0.06, 0.05)
        ],

        'Agresión con objeto': [
            ('S01.8', 0.14, 0.27),
            ('S20.2', 0.14, 0.16),
            ('S40.0', 0.11, 0.13),
            ('S50.0', 0.11, 0.11),
            ('S41.1', 0.11, 0.11),
            ('S42.3', 0.13, 0.1),
            ('S06.0', 0.13, 0.06),
            ('S06.9', 0.11, 0.04),
            ('S02.2', 0.01, 0.01),
            ('S11.9', 0.01, 0.01)
        ]
    },

    # =========================================================
    # MORDEDURA O PICADURA
    # =========================================================

    'Mordedura o picadura': {

        'Mordedura': [
            ('S01.8', 0.14, 0.17),
            ('S41.1', 0.13, 0.16),
            ('S51.8', 0.13, 0.16),
            ('S61.0', 0.16, 0.16),
            ('S71.1', 0.13, 0.12),
            ('S81.0', 0.13, 0.1),
            ('T63.4', 0.11, 0.08),
            ('T78.2', 0.07, 0.05)
        ],

        'Picadura': [
            ('T14.0', 0.16, 0.2),
            ('T14.8', 0.13, 0.16),
            ('T63.4', 0.2, 0.17),
            ('T63.0', 0.11, 0.1),
            ('T63.2', 0.11, 0.1),
            ('T63.3', 0.11, 0.1),
            ('T78.2', 0.13, 0.1),
            ('T57.0', 0.05, 0.07)
        ]
    },

    # =========================================================
    # EXPOSICIÓN / CONTACTO CON AGENTE BIOLÓGICO
    # =========================================================

    'Exposición o contacto con agente biológico': {

        'Contacto con material biológico': [
            ('S01.0', 0.16, 0.2),
            ('S41.1', 0.14, 0.16),
            ('S51.8', 0.14, 0.15),
            ('S61.0', 0.18, 0.17),
            ('S71.1', 0.1, 0.1),
            ('S81.0', 0.08, 0.07),
            ('T78.2', 0.12, 0.08),
            ('T14.8', 0.08, 0.07)
        ],

        'Exposición a agente biológico': [
            ('T14.8', 0.2, 0.23),
            ('T78.2', 0.13, 0.14),
            ('S01.0', 0.13, 0.13),
            ('S41.1', 0.13, 0.13),
            ('S51.8', 0.13, 0.12),
            ('S61.0', 0.13, 0.11),
            ('S71.1', 0.07, 0.07),
            ('S81.0', 0.08, 0.07)
        ],

        'Pinchazo con material contaminado': [
            ('S61.0', 0.26, 0.28),
            ('S51.8', 0.14, 0.15),
            ('S41.1', 0.12, 0.13),
            ('S81.0', 0.08, 0.08),
            ('S71.1', 0.08, 0.08),
            ('T14.1', 0.1, 0.09),
            ('T78.2', 0.12, 0.1),
            ('T14.8', 0.1, 0.09)
        ]
    }
}

COMPATIBILIDAD_CARGO_AREA_ACCIDENTE = {

    # =====================================================
    # DIRECCIÓN / GERENCIA
    # =====================================================

    "Gerente General": [
        "Área administrativa",
        "Oficina",
        "Pasillos",
        "Escaleras",
        "Baños",
        "Cafetería",
        "Zona de cargue y descargue",
        "Vehículo",
    ],

    "Director Operativo": [
        "Área administrativa",
        "Oficina",
        "Taller",
        "Planta",
        "Zona de producción",
        "Obra / Frente de trabajo",
        "Área de mantenimiento",
        "Patio / Zona externa",
        "Pasillos",
        "Escaleras",
        "Zona de cargue y descargue",
        "Vehículo",
    ],

    "Director Comercial": [
        "Área administrativa",
        "Oficina",
        "Obra / Frente de trabajo",
        "Patio / Zona externa",
        "Vía pública",
        "Vehículo",
        "Pasillos",
        "Escaleras",
        "Zona de cargue y descargue",
    ],


    # =====================================================
    # COORDINADORES
    # =====================================================

    "Coordinador Administrativo": [
        "Área administrativa",
        "Oficina",
        "Bodega",
        "Zona de almacenamiento",
        "Pasillos",
        "Escaleras",
        "Baños",
        "Cafetería",
        "Zona de cargue y descargue",
    ],

    "Coordinador SST": [
        "Área administrativa",
        "Oficina",
        "Taller",
        "Planta",
        "Zona de producción",
        "Obra / Frente de trabajo",
        "Área de mantenimiento",
        "Bodega",
        "Patio / Zona externa",
        "Pasillos",
        "Escaleras",
        "Zona de cargue y descargue",
        "Vehículo",
    ],

    "Coordinador Logístico": [
        "Área administrativa",
        "Oficina",
        "Bodega",
        "Zona de almacenamiento",
        "Zona de cargue y descargue",
        "Patio / Zona externa",
        "Vía pública",
        "Vehículo",
        "Pasillos",
        "Escaleras",
    ],

    "Coordinador de Proyectos": [
        "Área administrativa",
        "Oficina",
        "Obra / Frente de trabajo",
        "Taller",
        "Área de mantenimiento",
        "Patio / Zona externa",
        "Zona de cargue y descargue",
        "Vehículo",
        "Pasillos",
        "Escaleras",
    ],


    # =====================================================
    # PROFESIONALES
    # =====================================================

    "Profesional de Recursos Humanos": [
        "Área administrativa",
        "Oficina",
        "Pasillos",
        "Escaleras",
        "Baños",
        "Cafetería",
    ],

    "Profesional de Compras": [
        "Área administrativa",
        "Oficina",
        "Bodega",
        "Zona de almacenamiento",
        "Zona de cargue y descargue",
        "Pasillos",
        "Escaleras",
    ],

    "Profesional de Calidad": [
        "Área administrativa",
        "Oficina",
        "Taller",
        "Planta",
        "Zona de producción",
        "Obra / Frente de trabajo",
        "Área de mantenimiento",
        "Bodega",
        "Pasillos",
        "Escaleras",
    ],

    "Ingeniero de Proyectos": [
        "Área administrativa",
        "Oficina",
        "Obra / Frente de trabajo",
        "Taller",
        "Planta",
        "Área de mantenimiento",
        "Patio / Zona externa",
        "Zona de cargue y descargue",
        "Vehículo",
        "Pasillos",
        "Escaleras",
    ],


    # =====================================================
    # COMERCIAL
    # =====================================================

    "Vendedor": [
        "Área administrativa",
        "Oficina",
        "Obra / Frente de trabajo",
        "Patio / Zona externa",
        "Vía pública",
        "Vehículo",
        "Pasillos",
        "Escaleras",
        "Zona de cargue y descargue",
    ],


    # =====================================================
    # TÉCNICOS
    # =====================================================

    "Técnico de Mantenimiento": [
        "Taller",
        "Planta",
        "Zona de producción",
        "Obra / Frente de trabajo",
        "Área de mantenimiento",
        "Bodega",
        "Zona de almacenamiento",
        "Patio / Zona externa",
        "Zona de cargue y descargue",
        "Vehículo",
        "Escaleras",
    ],

    "Técnico de Seguridad Industrial": [
        "Área administrativa",
        "Oficina",
        "Taller",
        "Planta",
        "Zona de producción",
        "Obra / Frente de trabajo",
        "Área de mantenimiento",
        "Bodega",
        "Patio / Zona externa",
        "Zona de cargue y descargue",
        "Vehículo",
        "Escaleras",
    ],


    # =====================================================
    # OPERATIVOS
    # =====================================================

    "Conductor": [
        "Vehículo",
        "Vía pública",
        "Patio / Zona externa",
        "Zona de cargue y descargue",
        "Bodega",
    ],

    "Operador de Máquina": [
        "Planta",
        "Zona de producción",
        "Taller",
        "Área de mantenimiento",
        "Bodega",
        "Zona de almacenamiento",
        "Zona de cargue y descargue",
    ],

    "Ayudante de Obra": [
        "Obra / Frente de trabajo",
        "Patio / Zona externa",
        "Bodega",
        "Zona de almacenamiento",
        "Zona de cargue y descargue",
        "Área de mantenimiento",
        "Vehículo",
        "Escaleras",
    ],


    # =====================================================
    # AUXILIARES
    # =====================================================

    "Auxiliar Contable": [
        "Área administrativa",
        "Oficina",
        "Pasillos",
        "Escaleras",
        "Baños",
        "Cafetería",
        "Zona de cargue y descargue",
    ],

    "Auxiliar Administrativo": [
        "Área administrativa",
        "Oficina",
        "Bodega",
        "Pasillos",
        "Escaleras",
        "Baños",
        "Cafetería",
        "Zona de cargue y descargue",
    ],

    "Auxiliar de Bodega": [
        "Bodega",
        "Zona de almacenamiento",
        "Zona de cargue y descargue",
        "Patio / Zona externa",
        "Pasillos",
        "Escaleras",
    ],
}

COMPATIBILIDAD_CARGO_TIPO_ACCIDENTE = {

    # --------------------------------------------------------
    # DIRECTIVOS
    # --------------------------------------------------------

    "Gerente General": [
        ("Caída de persona", 0.35),
        ("Pisada o golpe", 0.25),
        ("Sobreesfuerzo", 0.10),
        ("Caída de objeto", 0.10),
        ("Accidente de tránsito", 0.10),
        ("Violencia", 0.05),
        ("Otro", 0.05),
    ],

    "Director Operativo": [
        ("Caída de persona", 0.20),
        ("Caída de objeto", 0.15),
        ("Pisada o golpe", 0.15),
        ("Atrapamiento", 0.10),
        ("Sobreesfuerzo", 0.10),
        ("Temperatura extrema", 0.05),
        ("Contacto con electricidad", 0.05),
        ("Accidente de tránsito", 0.10),
        ("Sustancias nocivas", 0.05),
        ("Violencia", 0.05),
    ],

    "Director Comercial": [
        ("Caída de persona", 0.30),
        ("Pisada o golpe", 0.25),
        ("Accidente de tránsito", 0.18),
        ("Sobreesfuerzo", 0.08),
        ("Violencia", 0.08),
        ("Caída de objeto", 0.06),
        ("Otro", 0.05),
    ],

    # --------------------------------------------------------
    # COORDINADORES
    # --------------------------------------------------------

    "Coordinador Administrativo": [
        ("Caída de persona", 0.35),
        ("Pisada o golpe", 0.30),
        ("Sobreesfuerzo", 0.15),
        ("Caída de objeto", 0.05),
        ("Accidente de tránsito", 0.05),
        ("Violencia", 0.05),
        ("Otro", 0.05),
    ],

    "Coordinador SST": [
        ("Caída de persona", 0.25),
        ("Pisada o golpe", 0.20),
        ("Sobreesfuerzo", 0.10),
        ("Caída de objeto", 0.10),
        ("Contacto con electricidad", 0.10),
        ("Accidente de tránsito", 0.05),
        ("Sustancias nocivas", 0.05),
        ("Exposición o contacto con agente biológico", 0.05),
        ("Temperatura extrema", 0.05),
        ("Violencia", 0.05),
    ],

    "Coordinador Logístico": [
        ("Caída de persona", 0.15),
        ("Caída de objeto", 0.15),
        ("Pisada o golpe", 0.15),
        ("Atrapamiento", 0.15),
        ("Sobreesfuerzo", 0.12),
        ("Elemento cortopunzante", 0.08),
        ("Accidente de tránsito", 0.10),
        ("Temperatura extrema", 0.05),
        ("Contacto con electricidad", 0.05),
    ],

    "Coordinador de Proyectos": [
        ("Caída de persona", 0.18),
        ("Caída de objeto", 0.15),
        ("Pisada o golpe", 0.15),
        ("Atrapamiento", 0.12),
        ("Sobreesfuerzo", 0.12),
        ("Contacto con electricidad", 0.08),
        ("Elemento cortopunzante", 0.06),
        ("Accidente de tránsito", 0.08),
        ("Temperatura extrema", 0.06),
    ],

    # --------------------------------------------------------
    # PROFESIONALES
    # --------------------------------------------------------

    "Profesional de Recursos Humanos": [
        ("Caída de persona", 0.35),
        ("Pisada o golpe", 0.30),
        ("Sobreesfuerzo", 0.12),
        ("Caída de objeto", 0.06),
        ("Accidente de tránsito", 0.06),
        ("Violencia", 0.05),
        ("Otro", 0.06),
    ],

    "Profesional de Compras": [
        ("Caída de persona", 0.30),
        ("Pisada o golpe", 0.25),
        ("Sobreesfuerzo", 0.10),
        ("Caída de objeto", 0.08),
        ("Accidente de tránsito", 0.12),
        ("Elemento cortopunzante", 0.04),
        ("Violencia", 0.05),
        ("Otro", 0.06),
    ],

    "Profesional de Calidad": [
        ("Caída de persona", 0.25),
        ("Pisada o golpe", 0.25),
        ("Sobreesfuerzo", 0.10),
        ("Caída de objeto", 0.08),
        ("Accidente de tránsito", 0.08),
        ("Elemento cortopunzante", 0.05),
        ("Contacto con electricidad", 0.05),
        ("Sustancias nocivas", 0.04),
        ("Violencia", 0.05),
        ("Otro", 0.05),
    ],

    "Ingeniero de Proyectos": [
        ("Caída de persona", 0.18),
        ("Caída de objeto", 0.15),
        ("Pisada o golpe", 0.15),
        ("Atrapamiento", 0.10),
        ("Sobreesfuerzo", 0.10),
        ("Contacto con electricidad", 0.08),
        ("Elemento cortopunzante", 0.07),
        ("Accidente de tránsito", 0.08),
        ("Temperatura extrema", 0.04),
        ("Sustancias nocivas", 0.05),
    ],

    # --------------------------------------------------------
    # COMERCIAL
    # --------------------------------------------------------

    "Vendedor": [
        ("Caída de persona", 0.30),
        ("Pisada o golpe", 0.25),
        ("Accidente de tránsito", 0.20),
        ("Sobreesfuerzo", 0.08),
        ("Caída de objeto", 0.05),
        ("Violencia", 0.05),
        ("Mordedura o picadura", 0.02),
        ("Otro", 0.05),
    ],

    # --------------------------------------------------------
    # TÉCNICOS
    # --------------------------------------------------------

    "Técnico de Mantenimiento": [
        ("Atrapamiento", 0.18),
        ("Caída de persona", 0.15),
        ("Caída de objeto", 0.14),
        ("Pisada o golpe", 0.12),
        ("Contacto con electricidad", 0.12),
        ("Elemento cortopunzante", 0.09),
        ("Sobreesfuerzo", 0.08),
        ("Temperatura extrema", 0.05),
        ("Sustancias nocivas", 0.04),
        ("Accidente de tránsito", 0.03),
    ],

    "Técnico de Seguridad Industrial": [
        ("Caída de persona", 0.18),
        ("Caída de objeto", 0.12),
        ("Pisada o golpe", 0.12),
        ("Atrapamiento", 0.08),
        ("Sobreesfuerzo", 0.08),
        ("Contacto con electricidad", 0.10),
        ("Elemento cortopunzante", 0.06),
        ("Accidente de tránsito", 0.08),
        ("Temperatura extrema", 0.08),
        ("Sustancias nocivas", 0.05),
        ("Exposición o contacto con agente biológico", 0.05),
    ],

    # --------------------------------------------------------
    # OPERATIVOS
    # --------------------------------------------------------

    "Conductor": [
        ("Accidente de tránsito", 0.45),
        ("Caída de persona", 0.12),
        ("Pisada o golpe", 0.10),
        ("Sobreesfuerzo", 0.08),
        ("Caída de objeto", 0.05),
        ("Violencia", 0.07),
        ("Mordedura o picadura", 0.03),
        ("Temperatura extrema", 0.03),
        ("Elemento cortopunzante", 0.02),
        ("Otro", 0.05),
    ],

    "Operador de Máquina": [
        ("Atrapamiento", 0.28),
        ("Caída de objeto", 0.15),
        ("Pisada o golpe", 0.12),
        ("Elemento cortopunzante", 0.10),
        ("Sobreesfuerzo", 0.10),
        ("Contacto con electricidad", 0.08),
        ("Caída de persona", 0.07),
        ("Temperatura extrema", 0.04),
        ("Sustancias nocivas", 0.03),
        ("Accidente de tránsito", 0.03),
    ],

    "Ayudante de Obra": [
        ("Caída de persona", 0.18),
        ("Caída de objeto", 0.16),
        ("Atrapamiento", 0.15),
        ("Pisada o golpe", 0.13),
        ("Sobreesfuerzo", 0.12),
        ("Elemento cortopunzante", 0.08),
        ("Contacto con electricidad", 0.06),
        ("Temperatura extrema", 0.05),
        ("Sustancias nocivas", 0.04),
        ("Accidente de tránsito", 0.03),
    ],

    # --------------------------------------------------------
    # AUXILIARES
    # --------------------------------------------------------

    "Auxiliar Contable": [
        ("Caída de persona", 0.35),
        ("Pisada o golpe", 0.30),
        ("Sobreesfuerzo", 0.12),
        ("Caída de objeto", 0.05),
        ("Accidente de tránsito", 0.07),
        ("Violencia", 0.04),
        ("Otro", 0.07),
    ],

    "Auxiliar Administrativo": [
        ("Caída de persona", 0.35),
        ("Pisada o golpe", 0.30),
        ("Sobreesfuerzo", 0.12),
        ("Caída de objeto", 0.05),
        ("Accidente de tránsito", 0.06),
        ("Violencia", 0.04),
        ("Otro", 0.08),
    ],

    "Auxiliar de Bodega": [
        ("Caída de persona", 0.16),
        ("Caída de objeto", 0.18),
        ("Pisada o golpe", 0.15),
        ("Atrapamiento", 0.14),
        ("Sobreesfuerzo", 0.13),
        ("Elemento cortopunzante", 0.07),
        ("Contacto con electricidad", 0.05),
        ("Temperatura extrema", 0.04),
        ("Sustancias nocivas", 0.04),
        ("Accidente de tránsito", 0.04),
    ],
}

COMPATIBILIDAD_DIAGNOSTICO_MORTALIDAD = {

    # ---------------------------------------------------------
    # TRAUMATISMO CRANEOENCEFÁLICO
    # ---------------------------------------------------------

    "S06.0": 0.0020,   # Conmoción cerebral
    "S06.9": 0.0080,   # Traumatismo intracraneal no especificado


    # ---------------------------------------------------------
    # FRACTURAS MAYORES
    # ---------------------------------------------------------

    "S72.0": 0.0015,   # Fractura del cuello del fémur
    "S72.3": 0.0015,   # Fractura de la diáfisis del fémur
    "S82.2": 0.0005,   # Fractura de la diáfisis de la tibia
    "S42.3": 0.0003,   # Fractura de la diáfisis del húmero
    "S52.5": 0.0002,   # Fractura de la epífisis inferior del radio


    # ---------------------------------------------------------
    # AMPUTACIONES
    # ---------------------------------------------------------

    "S68.1": 0.0005,   # Amputación traumática de un dedo
    "S78.9": 0.0030,   # Amputación traumática de cadera y muslo


    # ---------------------------------------------------------
    # QUEMADURAS
    # ---------------------------------------------------------

    "T20.2": 0.0010,   # Quemadura de segundo grado cabeza/cuello
    "T21.2": 0.0015,   # Quemadura de segundo grado tronco
    "T22.2": 0.0008,   # Quemadura de segundo grado hombro/miembro superior
    "T23.2": 0.0005,   # Quemadura de segundo grado muñeca/mano
}

SALARIOS_BASE_2016 = {

    # -----------------------------------------------------
    # DIRECTIVOS
    # -----------------------------------------------------

    "Gerente General": 8_000_000,

    "Director Operativo": 6_000_000,

    "Director Comercial": 5_500_000,


    # -----------------------------------------------------
    # COORDINADORES
    # -----------------------------------------------------

    "Coordinador Administrativo": 3_500_000,

    "Coordinador SST": 3_800_000,

    "Coordinador Logístico": 3_300_000,

    "Coordinador de Proyectos": 4_000_000,


    # -----------------------------------------------------
    # PROFESIONALES
    # -----------------------------------------------------

    "Profesional de Recursos Humanos": 3_000_000,

    "Profesional de Compras": 2_800_000,

    "Profesional de Calidad": 3_200_000,

    "Ingeniero de Proyectos": 4_000_000,


    # -----------------------------------------------------
    # COMERCIAL
    # -----------------------------------------------------

    "Vendedor": 2_000_000,


    # -----------------------------------------------------
    # TÉCNICOS
    # -----------------------------------------------------

    "Técnico de Mantenimiento": 2_200_000,

    "Técnico de Seguridad Industrial": 2_300_000,


    # -----------------------------------------------------
    # OPERATIVOS
    # -----------------------------------------------------

    "Conductor": 1_500_000,

    "Operador de Máquina": 1_600_000,

    "Ayudante de Obra": 1_350_000,


    # -----------------------------------------------------
    # AUXILIARES
    # -----------------------------------------------------

    "Auxiliar Contable": 1_500_000,

    "Auxiliar Administrativo": 1_400_000,

    "Auxiliar de Bodega": 1_350_000,
}

