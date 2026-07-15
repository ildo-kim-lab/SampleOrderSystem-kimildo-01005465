from sample_order_system.domain.order import Order
from sample_order_system.domain.production_line import calculate_production_quantity
from sample_order_system.domain.sample import SampleRegistry


def approve_order(order: Order, registry: SampleRegistry) -> None:
    sample = registry.find_by_id(order.sample_id)
    order.approve(available_stock=sample.stock)


def release_order(order: Order, registry: SampleRegistry) -> None:
    sample = registry.find_by_id(order.sample_id)
    order.release()
    sample.decrease_stock(order.quantity)


def complete_order_production(order: Order, registry: SampleRegistry) -> None:
    sample = registry.find_by_id(order.sample_id)
    shortage = order.quantity - sample.stock
    production_quantity = calculate_production_quantity(shortage, sample.yield_rate)
    order.complete_production()
    sample.increase_stock(production_quantity)
