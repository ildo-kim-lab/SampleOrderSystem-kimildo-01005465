import json
from dataclasses import asdict
from pathlib import Path

from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.sample import Sample, SampleRegistry


def save_samples(sample_registry: SampleRegistry, filepath: Path) -> None:
    data = [asdict(sample) for sample in sample_registry.get_all()]
    filepath.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def load_samples(filepath: Path) -> SampleRegistry:
    registry = SampleRegistry()
    data = json.loads(filepath.read_text(encoding="utf-8"))
    for entry in data:
        registry.register(Sample(**entry))
    return registry


def save_orders(order_registry: OrderRegistry, filepath: Path) -> None:
    data = [
        {
            "sample_id": order.sample_id,
            "customer_name": order.customer_name,
            "quantity": order.quantity,
            "status": order.status.value,
        }
        for order in order_registry.get_all()
    ]
    filepath.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
