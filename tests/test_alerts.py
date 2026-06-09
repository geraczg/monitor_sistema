from datetime import datetime
import unittest

from src.alerts import get_alerts
from src.diagnostics import classify_percent, get_overall_status, get_recommendations
from src.models import ResourceUsage


class AlertTests(unittest.TestCase):
    def test_returns_alerts_when_limits_are_exceeded(self) -> None:
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 0, 0),
            cpu_percent=85.0,
            ram_percent=90.0,
            disk_percent=95.0,
        )

        alerts = get_alerts(usage)

        self.assertEqual(len(alerts), 3)
        self.assertIn("CPU alta", alerts[0])
        self.assertIn("RAM alta", alerts[1])
        self.assertIn("Disco", alerts[2])

    def test_returns_no_alerts_when_usage_is_normal(self) -> None:
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 0, 0),
            cpu_percent=20.0,
            ram_percent=40.0,
            disk_percent=60.0,
        )

        self.assertEqual(get_alerts(usage), [])

    def test_classifies_percent_by_status(self) -> None:
        self.assertEqual(classify_percent(30.0), "OK")
        self.assertEqual(classify_percent(80.0), "ADVERTENCIA")
        self.assertEqual(classify_percent(90.0), "CRITICO")

    def test_classifies_percent_with_custom_limits(self) -> None:
        self.assertEqual(
            classify_percent(76.0, warning_limit=75.0, critical_limit=90.0),
            "ADVERTENCIA",
        )

    def test_returns_overall_status_from_highest_resource_status(self) -> None:
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 0, 0),
            cpu_percent=20.0,
            ram_percent=82.0,
            disk_percent=91.0,
        )

        self.assertEqual(get_overall_status(usage), "CRITICO")

    def test_returns_recommendations_for_alerted_resources(self) -> None:
        usage = ResourceUsage(
            timestamp=datetime(2026, 6, 5, 12, 0, 0),
            cpu_percent=20.0,
            ram_percent=85.0,
            disk_percent=40.0,
        )

        recommendations = get_recommendations(usage)

        self.assertEqual(len(recommendations), 1)
        self.assertIn("RAM", recommendations[0])


if __name__ == "__main__":
    unittest.main()
