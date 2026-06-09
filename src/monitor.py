from __future__ import annotations

import argparse
from collections.abc import Sequence

from src.diagnostics import (
    CRITICAL_LIMIT,
    WARNING_LIMIT,
    get_alerts,
    get_overall_status,
    get_recommendations,
    get_resource_diagnostics,
)
from src.models import ResourceUsage, SystemDetails
from src.reports import save_report


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line options for menu and quick diagnostic modes."""
    parser = argparse.ArgumentParser(
        description="Monitor de sistema para diagnostico basico de recursos."
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Muestra un diagnostico una sola vez y termina.",
    )
    parser.add_argument(
        "--warning",
        type=float,
        default=WARNING_LIMIT,
        help=f"Porcentaje para estado ADVERTENCIA. Default: {WARNING_LIMIT:.0f}.",
    )
    parser.add_argument(
        "--critical",
        type=float,
        default=CRITICAL_LIMIT,
        help=f"Porcentaje para estado CRITICO. Default: {CRITICAL_LIMIT:.0f}.",
    )
    return parser.parse_args(argv)


def validate_limits(warning_limit: float, critical_limit: float) -> None:
    """Validate warning and critical thresholds."""
    if not 0 <= warning_limit <= 100:
        raise ValueError("El limite de advertencia debe estar entre 0 y 100.")
    if not 0 <= critical_limit <= 100:
        raise ValueError("El limite critico debe estar entre 0 y 100.")
    if warning_limit >= critical_limit:
        raise ValueError("El limite de advertencia debe ser menor que el critico.")


def display_system_status(
    details: SystemDetails,
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> None:
    """Print system information, resource usage and basic alerts."""
    print("\nMonitor de Sistema")
    print("=" * 19)
    print(f"Estado general: {get_overall_status(usage, warning_limit, critical_limit)}")
    print(
        f"Limites usados: advertencia >= {warning_limit:.0f}% | "
        f"critico >= {critical_limit:.0f}%"
    )
    print(f"Sistema operativo: {details.operating_system}")
    print(f"Version: {details.version}")
    print(f"Equipo: {details.computer_name}")
    print("\nUso de recursos")
    for diagnostic in get_resource_diagnostics(usage, warning_limit, critical_limit):
        print(f"{diagnostic.name}: {diagnostic.percent:.1f}% - {diagnostic.status}")

    alerts = get_alerts(usage, warning_limit, critical_limit)
    print("\nAlertas")
    if alerts:
        for alert in alerts:
            print(f"- {alert}")
    else:
        print("- Sin alertas.")


def display_recommendations(
    usage: ResourceUsage,
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> None:
    """Print practical recommendations based on current resource usage."""
    recommendations = get_recommendations(usage, warning_limit, critical_limit)

    print("\nRecomendaciones")
    if recommendations:
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("- Sin acciones recomendadas.")


def show_menu() -> None:
    """Print the main console menu."""
    print("\nMenu")
    print("1. Ver estado del sistema")
    print("2. Generar reporte")
    print("3. Ver recomendaciones")
    print("4. Salir")


def get_current_system_data() -> tuple[SystemDetails, ResourceUsage]:
    """Collect current system details and resource usage."""
    from src.system_info import get_resource_usage, get_system_details

    return get_system_details(), get_resource_usage()


def run_menu(
    warning_limit: float = WARNING_LIMIT,
    critical_limit: float = CRITICAL_LIMIT,
) -> None:
    """Run the console menu until the user chooses to exit."""
    while True:
        show_menu()
        option = input("Seleccione una opcion: ").strip()

        if option == "1":
            details, usage = get_current_system_data()
            display_system_status(
                details,
                usage,
                warning_limit,
                critical_limit,
            )
        elif option == "2":
            details, usage = get_current_system_data()
            report_path = save_report(details, usage, warning_limit, critical_limit)
            print(f"\nReporte generado: {report_path}")
        elif option == "3":
            _, usage = get_current_system_data()
            display_recommendations(usage, warning_limit, critical_limit)
        elif option == "4":
            print("\nSaliendo del monitor. Hasta luego.")
            break
        else:
            print("\nOpcion no valida. Intente de nuevo.")


def main(argv: Sequence[str] | None = None) -> None:
    """Application entry point."""
    args = parse_args(argv)
    validate_limits(args.warning, args.critical)

    if args.once:
        details, usage = get_current_system_data()
        display_system_status(
            details,
            usage,
            args.warning,
            args.critical,
        )
        return

    run_menu(args.warning, args.critical)


if __name__ == "__main__":
    main()
