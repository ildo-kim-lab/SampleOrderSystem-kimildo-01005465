from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.sample import Sample, SampleRegistry

_DUMMY_SAMPLES = [
    Sample(
        sample_id="S-001",
        name="Wafer-A",
        avg_production_time=2.5,
        yield_rate=0.9,
        stock=100,
    ),
    Sample(
        sample_id="S-002",
        name="Wafer-B",
        avg_production_time=1.5,
        yield_rate=0.85,
        stock=5,
    ),
    Sample(
        sample_id="S-003",
        name="Wafer-C",
        avg_production_time=3.0,
        yield_rate=0.95,
        stock=0,
    ),
]


def generate_dummy_samples(sample_registry: SampleRegistry) -> None:
    for sample in _DUMMY_SAMPLES:
        sample_registry.register(sample)


def generate_dummy_orders(order_registry: OrderRegistry) -> None:
    reserved = Order(sample_id="S-001", customer_name="Customer A", quantity=5)

    rejected = Order(sample_id="S-001", customer_name="Customer B", quantity=3)
    rejected.status = OrderStatus.REJECTED

    producing = Order(sample_id="S-002", customer_name="Customer C", quantity=20)
    producing.status = OrderStatus.PRODUCING

    confirmed = Order(sample_id="S-001", customer_name="Customer D", quantity=10)
    confirmed.status = OrderStatus.CONFIRMED

    released = Order(sample_id="S-001", customer_name="Customer E", quantity=8)
    released.status = OrderStatus.RELEASED

    for order in (reserved, rejected, producing, confirmed, released):
        order_registry.register(order)
