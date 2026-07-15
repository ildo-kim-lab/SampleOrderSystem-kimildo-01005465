from sample_order_system.console.order_controller import create_order
from sample_order_system.domain.order import OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry


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
