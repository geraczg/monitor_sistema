from __future__ import annotations

from src.metrics import SystemMetrics


def format_bytes(value: int) -> str:
    units = ("B", "KB", "MB", "GB", "TB")
    size = float(value)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} TB"


def build_alerts(metrics: SystemMetrics, threshold: float) -> list[str]:
    checks = {
        "CPU": metrics.cpu_percent,
        "Memoria": metrics.memory_percent,
        "Disco": metrics.disk_percent,
    }

    return [
        f"{name} alto: {value:.1f}%"
        for name, value in checks.items()
        if value >= threshold
    ]


def render_snapshot(metrics: SystemMetrics, threshold: float) -> str:
    alerts = build_alerts(metrics, threshold)
    alert_text = "\n".join(f"  ! {alert}" for alert in alerts) if alerts else "  Sin alertas"

    return "\n".join(
        [
            "Monitor de Sistema",
            "=" * 19,
            f"Hora:       {metrics.timestamp}",
            f"CPU:        {metrics.cpu_percent:5.1f}%",
            f"Memoria:    {metrics.memory_percent:5.1f}%",
            f"Disco:      {metrics.disk_percent:5.1f}%",
            f"Red envio:  {format_bytes(metrics.bytes_sent)}",
            f"Red recibo: {format_bytes(metrics.bytes_recv)}",
            "",
            "Alertas:",
            alert_text,
        ]
    )
