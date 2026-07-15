from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_service import (
    approve_order,
    complete_order_production,
    release_order,
)
from sample_order_system.domain.sample import Sample, SampleRegistry


def test_approve_order_uses_actual_stock_from_registry():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=5,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)

    approve_order(order, registry)

    assert order.status == OrderStatus.PRODUCING


def test_release_order_decreases_stock_by_order_quantity():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=50,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)

    release_order(order, registry)

    assert order.status == OrderStatus.RELEASED
    assert registry.find_by_id("S-001").stock == 40


def test_complete_order_production_increases_stock_by_actual_production_quantity():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=3,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)

    complete_order_production(order, registry)

    assert order.status == OrderStatus.CONFIRMED
    # shortage = 10 - 3 = 7, production_quantity = ceil(7 / 0.9) = 8
    assert registry.find_by_id("S-001").stock == 11
