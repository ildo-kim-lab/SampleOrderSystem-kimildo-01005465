from sample_order_system.console.order_controller import (
    approve_order_console,
    create_order,
)
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.sample import Sample, SampleRegistry


def test_create_order_adds_reserved_order_with_entered_values():
    order_registry = OrderRegistry()
    inputs = iter(["S-001", "ACME Corp", "10"])
    outputs = []

    create_order(
        order_registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    orders = order_registry.get_all()
    assert len(orders) == 1
    assert orders[0].sample_id == "S-001"
    assert orders[0].customer_name == "ACME Corp"
    assert orders[0].quantity == 10
    assert orders[0].status == OrderStatus.RESERVED


def test_approve_order_console_confirms_when_stock_is_sufficient():
    sample_registry = SampleRegistry()
    sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    outputs = []

    approve_order_console(order, sample_registry, output_func=outputs.append)

    assert order.status == OrderStatus.CONFIRMED
    assert any("CONFIRMED" in message for message in outputs)
