from sample_order_system.console.production_controller import (
    complete_production_console,
)
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.sample import Sample, SampleRegistry


def test_complete_production_console_confirms_and_increases_stock():
    sample_registry = SampleRegistry()
    sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=3,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    outputs = []

    complete_production_console(order, sample_registry, output_func=outputs.append)

    assert order.status == OrderStatus.CONFIRMED
    # shortage = 10 - 3 = 7, production_quantity = ceil(7 / 0.9) = 8
    assert sample_registry.find_by_id("S-001").stock == 11
    assert any("CONFIRMED" in message for message in outputs)
