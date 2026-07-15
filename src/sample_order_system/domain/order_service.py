from sample_order_system.domain.order import Order
from sample_order_system.domain.sample import SampleRegistry


def approve_order(order: Order, registry: SampleRegistry) -> None:
    sample = registry.find_by_id(order.sample_id)
    order.approve(available_stock=sample.stock)
