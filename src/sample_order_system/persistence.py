import json
from dataclasses import asdict
from pathlib import Path

from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import Sample, SampleRegistry


def _order_to_dict(order: Order) -> dict:
    return {
        "sample_id": order.sample_id,
        "customer_name": order.customer_name,
        "quantity": order.quantity,
        "status": order.status.value,
    }


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
    data = [_order_to_dict(order) for order in order_registry.get_all()]
    filepath.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def _dict_to_order(entry: dict) -> Order:
    order = Order(
        sample_id=entry["sample_id"],
        customer_name=entry["customer_name"],
        quantity=entry["quantity"],
    )
    order.status = OrderStatus(entry["status"])
    return order


def load_orders(filepath: Path) -> OrderRegistry:
    registry = OrderRegistry()
    data = json.loads(filepath.read_text(encoding="utf-8"))
    for entry in data:
        registry.register(_dict_to_order(entry))
    return registry


def save_production_queue(queue: ProductionQueue, filepath: Path) -> None:
    data = [_order_to_dict(order) for order in queue.list_all()]
    filepath.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def load_production_queue(filepath: Path) -> ProductionQueue:
    queue = ProductionQueue()
    data = json.loads(filepath.read_text(encoding="utf-8"))
    for entry in data:
        queue.enqueue(_dict_to_order(entry))
    return queue
