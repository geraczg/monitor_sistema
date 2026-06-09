from __future__ import annotations

from pathlib import Path

from src.diagnostics import (
    CRITICAL_LIMIT,
    WARNING_LIMIT,
    get_alerts,
    get_overall_status,
    get_recommendations,
    get_resource_diagnostics,
)
from src.models import ResourceUsage, SystemDetails

REPORTS_DIR = Path("reports")


def build_report_content(
    details: SystemDetails,
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> str:
    """Build the plain text content for a system status report."""
    alerts = get_alerts(usage, warning_limit, critical_limit)
    alert_lines = alerts if alerts else ["Sin alertas."]
    recommendations = get_recommendations(usage, warning_limit, critical_limit)
    recommendation_lines = recommendations if recommendations else ["Sin acciones recomendadas."]

    return "\n".join(
        [
            "Reporte del Monitor de Sistema",
            "=" * 30,
            f"Fecha y hora: {usage.timestamp:%Y-%m-%d %H:%M:%S}",
            f"Estado general: {get_overall_status(usage, warning_limit, critical_limit)}",
            f"Limites: advertencia >= {warning_limit:.0f}% | critico >= {critical_limit:.0f}%",
            "",
            "Informacion del sistema",
            f"Sistema operativo: {details.operating_system}",
            f"Version: {details.version}",
            f"Equipo: {details.computer_name}",
            "",
            "Uso de recursos",
            *[
                f"{diagnostic.name}: {diagnostic.percent:.1f}% - {diagnostic.status}"
                for diagnostic in get_resource_diagnostics(
                    usage,
                    warning_limit,
                    critical_limit,
                )
            ],
            "",
            "Alertas",
            *alert_lines,
            "",
            "Recomendaciones",
            *recommendation_lines,
            "",
        ]
    )


def save_report(
    details: SystemDetails,
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> Path:
    """Create a TXT report inside the reports directory."""
    REPORTS_DIR.mkdir(exist_ok=True)
    filename = f"system_report_{usage.timestamp:%Y%m%d_%H%M%S}.txt"
    report_path = REPORTS_DIR / filename
    report_path.write_text(
        build_report_content(details, usage, warning_limit, critical_limit),
        encoding="utf-8",
    )
    return report_path
