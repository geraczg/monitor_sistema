from datetime import datetime
import unittest

from src.models import ResourceUsage, SystemDetails
from src.reports import build_report_content


class ReportTests(unittest.TestCase):
    def test_report_includes_status_alerts_and_recommendations(self) -> None:
        details = SystemDetails(
            operating_system="Windows",
            version="10.0.26200",
            computer_name="LAPTOP-TEST",
        )
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 30, 0),
            cpu_percent=35.0,
            ram_percent=88.0,
            disk_percent=92.0,
        )

        content = build_report_content(details, usage)

        self.assertIn("Estado general: CRITICO", content)
        self.assertIn("Limites: advertencia >= 80% | critico >= 90%", content)
        self.assertIn("RAM: 88.0% - ADVERTENCIA", content)
        self.assertIn("Disco: 92.0% - CRITICO", content)
        self.assertIn("ADVERTENCIA: RAM alta", content)
        self.assertIn("CRITICO: Disco con uso alto", content)
        self.assertIn("Recomendaciones", content)

    def test_report_uses_clean_message_when_system_is_ok(self) -> None:
        details = SystemDetails(
            operating_system="Windows",
            version="10.0.26200",
            computer_name="LAPTOP-TEST",
        )
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 30, 0),
            cpu_percent=20.0,
            ram_percent=30.0,
            disk_percent=40.0,
        )

        content = build_report_content(details, usage)

        self.assertIn("Estado general: OK", content)
        self.assertIn("Sin alertas.", content)
        self.assertIn("Sin acciones recomendadas.", content)

    def test_report_uses_custom_limits(self) -> None:
        details = SystemDetails(
            operating_system="Windows",
            version="10.0.26200",
            computer_name="LAPTOP-TEST",
        )
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 30, 0),
            cpu_percent=76.0,
            ram_percent=30.0,
            disk_percent=40.0,
        )

        content = build_report_content(
            details,
            usage,
            warning_limit=75.0,
            critical_limit=90.0,
        )

        self.assertIn("Limites: advertencia >= 75% | critico >= 90%", content)
        self.assertIn("CPU: 76.0% - ADVERTENCIA", content)


if __name__ == "__main__":
    unittest.main()
