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
    orders = [
        Order(sample_id="S-001", customer_name="Customer A", quantity=5),
        Order(
            sample_id="S-001",
            customer_name="Customer B",
            quantity=3,
            status=OrderStatus.REJECTED,
        ),
        Order(
            sample_id="S-002",
            customer_name="Customer C",
            quantity=20,
            status=OrderStatus.PRODUCING,
        ),
        Order(
            sample_id="S-001",
            customer_name="Customer D",
            quantity=10,
            status=OrderStatus.CONFIRMED,
        ),
        Order(
            sample_id="S-001",
            customer_name="Customer E",
            quantity=8,
            status=OrderStatus.RELEASED,
        ),
    ]
    for order in orders:
        order_registry.register(order)
