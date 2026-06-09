from __future__ import annotations

from dataclasses import dataclass

from src.models import ResourceUsage

WARNING_LIMIT = 80.0
CRITICAL_LIMIT = 90.0


@dataclass(frozen=True)
class ResourceDiagnostic:
    """Diagnostic result for one monitored resource."""

    name: str
    percent: float
    status: str
    message: str
    recommendation: str


def classify_percent(
    percent: float,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> str:
    """Return a readable health status for a usage percentage."""
    if percent >= critical_limit:
        return "CRITICO"
    if percent >= warning_limit:
        return "ADVERTENCIA"
    return "OK"


def get_resource_diagnostics(
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> list[ResourceDiagnostic]:
    """Build diagnostics for CPU, RAM and disk usage."""
    diagnostics = [
        ResourceDiagnostic(
            name="CPU",
            percent=usage.cpu_percent,
            status=classify_percent(usage.cpu_percent, warning_limit, critical_limit),
            message=f"CPU alta ({usage.cpu_percent:.1f}%).",
            recommendation="Revisar procesos con alto consumo y cerrar tareas no necesarias.",
        ),
        ResourceDiagnostic(
            name="RAM",
            percent=usage.ram_percent,
            status=classify_percent(usage.ram_percent, warning_limit, critical_limit),
            message=f"RAM alta ({usage.ram_percent:.1f}%).",
            recommendation="Cerrar aplicaciones pesadas o reiniciar si el consumo no baja.",
        ),
        ResourceDiagnostic(
            name="Disco",
            percent=usage.disk_percent,
            status=classify_percent(usage.disk_percent, warning_limit, critical_limit),
            message=f"Disco con uso alto ({usage.disk_percent:.1f}%).",
            recommendation="Liberar espacio, vaciar temporales y revisar archivos grandes.",
        ),
    ]

    return diagnostics


def get_alerts(
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> list[str]:
    """Return warning messages for resources that need attention."""
    return [
        f"{diagnostic.status}: {diagnostic.message}"
        for diagnostic in get_resource_diagnostics(usage, warning_limit, critical_limit)
        if diagnostic.status != "OK"
    ]


def get_recommendations(
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> list[str]:
    """Return practical recommendations for resources above the warning limit."""
    return [
        f"{diagnostic.name}: {diagnostic.recommendation}"
        for diagnostic in get_resource_diagnostics(usage, warning_limit, critical_limit)
        if diagnostic.status != "OK"
    ]


def get_overall_status(
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> str:
    """Return the highest system status based on all monitored resources."""
    statuses = {
        diagnostic.status
        for diagnostic in get_resource_diagnostics(usage, warning_limit, critical_limit)
    }

    if "CRITICO" in statuses:
        return "CRITICO"
    if "ADVERTENCIA" in statuses:
        return "ADVERTENCIA"
    return "OK"
