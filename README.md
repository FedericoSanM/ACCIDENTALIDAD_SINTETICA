# Accidentalidad Sintética

Generador de datos sintéticos de accidentalidad laboral para Colombia.

## Objetivo

Generar datos sintéticos de trabajadores y accidentalidad laboral
que permitan practicar procesos de ELT, realizar pruebas, análisis
y desarrollar soluciones relacionadas con la gestión de la seguridad
y salud en el trabajo (SST), sin utilizar información personal o datos
reales.

## Características principales

- Generación de trabajadores sintéticos con información demográfica y laboral.
- Generación de registros sintéticos de accidentalidad laboral.
- Simulación de múltiples accidentes para un mismo trabajador.
- Asignación de diagnósticos, lesiones, partes del cuerpo, mecanismos y agentes de acuerdo con reglas de compatibilidad.
- Clasificación de la gravedad de los accidentes de acuerdo con los criterios definidos para el proyecto.
- Generación de casos de mortalidad como categoría independiente.
- Cálculo de días de incapacidad considerando las reglas definidas para el escenario de accidentalidad.
- Simulación de accidentes relacionados con ventanas cercanas al retiro del trabajador.
- Generación de datos limpios (`CLEAN`) y datos con inconsistencias controladas (`DIRTY`) para practicar procesos de ELT,
  limpieza, transformación y análisis de datos.
- Exportación de las matrices generadas en formatos Excel y CSV.
- Ejecución de pruebas automatizadas mediante `pytest`.
- Generación de un informe anual descriptivo a partir de los datos generados.
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

```markdown
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

El proceso genera:
- Matriz sintética de trabajadores.
- Matriz sintética de accidentalidad laboral.
- Versiones `DIRTY` de las matrices con inconsistencias controladas para practicar 
  procesos de ELT, limpieza, transformación y análisis de datos.
- Archivos en formato Excel y CSV.
- Informe anual descriptivo.

## Pruebas

El proyecto cuenta con una suite de pruebas automatizadas desarrollada
con `pytest`.

Para ejecutar todas las pruebas, utilice:

```bash
python -m pytest
```

Las pruebas verifican diferentes componentes y reglas del proyecto, incluyendo:
- Catálogos.
- Compatibilidad de los datos.
- Diagnósticos.
- Reglas relacionadas con la generación de datos `DIRTY`.
- Gravedad de los accidentes.
- Incapacidades.
- Integración de los componentes.
- Mortalidad.
- Reincidencia.
- Retiro de trabajadores.

Una ejecución correcta debe finalizar sin errores.

## Archivos generados

Al ejecutar el proyecto se generan archivos sintéticos en las siguientes
ubicaciones:

### Datos sintéticos CLEAN

Ubicación:

```text
data/sample/
```

Contiene las matrices sintéticas generadas sin inconsistencias controladas:
- trabajadores_sinteticos.xlsx
- trabajadores_sinteticos.csv
- accidentalidad_sintetica.xlsx
- accidentalidad_sintetica.csv

### Datos sintéticos DIRTY

Ubicación:

```text
data/dirty/
```

Los datos `DIRTY` permiten trabajar con situaciones similares a las que
pueden encontrarse en procesos reales de preparación y calidad de datos:

- trabajadores_dirty.xlsx
- trabajadores_dirty.csv
- accidentalidad_dirty.xlsx
- accidentalidad_dirty.csv

### Informe anual

Ubicación:

```text
resultados/
```

Contiene:
- validacion_anual.txt

El informe presenta un análisis descriptivo de los datos generados
para el período anual.

## Datos sintéticos

Los datos generados por este proyecto son completamente sintéticos.
No corresponden a trabajadores, accidentes ni situaciones reales.

Su propósito es proporcionar un conjunto de datos controlado para
pruebas, análisis y desarrollo de soluciones relacionadas con la
accidentalidad laboral y la gestión de SST.

### Datos CLEAN

Los datos `CLEAN` representan registros generados de acuerdo con las
reglas definidas para el proyecto y constituyen la base a partir de la
cual se generan los datos `DIRTY`.

### Datos DIRTY

Los datos `DIRTY` se generan a partir de las matrices `CLEAN` mediante
la introducción controlada de inconsistencias.

El objetivo de los datos `DIRTY` es proporcionar un conjunto de
datos para practicar:

- Procesos de ELT.
- Identificación y tratamiento de inconsistencias.
- Limpieza y transformación de datos.
- Análisis exploratorio y descriptivo.
- Construcción de indicadores.
- Generación de visualizaciones.
- Obtención de información para apoyar la toma de decisiones.

Las inconsistencias son intencionales y forman parte del diseño del
conjunto de datos de práctica.

### Privacidad

El proyecto no requiere información personal ni datos reales para su
ejecución. Los registros generados tienen carácter exclusivamente
sintético y demostrativo.

## Reproducibilidad

El proyecto utiliza semillas (`SEED`) para controlar la generación de
datos aleatorios y favorecer la reproducibilidad de los resultados.

Esto permite obtener resultados reproducibles cuando se ejecuta el
proyecto con los mismos parámetros y la misma configuración.

La reproducibilidad permite:

- Repetir una ejecución.
- Comparar resultados entre diferentes ejecuciones.
- Facilitar las pruebas y la validación del proyecto.
- Permitir que otras personas reproduzcan el escenario de datos
  sintéticos.

Los datos generados no se almacenan como parte del repositorio.
Cada usuario puede generarlos localmente siguiendo las instrucciones
de instalación y ejecución.

## Alcance y limitaciones

### Alcance

El proyecto está orientado a la generación de datos sintéticos de
trabajadores y accidentalidad laboral para Colombia.

Su diseño permite disponer de un escenario controlado para:

- Desarrollo y prueba de soluciones de datos.
- Pruebas de procesos de calidad y validación de datos.
- Práctica de procesos de ELT.
- Limpieza y transformación de datos.
- Análisis de accidentalidad laboral.
- Construcción de indicadores y visualizaciones.
- Práctica de análisis orientado a la toma de decisiones.

El proyecto también incorpora pruebas automatizadas para verificar
las reglas y condiciones implementadas en la generación de los datos.

### Limitaciones

- Los datos son completamente sintéticos y no representan una población laboral real.
- Los registros no deben utilizarse para establecer conclusiones sobre la accidentalidad laboral de Colombia.
- Las distribuciones, probabilidades y reglas utilizadas corresponden al escenario definido para este proyecto.
- Los datos `DIRTY` contienen inconsistencias introducidas deliberadamente para fines de práctica y análisis.
- El proyecto no pretende reemplazar fuentes oficiales de información ni sistemas reales de gestión de SST.
- Los resultados obtenidos a partir de los datos sintéticos dependen de los parámetros y condiciones de generación utilizados.

## Licencia

Este proyecto se distribuirá bajo los términos de la licencia MIT.

La licencia permite utilizar, copiar, modificar, distribuir y reutilizar
el proyecto, sujeto a las condiciones establecidas en la licencia.

El archivo `LICENSE` se incorporará al repositorio antes de su publicación.

## Uso de inteligencia artificial

Este proyecto fue desarrollado con apoyo de herramientas de inteligencia
artificial utilizadas como asistente durante el proceso de desarrollo.

La IA se utilizó para apoyar actividades como generación y revisión de
código, estructuración de componentes, elaboración de pruebas,
documentación y resolución de problemas técnicos.

Las reglas de negocio, parámetros, objetivos del proyecto y criterios
de validación fueron definidos y revisados durante el proceso de
desarrollo. Los resultados generados por la IA fueron sometidos a
revisión, pruebas y ajustes antes de incorporarse al proyecto.

El uso de IA se entiende como una herramienta de apoyo al desarrollo y
no como sustituto de la definición del problema, el criterio técnico,
la revisión de resultados y la toma de decisiones.

## Autor

**Federico Sanín Medina**

Profesional en transición hacia el análisis de datos, con experiencia en
gestión de riesgos, seguridad y salud en el trabajo (SST), ambiente,
calidad y gestión del talento humano.

Este proyecto forma parte del portafolio de desarrollo y análisis de
datos.