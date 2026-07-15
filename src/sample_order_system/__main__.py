from pathlib import Path

from sample_order_system.console.app import start_app


def main() -> None:
    start_app(Path("samples.json"), Path("orders.json"), input, print)


if __name__ == "__main__":
    main()
