from __future__ import annotations

from datetime import datetime
import platform

import psutil

from src.models import ResourceUsage, SystemDetails


def get_system_details() -> SystemDetails:
    """Return basic information about the current Windows system."""
    return SystemDetails(
        operating_system=platform.system(),
        version=platform.version(),
        computer_name=platform.node(),
    )


def get_resource_usage() -> ResourceUsage:
    """Collect current CPU, RAM and disk usage using psutil."""
    return ResourceUsage(
        timestamp=datetime.now(),
        cpu_percent=psutil.cpu_percent(interval=1),
        ram_percent=psutil.virtual_memory().percent,
        disk_percent=psutil.disk_usage("/").percent,
    )
