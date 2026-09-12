from faker import Faker
from datetime import date, timedelta

from src.catalogos import (
    GENEROS,
    CIUDADES_DEPARTAMENTOS,
    CARGOS,
    TIPOS_VINCULACION,
)

from config.parametros import (
    FECHA_INICIO_EMPRESA,
    FECHA_INICIO_ANALISIS,
    FECHA_CORTE,
    SEED,
)

def crear_faker():
    """Crea y configura el generador de datos ficticios."""
    faker = Faker("es_CO")
    faker.seed_instance(SEED)

    return faker


def determinar_sexo_nombre(faker, genero):
    """Determina el patrón nominal utilizado para generar el nombre."""

    if genero == "Masculino":
        return "Masculino"

    if genero == "Femenino":
        return "Femenino"

    return faker.random_element(
        elements=["Masculino", "Femenino"]
    )


def generar_nombre(faker, sexo_nombre):
    """Genera un nombre completo según el patrón nominal."""

    if sexo_nombre == "Femenino":
        generador_nombre = faker.first_name_female
    else:
        generador_nombre = faker.first_name_male

    cantidad_nombres = faker.random_int(min=1, max=2)
    cantidad_apellidos = faker.random_int(min=1, max=2)

    nombres = [generador_nombre()]

    if cantidad_nombres == 2:
        segundo_nombre = generador_nombre()

        while segundo_nombre == nombres[0]:
            segundo_nombre = generador_nombre()

        nombres.append(segundo_nombre)

    apellidos = [
        faker.last_name()
        for _ in range(cantidad_apellidos)
    ]

    return " ".join(nombres + apellidos)


def calcular_edad(fecha_nacimiento, fecha_corte):
    """Calcula la edad cumplida a una fecha determinada."""
    edad = fecha_corte.year - fecha_nacimiento.year

    if (
        fecha_corte.month,
        fecha_corte.day
    ) < (
        fecha_nacimiento.month,
        fecha_nacimiento.day
    ):
        edad -= 1

    return edad


def calcular_fecha_mayoria_edad(fecha_nacimiento):
    """Calcula la fecha en que el trabajador cumple 18 años."""

    try:
        return fecha_nacimiento.replace(
            year = fecha_nacimiento.year + 18
        )
    except ValueError:
        return fecha_nacimiento.replace(
            year = fecha_nacimiento.year + 18,
            day = 28,
        )


def generar_fecha_ingreso(
    faker,
    fecha_nacimiento,
    fecha_inicio_empresa,
    fecha_corte,
):
    """Genera una fecha de ingreso laboral válida."""

    fecha_minima = max(
        fecha_inicio_empresa,
        calcular_fecha_mayoria_edad(fecha_nacimiento),
    )

    if fecha_minima > fecha_corte:
        raise ValueError(
            f"No existe una fecha de ingreso válida: "
            f"fecha mínima {fecha_minima} > "
            f"fecha máxima {fecha_corte}."
        )

    return faker.date_between(
        start_date=fecha_minima,
        end_date=fecha_corte,
    )


def contar_activos(trabajadores, fecha):
    """Cuenta los trabajadores activos en una fecha determinada."""

    return sum(
        1
        for trabajador in trabajadores
        if trabajador["fecha_ingreso"] <= fecha
        and (
            trabajador["fecha_retiro"] is None
            or trabajador["fecha_retiro"] > fecha
        )
    )


def calibrar_poblacion(trabajadores, faker):
    """Ajusta ingresos y retiros para aproximar la población objetivo."""

    fecha_inicio_empresa = date.fromisoformat(FECHA_INICIO_EMPRESA)
    fecha_inicio_analisis = date.fromisoformat(FECHA_INICIO_ANALISIS)
    fecha_corte = date.fromisoformat(FECHA_CORTE)

    # El período histórico termina el día anterior al inicio del análisis.
    fecha_fin_historicos = fecha_inicio_analisis - timedelta(days = 1)

    # Mezclamos los trabajadores para evitar que el ID determine
    # la cohorte a la que pertenece cada trabajador.
    faker.random.shuffle(trabajadores)

    # ---------------------------------------------------------
    # 1. Selección de trabajadores históricos
    # ---------------------------------------------------------

    fecha_limite_ingreso_historico = (
        fecha_fin_historicos - timedelta(days = 30)
    )

    trabajadores_elegibles_historicos = [
        trabajador
        for trabajador in trabajadores
        if calcular_fecha_mayoria_edad(
            trabajador["fecha_nacimiento"]
        ) <= fecha_limite_ingreso_historico
    ]

    if len(trabajadores_elegibles_historicos) < 100:
        raise ValueError(
            "No existen suficientes trabajadores elegibles "
            "para formar la cohorte histórica."
        )

    historicos = faker.random.sample(
        trabajadores_elegibles_historicos,
        100,
    )

    ids_historicos = {
        trabajador["id_trabajador"]
        for trabajador in historicos
    }

    # ---------------------------------------------------------
    # 2. Trabajadores disponibles después de seleccionar
    #    la cohorte histórica
    # ---------------------------------------------------------

    trabajadores_disponibles = [
        trabajador
        for trabajador in trabajadores
        if trabajador["id_trabajador"] not in ids_historicos
    ]

    # ---------------------------------------------------------
    # 3. Selección de trabajadores activos al inicio
    #    del período de análisis
    # ---------------------------------------------------------

    trabajadores_elegibles_iniciales = [
        trabajador
        for trabajador in trabajadores_disponibles
        if calcular_fecha_mayoria_edad(
            trabajador["fecha_nacimiento"]
        ) <= fecha_inicio_analisis
    ]

    if len(trabajadores_elegibles_iniciales) < 550:
        raise ValueError(
            "No existen suficientes trabajadores elegibles "
            "para estar activos al inicio del análisis."
        )

    iniciales = faker.random.sample(
        trabajadores_elegibles_iniciales,
        550,
    )

    ids_iniciales = {
        trabajador["id_trabajador"]
        for trabajador in iniciales
    }

    # ---------------------------------------------------------
    # 4. Los restantes serán nuevos trabajadores durante
    #    el período de análisis
    # ---------------------------------------------------------

    nuevos = [
        trabajador
        for trabajador in trabajadores_disponibles
        if trabajador["id_trabajador"] not in ids_iniciales
    ]

    # ---------------------------------------------------------
    # 5. Trabajadores históricos:
    #    ingresan y se retiran antes del análisis
    # ---------------------------------------------------------

    for trabajador in historicos:

        trabajador["fecha_ingreso"] = generar_fecha_ingreso(
            faker,
            trabajador["fecha_nacimiento"],
            fecha_inicio_empresa,
            fecha_fin_historicos - timedelta(days = 30),
        )

        fecha_minima_retiro = (
            trabajador["fecha_ingreso"]
            + timedelta(days = 30)
        )

        trabajador["fecha_retiro"] = faker.date_between(
            start_date = fecha_minima_retiro,
            end_date = fecha_fin_historicos,
        )

    # ---------------------------------------------------------
    # 6. Trabajadores activos al inicio del análisis
    # ---------------------------------------------------------

    for trabajador in iniciales:

        trabajador["fecha_ingreso"] = generar_fecha_ingreso(
            faker,
            trabajador["fecha_nacimiento"],
            fecha_inicio_empresa,
            fecha_inicio_analisis,
        )

        trabajador["fecha_retiro"] = None

    # ---------------------------------------------------------
    # 7. Nuevos trabajadores durante el período de análisis
    # ---------------------------------------------------------

    cantidad_por_cohorte = len(nuevos) // 3

    fecha_inicio_cohorte = fecha_inicio_analisis

    cohortes_ingreso = []

    for i in range(3):

        fecha_fin_cohorte = (
            fecha_inicio_cohorte
            + timedelta(days = 365)
            - timedelta(days = 1)
        )

        inicio = i * cantidad_por_cohorte
        fin = (
            (i + 1) * cantidad_por_cohorte
            if i < 2
            else len(nuevos)
        )

        cohortes_ingreso.append(
            (
                nuevos[inicio:fin],
                fecha_inicio_cohorte,
                fecha_fin_cohorte,
            )
        )

        fecha_inicio_cohorte = (
            fecha_fin_cohorte + timedelta(days = 1)
        )

    for grupo, fecha_inicio, fecha_fin in cohortes_ingreso:

        for trabajador in grupo:

            trabajador["fecha_ingreso"] = generar_fecha_ingreso(
                faker,
                trabajador["fecha_nacimiento"],
                fecha_inicio,
                fecha_fin,
            )

            trabajador["fecha_retiro"] = None

    # ---------------------------------------------------------
    # 8. Retiros durante el período de análisis
    # ---------------------------------------------------------

    grupos_retiro = [
        (
            iniciales[:25],
            fecha_inicio_analisis + timedelta(days = 184),
            fecha_inicio_analisis + timedelta(days = 364),
        ),
        (
            iniciales[25:50],
            fecha_inicio_analisis + timedelta(days = 549),
            fecha_inicio_analisis + timedelta(days = 729),
        ),
        (
            iniciales[50:75],
            fecha_inicio_analisis + timedelta(days = 914),
            fecha_inicio_analisis + timedelta(days = 1094),
        ),
        (
            iniciales[75:100],
            fecha_corte - timedelta(days = 180),
            fecha_corte,
        ),
    ]

    for grupo, fecha_inicio, fecha_fin in grupos_retiro:

        for trabajador in grupo:

            fecha_minima_retiro = max(
                trabajador["fecha_ingreso"] + timedelta(days = 30),
                fecha_inicio,
            )

            trabajador["fecha_retiro"] = faker.date_between(
                start_date = fecha_minima_retiro,
                end_date = fecha_fin,
            )

    # ---------------------------------------------------------
    # 9. Calcular edad en el último momento observado
    # ---------------------------------------------------------

    for trabajador in trabajadores:
        fecha_referencia = (
            trabajador["fecha_retiro"]
            if trabajador["fecha_retiro"] is not None
            else fecha_corte
        )

        trabajador["edad"] = calcular_edad(
            trabajador["fecha_nacimiento"],
            fecha_referencia,
        )

    # ---------------------------------------------------------
    # 10. Ordenar nuevamente el registro por ID_TRABAJADOR
    # ---------------------------------------------------------

    trabajadores.sort(
    key = lambda trabajador: trabajador["id_trabajador"]
)
    
    return trabajadores


def poblacion_objetivo_en_fecha(fecha, poblacion_objetivo):
    """Obtiene la población objetivo correspondiente a una fecha."""

    fechas = [
        date.fromisoformat(fecha_objetivo)
        for fecha_objetivo in poblacion_objetivo
    ]

    fecha_anterior = max(
        fecha_objetivo
        for fecha_objetivo in fechas
        if fecha_objetivo <= fecha
    )

    return poblacion_objetivo[fecha_anterior.isoformat()]


def generar_trabajadores(cantidad):
    """Genera una población sintética de trabajadores."""

    faker = crear_faker()

    trabajadores = []

    for i in range(1, cantidad + 1):

        genero = faker.random_element(
            elements = GENEROS
        )

        sexo_nombre = determinar_sexo_nombre(
            faker,
            genero,
        )

        fecha_nacimiento = faker.date_of_birth(
            minimum_age = 23,
            maximum_age = 65,
        )

        nombre = generar_nombre(
            faker,
            sexo_nombre,
        )

        ciudad = faker.random_element(
            elements = list(CIUDADES_DEPARTAMENTOS.keys())
        )

        departamento = CIUDADES_DEPARTAMENTOS[ciudad]

        cargo = faker.random_element(
            elements = list(CARGOS.keys())
        )

        nivel = CARGOS[cargo]["nivel"]

        area = faker.random_element(
            elements = CARGOS[cargo]["areas"]
        )

        tipo_vinculacion = faker.random_element(
            elements = TIPOS_VINCULACION
        )
                
        trabajador = {
            "id_trabajador": i,
            "nombre": nombre,
            "fecha_nacimiento": fecha_nacimiento,
            "edad": None,
            "genero": genero,
            "ciudad": ciudad,
            "departamento": departamento,
            "cargo": cargo,
            "nivel": nivel,
            "area_proceso": area,
            "tipo_vinculacion": tipo_vinculacion,
            "fecha_ingreso": None,
            "fecha_retiro": None,
        }

        trabajadores.append(trabajador)

    trabajadores = calibrar_poblacion(
        trabajadores,
        faker,
    )

    return trabajadores


def validar_trabajadores(trabajadores):
    """Valida la coherencia temporal de los trabajadores."""

    errores = []

    for trabajador in trabajadores:

        id_trabajador = trabajador["id_trabajador"]
        nacimiento = trabajador["fecha_nacimiento"]
        ingreso = trabajador["fecha_ingreso"]
        retiro = trabajador["fecha_retiro"]
        edad = trabajador["edad"]

        # 1. La fecha de ingreso debe existir.
        if ingreso is None:
            errores.append(
                f"Trabajador {id_trabajador}: "
                "fecha_ingreso es None."
            )
            continue

        # 2. El ingreso no puede ser anterior al nacimiento.
        if ingreso < nacimiento:
            errores.append(
                f"Trabajador {id_trabajador}: "
                "fecha_ingreso anterior a fecha_nacimiento."
            )

        # 3. El trabajador debe tener al menos 18 años
        #    al momento del ingreso.
        edad_al_ingreso = calcular_edad(
            nacimiento,
            ingreso,
        )

        if edad_al_ingreso < 18:
            errores.append(
                f"Trabajador {id_trabajador}: "
                f"ingresó con {edad_al_ingreso} años."
            )

        # 4. Si existe retiro, debe ser posterior al ingreso.
        if retiro is not None:

            if retiro <= ingreso:
                errores.append(
                    f"Trabajador {id_trabajador}: "
                    "fecha_retiro no es posterior "
                    "a fecha_ingreso."
                )

            # 5. La edad almacenada debe corresponder
            #    a la edad al momento del retiro.
            edad_esperada = calcular_edad(
                nacimiento,
                retiro,
            )

        else:

            # 6. Si continúa activo, la edad debe corresponder
            #    a la fecha de corte.
            edad_esperada = calcular_edad(
                nacimiento,
                date.fromisoformat(FECHA_CORTE),
            )

        if edad != edad_esperada:
            errores.append(
                f"Trabajador {id_trabajador}: "
                f"edad incorrecta. "
                f"Esperada={edad_esperada}, "
                f"obtenida={edad}."
            )

    return errores


def validar_relaciones_trabajadores(trabajadores):
    """Valida las relaciones entre los atributos de los trabajadores."""

    errores = []

    for trabajador in trabajadores:

        id_trabajador = trabajador["id_trabajador"]
        ciudad = trabajador["ciudad"]
        departamento = trabajador["departamento"]
        cargo = trabajador["cargo"]
        nivel = trabajador["nivel"]
        area = trabajador["area_proceso"]
        salario = trabajador["salario"] 

        # 1. Ciudad → Departamento
        departamento_esperado = CIUDADES_DEPARTAMENTOS.get(
            ciudad
        )

        if departamento != departamento_esperado:
            errores.append(
                f"Trabajador {id_trabajador}: "
                f"departamento incorrecto para {ciudad}."
            )

        # 2. Cargo → Nivel
        cargo_info = CARGOS.get(cargo)

        if cargo_info is None:
            errores.append(
                f"Trabajador {id_trabajador}: "
                f"cargo '{cargo}' no existe en el catálogo."
            )
            continue

        if nivel != cargo_info["nivel"]:
            errores.append(
                f"Trabajador {id_trabajador}: "
                f"nivel incorrecto para cargo '{cargo}'."
            )

        # 3. Cargo → Área/Proceso
        areas_permitidas = cargo_info["areas"]

        if area not in areas_permitidas:
            errores.append(
                f"Trabajador {id_trabajador}: "
                f"área '{area}' no permitida para "
                f"cargo '{cargo}'."
            )

    return errores


def validar_dataset_trabajadores(trabajadores):
    """Ejecuta todas las validaciones del dataset de trabajadores."""

    errores_temporales = validar_trabajadores(
        trabajadores
    )

    errores_relaciones = validar_relaciones_trabajadores(
        trabajadores
    )

    errores = (
        errores_temporales
        + errores_relaciones
    )

    return errores



