from sample_order_system.console.production_controller import (
    complete_production_console,
    list_waiting_orders,
    show_production_status,
)
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.production_line_status import ProductionLine
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import Sample, SampleRegistry


def test_complete_production_console_confirms_and_increases_stock():
    sample_registry = SampleRegistry()
    sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=3,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    outputs = []

    complete_production_console(order, sample_registry, output_func=outputs.append)

    assert order.status == OrderStatus.CONFIRMED
    # shortage = 10 - 3 = 7, production_quantity = ceil(7 / 0.9) = 8
    assert sample_registry.find_by_id("S-001").stock == 11
    assert any("CONFIRMED" in message for message in outputs)


def test_list_waiting_orders_outputs_orders_in_fifo_order():
    queue = ProductionQueue()
    first_order = Order(sample_id="S-001", customer_name="A", quantity=3)
    second_order = Order(sample_id="S-002", customer_name="B", quantity=5)
    queue.enqueue(first_order)
    queue.enqueue(second_order)
    outputs = []

    list_waiting_orders(queue, output_func=outputs.append)

    assert outputs == [
        "S-001 | A | 수량: 3",
        "S-002 | B | 수량: 5",
    ]


def test_show_production_status_reports_current_order_progress():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    line = ProductionLine(current_order=order, produced_quantity=4)
    outputs = []

    show_production_status(line, output_func=outputs.append)

    assert outputs == ["S-001 | ACME Corp | 생산량: 4"]


def test_show_production_status_reports_no_order_when_idle():
    line = ProductionLine()
    outputs = []

    show_production_status(line, output_func=outputs.append)

    assert outputs == ["생산 중인 주문 없음"]
