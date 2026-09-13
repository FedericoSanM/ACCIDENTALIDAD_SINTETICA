# Accidentalidad Sintética

Generador de datos sintéticos de accidentalidad laboral para Colombia.

## Objetivo

ACCIDENTALIDAD_SINTETICA es un proyecto de generación de datos sintéticos
orientado al aprendizaje y desarrollo de soluciones de análisis de datos
en el contexto de la Seguridad y Salud en el Trabajo (SST).

El proyecto genera datasets de trabajadores y accidentalidad laboral
utilizando reglas de negocio, relaciones entre variables y escenarios
configurables, buscando producir información sintética con características
plausibles del mundo real.

Los datasets generados están diseñados para utilizarse como insumo en
procesos de ELT, limpieza, transformación, análisis exploratorio,
visualización, construcción de indicadores, desarrollo de modelos y
ejercicios relacionados con la toma de decisiones.

El proyecto no pretende ser una solución de análisis de accidentalidad
ni reemplazar herramientas de BI o análisis. Su propósito es proporcionar
un entorno controlado y reproducible sobre el cual puedan desarrollarse
este tipo de soluciones.

## Características principales

- Generación de trabajadores sintéticos con información demográfica y laboral.
- Generación de registros sintéticos de accidentalidad laboral.
- Simulación de múltiples accidentes para un mismo trabajador.
- Asignación de diagnósticos, lesiones, partes del cuerpo, mecanismos y agentes mediante reglas de compatibilidad.
- Clasificación de la gravedad de los accidentes de acuerdo con los criterios definidos para el proyecto.
- Generación de casos de mortalidad como categoría independiente.
- Cálculo de días de incapacidad considerando las reglas definidas para el escenario de accidentalidad.
- Simulación de accidentes relacionados con ventanas cercanas al retiro del trabajador.
- Generación de datos limpios (`CLEAN`) y datos con inconsistencias controladas (`DIRTY`) para practicar procesos de ELT, limpieza, transformación y análisis de datos.
- Exportación de las matrices generadas en formatos Excel y CSV.
- Ejecución de pruebas automatizadas mediante `pytest`.
- Generación de un informe anual descriptivo como apoyo a la revisión del comportamiento de una corrida del generador.
- Uso de una semilla para favorecer la reproducibilidad de la generación de datos.

## Estructura del proyecto

```text
ACCIDENTALIDAD_SINTETICA/
│
├── config/
│   ├── __init__.py
│   ├── parametros.py
│   └── rutas.py
│
├── src/
│   ├── __init__.py
│   ├── accidentalidad.py
│   ├── analisis_anual.py
│   ├── catalogos.py
│   ├── dataframes.py
│   ├── dirty.py
│   ├── exportacion.py
│   ├── main.py
│   └── trabajadores.py
│
├── pruebas/
│   ├── __init__.py
│   ├── test_catalogos.py
│   ├── test_compatibilidades.py
│   ├── test_diagnosticos.py
│   ├── test_dirty.py
│   ├── test_gravedad.py
│   ├── test_incapacidad.py
│   ├── test_integracion.py
│   ├── test_mortalidad.py
│   ├── test_reincidencia.py
│   └── test_retiro.py
│
├── data/
│   ├── sample/
│   └── dirty/
│
├── resultados/
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

### Descripción de las carpetas

| Carpeta | Contenido |
|---|---|
| `config/` | Parámetros generales y rutas del proyecto. |
| `src/` | Código fuente para generación, transformación, exportación y análisis de los datos. |
| `pruebas/` | Pruebas automatizadas del proyecto. |
| `data/sample/` | Archivos de datos sintéticos generados para el escenario CLEAN. |
| `data/dirty/` | Archivos de datos sintéticos con inconsistencias controladas para practicar procesos de ELT, limpieza, transformación y análisis de datos. |
| `resultados/` | Informes y resultados generados durante la ejecución. |


### Principales módulos

- `trabajadores.py`: generación y gestión de los datos sintéticos de trabajadores.
- `accidentalidad.py`: generación y gestión de los registros sintéticos de accidentalidad laboral.
- `catalogos.py`: definición de los catálogos utilizados por el proyecto.
- `dataframes.py`: transformación de los datos generados a estructuras `DataFrame`.
- `dirty.py`: generación de datos con inconsistencias controladas para practicar procesos de ELT, limpieza, transformación y análisis de datos.
- `exportacion.py`: exportación de las matrices generadas a formatos Excel y CSV.
- `analisis_anual.py`: construcción del informe anual descriptivo a partir de los datos generados.
- `main.py`: punto de entrada y orquestación del flujo principal del proyecto.

## Reglas de negocio

La generación de los datos se basa en un conjunto de reglas que buscan
mantener coherencia entre las diferentes variables del escenario.

Entre las principales reglas se encuentran:

- Los trabajadores se generan con información demográfica y laboral
  sintética.
- Las fechas de ingreso, retiro y accidente mantienen relaciones
  temporales coherentes.
- Un trabajador puede presentar uno o varios accidentes durante el
  período de análisis.
- Los diagnósticos, tipos de lesión, partes del cuerpo, mecanismos y
  agentes se generan mediante reglas de compatibilidad.
- La gravedad del accidente se determina mediante los criterios definidos
  para el proyecto.
- La mortalidad se maneja como una categoría independiente.
- Los días de incapacidad se generan dentro de los límites establecidos
  para el escenario.
- Los accidentes cercanos al retiro del trabajador se identifican mediante
  una ventana temporal específica.
- El salario se determina de acuerdo con el cargo y el área o proceso del
  trabajador.
- Los datos `DIRTY` se construyen a partir de los datos `CLEAN` mediante
  la introducción deliberada de inconsistencias controladas.
- La semilla (`SEED`) permite reproducir el escenario cuando se mantienen
  los mismos parámetros de generación.

## Personalización

Los principales parámetros de generación se encuentran centralizados en:

```text
config/parametros.py
```

Desde este archivo es posible modificar las condiciones generales del
escenario, como:
- Cantidad de trabajadores.
- Período de análisis.
- Fecha de corte.
- Semilla de generación (SEED).
- Tasas anuales de accidentalidad.
- Estacionalidad mensual.
- Límites relacionados con las incapacidades.
- Parámetros relacionados con los escenarios de retiro.

La modificación de estos parámetros permite generar diferentes escenarios
sintéticos sin modificar directamente la lógica principal de generación.

## Tecnologías utilizadas

- **Python 3.13** — lenguaje de programación principal.
- **Pandas** — creación y transformación de las matrices de datos.
- **NumPy** — operaciones y generación de valores utilizados por el proyecto.
- **Faker** — generación de datos sintéticos.
- **OpenPyXL** — generación de archivos Excel.
- **Pytest** — ejecución de pruebas automatizadas.

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd ACCIDENTALIDAD_SINTETICA
```

### 2. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows PowerShell o CMD:

```powershell
.\.venv\Scripts\Activate.ps1
```

```cmd
.venv\Scripts\activate.bat
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecución

Con el entorno virtual activado, ejecute:

```bash
python -m src.main
```

El flujo principal del proyecto realiza las siguientes etapas:

1. Genera los datos sintéticos CLEAN de trabajadores y accidentalidad.
2. Convierte las estructuras generadas a DataFrame.
3. Genera las versiones DIRTY a partir de los datos CLEAN, introduciendo inconsistencias controladas.
4. Exporta las matrices CLEAN y DIRTY en formatos Excel y CSV.
5. Presenta un resumen de la ejecución.
6. Genera un informe anual descriptivo a partir de los datos CLEAN.

Los archivos generados se almacenan en:
- data/sample/ — datasets CLEAN.
- data/dirty/ — datasets DIRTY.
- resultados/ — informe anual descriptivo.

## Pruebas

El proyecto cuenta con una suite de pruebas automatizadas desarrollada
con `pytest`.

Las pruebas verifican diferentes componentes y reglas de negocio del
generador, incluyendo:

- Catálogos y valores permitidos.
- Compatibilidad entre diagnósticos, lesiones, partes del cuerpo,
  mecanismos y agentes.
- Cobertura de diagnósticos.
- Generación de datos `DIRTY` con inconsistencias controladas.
- Clasificación de la gravedad de los accidentes.
- Cálculo de días de incapacidad.
- Casos de mortalidad.
- Reincidencia de accidentes.
- Reglas relacionadas con el retiro de trabajadores.
- Integración de los principales componentes del generador.

Para ejecutar todas las pruebas, utilice:

```bash
python -m pytest
```

Una ejecución correcta debe finalizar sin errores.

La suite de pruebas constituye el mecanismo automatizado de verificación
del comportamiento esperado del generador. El informe anual generado por
el proyecto tiene un propósito descriptivo y no reemplaza estas pruebas.

## Archivos generados

Al ejecutar:

```bash
python -m src.main
```

El proyecto genera los siguientes archivos.

### Datos CLEAN

Ubicación:

```text
data/sample/
```

Archivos:
- trabajadores_sinteticos.xlsx
- trabajadores_sinteticos.csv
- accidentalidad_sintetica.xlsx
- accidentalidad_sintetica.csv

Estos archivos contienen los datasets sintéticos generados a partir de
las reglas de negocio definidas para el escenario.

### Datos DIRTY

Ubicación:

```text
data/dirty/
```

Archivos:
- trabajadores_dirty.xlsx
- trabajadores_dirty.csv
- accidentalidad_dirty.xlsx
- accidentalidad_dirty.csv

Estos archivos se construyen a partir de los datos CLEAN mediante la
introducción deliberada de inconsistencias controladas. Su finalidad es
servir como insumo para ejercicios de ELT, limpieza, transformación y
validación de datos.

### Informe anual

Ubicación:

```text
resultados/
```

Archivo:
- validacion_anual.txt

El informe contiene un análisis descriptivo de la corrida realizada a
partir de los datos CLEAN. Incluye información resumida sobre el
comportamiento de la accidentalidad generada y diferentes distribuciones
del dataset.

El informe no constituye una segunda suite de pruebas ni reemplaza las
pruebas automatizadas ejecutadas mediante pytest.

## Datos sintéticos

Los datos generados por el proyecto son completamente sintéticos y no
corresponden a trabajadores, empresas, accidentes o registros reales.

El generador construye los datasets mediante reglas de negocio,
catálogos y parámetros configurables que permiten producir escenarios
coherentes para ejercicios de análisis y desarrollo.

### Matriz de trabajadores

La matriz de trabajadores contiene información sintética relacionada con
las características demográficas y laborales de los trabajadores
generados.

Entre otros elementos, puede incluir información relacionada con:

- Identificación sintética del trabajador.
- Información demográfica.
- Cargo.
- Área o proceso.
- Fechas de ingreso y retiro.
- Información salarial.

### Matriz de accidentalidad

La matriz de accidentalidad contiene registros sintéticos de accidentes
laborales relacionados con los trabajadores generados.

Entre las variables generadas se encuentran:

- Identificación del accidente.
- Identificación del trabajador.
- Fecha del accidente.
- Tipo de accidente.
- Mecanismo.
- Agente.
- Área del accidente.
- Código y diagnóstico.
- Tipo de lesión.
- Parte del cuerpo afectada.
- Gravedad del accidente.
- Días de incapacidad.
- Salario.

Las relaciones entre estas variables se generan mediante reglas de
compatibilidad y condiciones definidas en el proyecto.

### Escenarios controlados

El generador contempla diferentes escenarios para producir datos que
permitan probar comportamientos específicos, entre ellos:

- Trabajadores con uno o varios accidentes.
- Accidentes con diferentes niveles de gravedad.
- Casos de mortalidad.
- Diferentes escenarios de incapacidad.
- Accidentes próximos al retiro del trabajador.
- Datos `DIRTY` con inconsistencias controladas.

Estos escenarios buscan proporcionar un entorno reproducible para
desarrollar y probar procesos posteriores de ELT, limpieza,
transformación, análisis y visualización.

### Privacidad

El proyecto no requiere información personal ni datos reales para su
ejecución. Los registros generados tienen carácter exclusivamente
sintético y demostrativo.

## Reproducibilidad

El generador utiliza una semilla (`SEED`) para controlar la generación
aleatoria de los datos.

Cuando se mantienen la misma semilla y los mismos parámetros de
generación, es posible reproducir el mismo escenario sintético.

La semilla se encuentra definida en:

```text
config/parametros.py
```

Por ejemplo: SEED = 42

Modificar el valor de SEED permite generar un escenario diferente,
manteniendo las mismas reglas de negocio y parámetros generales.

La reproducibilidad depende de mantener constantes tanto la semilla como
los parámetros utilizados durante la generación.

## Alcance y limitaciones

### Alcance

ACCIDENTALIDAD_SINTETICA está orientado a la generación de datos
sintéticos de trabajadores y accidentalidad laboral para escenarios
relacionados con la Seguridad y Salud en el Trabajo (SST).

Los datos generados pueden utilizarse como insumo para:

- Ejercicios de ELT.
- Procesos de limpieza y transformación de datos.
- Análisis exploratorio.
- Construcción de indicadores.
- Visualización y desarrollo de dashboards.
- Pruebas de procesos y soluciones de datos.
- Desarrollo de modelos analíticos o de aprendizaje automático.
- Ejercicios académicos y de aprendizaje relacionados con datos.

El proyecto proporciona un entorno controlado para desarrollar estas
actividades sin utilizar información personal o registros reales.

### Limitaciones

- Los datos son completamente sintéticos y no representan una población
  laboral real.
- Las distribuciones y relaciones generadas corresponden a las reglas y
  parámetros definidos para el proyecto.
- Los escenarios generados no deben interpretarse como estadísticas
  oficiales de accidentalidad laboral.
- El proyecto no constituye un sistema de información para la gestión
  empresarial de SST.
- El proyecto no reemplaza herramientas de análisis, inteligencia de
  negocios (BI), sistemas de gestión ni fuentes oficiales de información.
- La clasificación y las reglas relacionadas con accidentalidad se
  implementan como parte del escenario sintético y no constituyen por sí
  mismas una interpretación jurídica o asesoría profesional.
- Los datos `DIRTY` contienen inconsistencias introducidas
  deliberadamente y no deben utilizarse como datos de referencia para
  análisis sin realizar previamente los procesos de limpieza
  correspondientes.

El propósito principal del proyecto es proporcionar datos sintéticos,
controlados y reproducibles sobre los cuales puedan desarrollarse y
probarse diferentes soluciones de datos.

## Licencia

Este proyecto se distribuirá bajo los términos de la licencia MIT.

La licencia MIT permite utilizar, copiar, modificar, distribuir y
reutilizar el código del proyecto, sujeto a las condiciones establecidas
en dicha licencia.

El proyecto utiliza únicamente datos sintéticos generados por el propio
sistema. No se incluyen datos personales ni registros reales de
trabajadores o accidentes.

El archivo `LICENSE` se incorporará al repositorio antes de la publicación
de la versión correspondiente.

## Uso de inteligencia artificial

Durante el desarrollo del proyecto se utilizaron herramientas de
inteligencia artificial como apoyo para:

- Diseño y revisión de la arquitectura del proyecto.
- Desarrollo y refactorización de código.
- Análisis y resolución de errores.
- Diseño de pruebas automatizadas.
- Revisión de reglas de negocio y relaciones entre variables.
- Estructuración y documentación del proyecto.
- Revisión de la organización y presentación del repositorio.

La inteligencia artificial se utilizó como herramienta de apoyo al
desarrollo. Las decisiones sobre la lógica del generador, las reglas de
negocio, los escenarios, la estructura de los datos y la validación del
comportamiento fueron revisadas durante el desarrollo del proyecto.

Los datos generados por el proyecto son sintéticos y no provienen de
información personal utilizada como fuente de generación.

## Autor

**Federico Sanín**

Administrador Ambiental · Especialista en Seguridad y Salud en el
Trabajo (SST)

Profesional en transición hacia el análisis de datos, con experiencia en
gestión de riesgos, Seguridad y Salud en el Trabajo, ambiente, calidad y
gestión del talento humano.

Este proyecto forma parte del proceso de aprendizaje y transición
profesional hacia el análisis y desarrollo de soluciones basadas en datos.

### Perfil profesional

- Excel
- Power BI
- Power Query
- SQL
- Python
- Análisis y visualización de datos
- Gestión de riesgos
- Seguridad y Salud en el Trabajo (SST)
- Sistemas integrados de gestión