from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime

import psutil


@dataclass(frozen=True)
class SystemMetrics:
    timestamp: str
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    bytes_sent: int
    bytes_recv: int

    def to_dict(self) -> dict[str, str | float | int]:
        return asdict(self)


def collect_metrics() -> SystemMetrics:
    disk = psutil.disk_usage("/")
    network = psutil.net_io_counters()

    return SystemMetrics(
        timestamp=datetime.now().isoformat(timespec="seconds"),
        cpu_percent=psutil.cpu_percent(interval=None),
        memory_percent=psutil.virtual_memory().percent,
        disk_percent=disk.percent,
        bytes_sent=network.bytes_sent,
        bytes_recv=network.bytes_recv,
    )
