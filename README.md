# Monitor de Sistema

Herramienta de consola en Python para diagnostico basico de recursos del sistema. El proyecto esta orientado a un perfil de **Soporte TI Jr** y busca demostrar fundamentos de monitoreo, automatizacion, reportes y buenas practicas con Git/GitHub.

## Objetivo

El monitor permite revisar rapidamente el estado de una computadora, detectar consumo alto de recursos y generar un reporte local que puede servir como evidencia inicial antes de escalar un incidente.

## Funciones principales

- Consulta informacion general del equipo: sistema operativo, version y nombre del host.
- Mide uso actual de CPU, RAM y disco con `psutil`.
- Clasifica cada recurso como `OK`, `ADVERTENCIA` o `CRITICO`.
- Genera alertas cuando CPU, RAM o disco superan los limites definidos.
- Muestra recomendaciones practicas segun el recurso afectado.
- Permite ejecutar un diagnostico rapido con `--once`.
- Permite ajustar los limites de advertencia y critico desde consola.
- Crea reportes TXT dentro de la carpeta `reports`.
- Incluye pruebas unitarias para diagnostico, alertas y reportes.

## Tecnologias usadas

- Python 3
- psutil
- unittest
- Git

## Instalacion

Clona o descarga el repositorio y entra a la carpeta del proyecto:

```powershell
cd "Monitor de Sistema"
```

Crea un entorno virtual:

```powershell
python -m venv .venv
```

Activa el entorno virtual en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecucion

Ejecuta el monitor desde la raiz del proyecto:

```powershell
python -m src.monitor
```

El menu principal permite:

```text
Menu
1. Ver estado del sistema
2. Generar reporte
3. Ver recomendaciones
4. Salir
Seleccione una opcion:
```

Tambien puedes ejecutar un diagnostico rapido sin entrar al menu:

```powershell
python -m src.monitor --once
```

Para ajustar los limites de diagnostico:

```powershell
python -m src.monitor --once --warning 75 --critical 90
```

## Ejemplo de salida

```text
Monitor de Sistema
===================
Estado general: ADVERTENCIA
Limites usados: advertencia >= 80% | critico >= 90%
Sistema operativo: Windows
Version: 10.0.26200
Equipo: LAPTOP-TEST

Uso de recursos
CPU: 15.8% - OK
RAM: 85.8% - ADVERTENCIA
Disco: 66.9% - OK

Alertas
- ADVERTENCIA: RAM alta (85.8%).
```

## Reportes

Al elegir la opcion `2`, la aplicacion genera un archivo TXT en `reports` con:

- fecha y hora del diagnostico;
- informacion del equipo;
- estado general;
- uso de CPU, RAM y disco;
- alertas detectadas;
- recomendaciones de accion.

Ejemplo de archivo generado:

```text
reports/system_report_20260605_123000.txt
```

Tambien se incluye un reporte ficticio de ejemplo en `docs/example_report.txt`.

Los reportes generados se ignoran en Git para mantener limpio el repositorio.

## Pruebas

Ejecuta las pruebas con `unittest`:

```powershell
python -m unittest discover tests
```

## Estructura del proyecto

```text
monitor-sistema/
|
|-- src/
|   |-- __init__.py
|   |-- alerts.py
|   |-- diagnostics.py
|   |-- models.py
|   |-- monitor.py
|   |-- reports.py
|   `-- system_info.py
|
|-- reports/
|   `-- .gitkeep
|
|-- docs/
|   `-- example_report.txt
|
|-- tests/
|   |-- test_alerts.py
|   |-- test_monitor.py
|   `-- test_reports.py
|
|-- .gitignore
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Habilidades que demuestra

- Uso de librerias para monitoreo basico del sistema.
- Separacion de responsabilidades en modulos pequenos.
- Manejo de estructuras de datos con `dataclass`.
- Generacion de reportes locales.
- Pruebas unitarias para logica de negocio.
- Preparacion de un repositorio limpio para portafolio.

## Alcance

Este proyecto no pretende reemplazar herramientas profesionales de monitoreo. Su objetivo es mostrar una solucion sencilla, explicable y mantenible para diagnostico basico en un contexto de Soporte TI Jr.
