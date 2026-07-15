from sample_order_system.domain.order import Order, OrderStatus


def test_new_order_has_reserved_status():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )

    assert order.status == OrderStatus.RESERVED
