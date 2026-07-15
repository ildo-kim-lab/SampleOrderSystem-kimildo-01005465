from sample_order_system.console.release_controller import release_order_console
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.sample import Sample, SampleRegistry


def test_release_order_console_releases_and_decreases_stock():
    sample_registry = SampleRegistry()
    sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=50,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.status = OrderStatus.CONFIRMED
    outputs = []

    release_order_console(order, sample_registry, output_func=outputs.append)

    assert order.status == OrderStatus.RELEASED
    assert sample_registry.find_by_id("S-001").stock == 40
    assert any("RELEASED" in message for message in outputs)
