# Monitor de Sistema

Herramienta de consola en Python para diagnostico basico de recursos del sistema. 

## Objetivo

El monitor permite revisar rápidamente el estado de una computadora, detectar consumo alto de recursos y generar un reporte local que puede servir como evidencia inicial antes de escalar un incidente.

## Funciones principales

- Consulta información general del equipo: sistema operativo, versión y nombre del host.
- Mide uso actual de CPU, RAM y disco con `psutil`.
- Clasifica cada recurso como `OK`, `ADVERTENCIA` o `CRITICO`.
- Genera alertas cuando CPU, RAM o disco superan los limites definidos.
- Muestra recomendaciones prácticas según el recurso afectado.
- Permite ejecutar un diagnóstico rapido con `--once`.
- Permite ajustar los limites de advertencia y crítico desde consola.
- Crea reportes TXT dentro de la carpeta `reports`.
- Incluye pruebas unitarias para diagnóstico, alertas y reportes.

## Tecnologías usadas

- Python 3
- psutil
- unittest
- Git

## Instalación

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

## Ejecución

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

Ejecutar un diagnóstico rápido sin entrar al menú:

```powershell
python -m src.monitor --once
```

Para ajustar los límites de diagnóstico:

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

Al elegir la opción `2`, la aplicación genera un archivo TXT en `reports` con:

- fecha y hora del diagnóstico;
- información del equipo;
- estado general;
- uso de CPU, RAM y disco;
- alertas detectadas;
- recomendaciones de acción.

Ejemplo de archivo generado:

```text
reports/system_report_20260605_123000.txt
```

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
