from sample_order_system.console.monitoring_controller import (
    monitor_order_counts,
    monitor_stock_levels,
)
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.sample import Sample, SampleRegistry


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


def test_monitor_stock_levels_reports_status_based_on_active_order_demand():
    sample_registry = SampleRegistry()
    sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=5,
        )
    )
    order_registry = OrderRegistry()
    reserved = Order(sample_id="S-001", customer_name="A", quantity=3)
    confirmed = Order(sample_id="S-001", customer_name="B", quantity=4)
    confirmed.status = OrderStatus.CONFIRMED
    released = Order(sample_id="S-001", customer_name="C", quantity=2)
    released.status = OrderStatus.RELEASED
    for order in (reserved, confirmed, released):
        order_registry.register(order)
    outputs = []

    monitor_stock_levels(sample_registry, order_registry, output_func=outputs.append)

    combined_output = "\n".join(outputs)
    assert "Wafer-A" in combined_output
    # demand = 3 + 4 = 7 (released excluded), stock = 5 -> 부족
    assert "부족" in combined_output
