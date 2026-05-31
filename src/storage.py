from __future__ import annotations

import csv
from pathlib import Path

from src.metrics import SystemMetrics


CSV_FIELDS = [
    "timestamp",
    "cpu_percent",
    "memory_percent",
    "disk_percent",
    "bytes_sent",
    "bytes_recv",
]


def append_metrics_csv(path: str | Path, metrics: SystemMetrics) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    should_write_header = not target.exists()

    with target.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        if should_write_header:
            writer.writeheader()
        writer.writerow(metrics.to_dict())
