import pytest

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


def test_approve_starts_production_when_stock_is_insufficient():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )

    order.approve(available_stock=9)

    assert order.status == OrderStatus.PRODUCING


def test_release_transitions_confirmed_order_to_released():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )
    order.approve(available_stock=10)

    order.release()

    assert order.status == OrderStatus.RELEASED


def test_complete_production_transitions_producing_order_to_confirmed():
    order = Order(
        sample_id="S-001",
        customer_name="ACME Corp",
        quantity=10,
    )
    order.approve(available_stock=9)

    order.complete_production()

    assert order.status == OrderStatus.CONFIRMED


def test_reject_raises_when_order_already_rejected():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.reject()

    with pytest.raises(ValueError):
        order.reject()


def test_reject_raises_when_order_already_released():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.approve(available_stock=10)
    order.release()

    with pytest.raises(ValueError):
        order.reject()


def test_approve_raises_when_order_already_rejected():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.reject()

    with pytest.raises(ValueError):
        order.approve(available_stock=10)


def test_release_raises_when_order_already_rejected():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.reject()

    with pytest.raises(ValueError):
        order.release()


def test_complete_production_raises_when_order_already_rejected():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.reject()

    with pytest.raises(ValueError):
        order.complete_production()


def test_approve_raises_when_order_already_producing():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.approve(available_stock=0)

    with pytest.raises(ValueError):
        order.approve(available_stock=10)


def test_release_raises_when_order_still_reserved():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)

    with pytest.raises(ValueError):
        order.release()
