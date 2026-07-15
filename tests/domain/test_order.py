from sample_order_system.domain.order import Order, OrderStatus


def test_new_order_has_reserved_status():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )

    assert order.status == OrderStatus.RESERVED


def test_reject_transitions_reserved_order_to_rejected():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )

    order.reject()

    assert order.status == OrderStatus.REJECTED


def test_approve_confirms_order_when_stock_is_sufficient():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )

    order.approve(available_stock=10)

    assert order.status == OrderStatus.CONFIRMED
