from sample_order_system.domain.order import Order
from sample_order_system.domain.production_line_status import ProductionLine


def test_production_line_reports_current_order_and_produced_quantity():
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    line = ProductionLine(current_order=order, produced_quantity=4)

    assert line.current_order is order
    assert line.produced_quantity == 4
