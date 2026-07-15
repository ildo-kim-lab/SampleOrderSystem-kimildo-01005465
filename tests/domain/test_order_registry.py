from sample_order_system.domain.order import Order
from sample_order_system.domain.order_registry import OrderRegistry


def test_registered_order_appears_in_get_all():
    registry = OrderRegistry()
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)

    registry.register(order)

    assert order in registry.get_all()
