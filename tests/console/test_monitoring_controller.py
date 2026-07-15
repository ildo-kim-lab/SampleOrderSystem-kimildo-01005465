from sample_order_system.console.monitoring_controller import monitor_order_counts
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry


def test_monitor_order_counts_excludes_rejected():
    order_registry = OrderRegistry()
    reserved = Order(sample_id="S-001", customer_name="A", quantity=1)
    confirmed = Order(sample_id="S-001", customer_name="B", quantity=1)
    confirmed.status = OrderStatus.CONFIRMED
    rejected = Order(sample_id="S-001", customer_name="C", quantity=1)
    rejected.status = OrderStatus.REJECTED
    for order in (reserved, confirmed, rejected):
        order_registry.register(order)
    outputs = []

    monitor_order_counts(order_registry, output_func=outputs.append)

    combined_output = "\n".join(outputs)
    assert "RESERVED: 1" in combined_output
    assert "CONFIRMED: 1" in combined_output
    assert "REJECTED" not in combined_output
