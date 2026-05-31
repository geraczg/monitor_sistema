# Monitor de Sistema

Monitor de sistema en Python pensado para portafolio. Muestra en tiempo real el uso de CPU, memoria, disco y red, y puede guardar snapshots en CSV para analizar el comportamiento del equipo.

## Caracteristicas

- Lectura de metricas del sistema con `psutil`.
- Vista en consola con refresco configurable.
- Alertas simples cuando CPU, memoria o disco superan un umbral.
- Exportacion opcional a CSV.
- Pruebas unitarias para la logica de alertas y formato.

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

Ejecutar el monitor:

```powershell
python -m src.monitor
```

Cambiar intervalo, umbral de alerta y guardar CSV:

```powershell
python -m src.monitor --interval 2 --threshold 75 --csv logs/metrics.csv
```

Tomar una sola lectura, util para demos o pruebas rapidas:

```powershell
python -m src.monitor --once
```

## Flujo Git recomendado

1. `git add README.md requirements.txt .gitignore src tests`
2. `git commit -m "chore: scaffold system monitor project"`
3. `git commit -m "feat: add live system metrics monitor"`
4. `git commit -m "test: cover alert and formatting helpers"`

Para un portafolio, conviene que cada commit cuente una parte del trabajo: estructura, funcionalidad, pruebas y pulido visual/documental.
