from sample_order_system.domain.order import Order
from sample_order_system.domain.production_queue import ProductionQueue


def test_dequeue_returns_orders_in_fifo_order():
    queue = ProductionQueue()
    first_order = Order(sample_id="S-001", customer_name="A", quantity=1)
    second_order = Order(sample_id="S-002", customer_name="B", quantity=1)
    queue.enqueue(first_order)
    queue.enqueue(second_order)

    assert queue.dequeue() is first_order
    assert queue.dequeue() is second_order
