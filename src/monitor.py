from __future__ import annotations

import argparse
import os
import time
from collections.abc import Sequence

from src.display import render_snapshot
from src.metrics import collect_metrics
from src.storage import append_metrics_csv


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Monitor de sistema en consola con exportacion opcional a CSV."
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Segundos entre lecturas. Default: 1.0",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=80.0,
        help="Porcentaje desde el cual se muestran alertas. Default: 80",
    )
    parser.add_argument(
        "--csv",
        help="Ruta opcional para guardar las lecturas en CSV.",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Toma una sola lectura y termina.",
    )
    return parser.parse_args(argv)


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def run_monitor(args: argparse.Namespace) -> None:
    while True:
        metrics = collect_metrics()

        clear_screen()
        print(render_snapshot(metrics, args.threshold))

        if args.csv:
            append_metrics_csv(args.csv, metrics)

        if args.once:
            break

        time.sleep(max(args.interval, 0.2))


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    run_monitor(args)


if __name__ == "__main__":
    main()
