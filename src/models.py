from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SystemDetails:
    """Basic operating system and host information."""

    operating_system: str
    version: str
    computer_name: str


@dataclass(frozen=True)
class ResourceUsage:
    """Current CPU, RAM and disk usage percentages."""

    timestamp: datetime
    cpu_percent: float
    ram_percent: float
    disk_percent: float
