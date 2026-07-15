import json
from dataclasses import asdict
from pathlib import Path
from typing import Callable, Iterable, TypeVar

from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import Sample, SampleRegistry

T = TypeVar("T")


def _order_to_dict(order: Order) -> dict:
    return {
        "sample_id": order.sample_id,
        "customer_name": order.customer_name,
        "quantity": order.quantity,
        "status": order.status.value,
    }


def _dict_to_order(entry: dict) -> Order:
    return Order(
        sample_id=entry["sample_id"],
        customer_name=entry["customer_name"],
        quantity=entry["quantity"],
        status=OrderStatus(entry["status"]),
    )


def save_json_list(
    items: Iterable[T], to_dict: Callable[[T], dict], filepath: Path
) -> None:
    data = [to_dict(item) for item in items]
    filepath.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def load_json_list(filepath: Path, from_dict: Callable[[dict], T]) -> list[T]:
    data = json.loads(filepath.read_text(encoding="utf-8"))
    return [from_dict(entry) for entry in data]


def save_samples(sample_registry: SampleRegistry, filepath: Path) -> None:
    save_json_list(sample_registry.get_all(), asdict, filepath)


def load_samples(filepath: Path) -> SampleRegistry:
    registry = SampleRegistry()
    for sample in load_json_list(filepath, lambda entry: Sample(**entry)):
        registry.register(sample)
    return registry


def save_orders(order_registry: OrderRegistry, filepath: Path) -> None:
    save_json_list(order_registry.get_all(), _order_to_dict, filepath)


def load_orders(filepath: Path) -> OrderRegistry:
    registry = OrderRegistry()
    for order in load_json_list(filepath, _dict_to_order):
        registry.register(order)
    return registry


def save_production_queue(queue: ProductionQueue, filepath: Path) -> None:
    save_json_list(queue.list_all(), _order_to_dict, filepath)


def load_production_queue(filepath: Path) -> ProductionQueue:
    queue = ProductionQueue()
    for order in load_json_list(filepath, _dict_to_order):
        queue.enqueue(order)
    return queue
