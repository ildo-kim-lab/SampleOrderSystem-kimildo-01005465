import json

from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import Sample, SampleRegistry
from sample_order_system.persistence import (
    load_orders,
    load_production_queue,
    load_samples,
    save_orders,
    save_production_queue,
    save_samples,
)


def test_save_samples_writes_json_file(tmp_path):
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    filepath = tmp_path / "samples.json"

    save_samples(registry, filepath)

    saved = json.loads(filepath.read_text(encoding="utf-8"))
    assert saved == [
        {
            "sample_id": "S-001",
            "name": "Wafer-A",
            "avg_production_time": 2.5,
            "yield_rate": 0.9,
            "stock": 10,
        }
    ]


def test_load_samples_restores_registry_from_json_file(tmp_path):
    original = SampleRegistry()
    original.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    filepath = tmp_path / "samples.json"
    save_samples(original, filepath)

    restored = load_samples(filepath)

    sample = restored.find_by_id("S-001")
    assert sample is not None
    assert sample.name == "Wafer-A"
    assert sample.avg_production_time == 2.5
    assert sample.yield_rate == 0.9
    assert sample.stock == 10


def test_save_orders_writes_json_file(tmp_path):
    registry = OrderRegistry()
    registry.register(
        Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    )
    filepath = tmp_path / "orders.json"

    save_orders(registry, filepath)

    saved = json.loads(filepath.read_text(encoding="utf-8"))
    assert saved == [
        {
            "sample_id": "S-001",
            "customer_name": "ACME Corp",
            "quantity": 10,
            "status": "RESERVED",
        }
    ]


def test_load_orders_restores_registry_with_status(tmp_path):
    original = OrderRegistry()
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.status = OrderStatus.CONFIRMED
    original.register(order)
    filepath = tmp_path / "orders.json"
    save_orders(original, filepath)

    restored = load_orders(filepath)

    orders = restored.get_all()
    assert len(orders) == 1
    assert orders[0].sample_id == "S-001"
    assert orders[0].customer_name == "ACME Corp"
    assert orders[0].quantity == 10
    assert orders[0].status == OrderStatus.CONFIRMED


def test_save_production_queue_writes_json_file_in_fifo_order(tmp_path):
    queue = ProductionQueue()
    first_order = Order(sample_id="S-001", customer_name="A", quantity=5)
    first_order.status = OrderStatus.PRODUCING
    second_order = Order(sample_id="S-002", customer_name="B", quantity=3)
    second_order.status = OrderStatus.PRODUCING
    queue.enqueue(first_order)
    queue.enqueue(second_order)
    filepath = tmp_path / "queue.json"

    save_production_queue(queue, filepath)

    saved = json.loads(filepath.read_text(encoding="utf-8"))
    assert saved == [
        {
            "sample_id": "S-001",
            "customer_name": "A",
            "quantity": 5,
            "status": "PRODUCING",
        },
        {
            "sample_id": "S-002",
            "customer_name": "B",
            "quantity": 3,
            "status": "PRODUCING",
        },
    ]


def test_load_production_queue_restores_orders_in_fifo_order(tmp_path):
    original = ProductionQueue()
    first_order = Order(sample_id="S-001", customer_name="A", quantity=5)
    first_order.status = OrderStatus.PRODUCING
    second_order = Order(sample_id="S-002", customer_name="B", quantity=3)
    second_order.status = OrderStatus.PRODUCING
    original.enqueue(first_order)
    original.enqueue(second_order)
    filepath = tmp_path / "queue.json"
    save_production_queue(original, filepath)

    restored = load_production_queue(filepath)

    assert restored.dequeue().sample_id == "S-001"
    assert restored.dequeue().sample_id == "S-002"
