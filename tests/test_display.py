from src.display import build_alerts, format_bytes, render_snapshot
from src.metrics import SystemMetrics


def sample_metrics(**overrides):
    values = {
        "timestamp": "2026-05-31T16:00:00",
        "cpu_percent": 50.0,
        "memory_percent": 60.0,
        "disk_percent": 70.0,
        "bytes_sent": 2048,
        "bytes_recv": 5_242_880,
    }
    values.update(overrides)
    return SystemMetrics(**values)


def test_format_bytes_uses_readable_units():
    assert format_bytes(512) == "512.0 B"
    assert format_bytes(2048) == "2.0 KB"
    assert format_bytes(5_242_880) == "5.0 MB"


def test_build_alerts_returns_values_over_threshold():
    metrics = sample_metrics(cpu_percent=90.0, memory_percent=79.9, disk_percent=80.0)

    assert build_alerts(metrics, threshold=80) == [
        "CPU alto: 90.0%",
        "Disco alto: 80.0%",
    ]


def test_render_snapshot_includes_metrics_and_alert_state():
    output = render_snapshot(sample_metrics(), threshold=95)

    assert "Monitor de Sistema" in output
    assert "CPU:" in output
    assert "Sin alertas" in output
