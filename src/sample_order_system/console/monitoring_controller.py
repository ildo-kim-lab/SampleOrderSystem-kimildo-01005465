from collections import Counter
from typing import Callable

from sample_order_system.domain.order import OrderStatus, TERMINAL_STATUSES
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.sample import SampleRegistry
from sample_order_system.domain.stock_status import determine_stock_status

_MONITORED_STATUSES = (
    OrderStatus.RESERVED,
    OrderStatus.CONFIRMED,
    OrderStatus.PRODUCING,
    OrderStatus.RELEASED,
)


def monitor_order_counts(
    order_registry: OrderRegistry,
    output_func: Callable[[str], None],
) -> None:
    counts = Counter(order.status for order in order_registry.get_all())
    for status in _MONITORED_STATUSES:
        output_func(f"{status.value}: {counts[status]}")


def monitor_stock_levels(
    sample_registry: SampleRegistry,
    order_registry: OrderRegistry,
    output_func: Callable[[str], None],
) -> None:
    orders = order_registry.get_all()
    for sample in sample_registry.get_all():
        demand = sum(
            order.quantity
            for order in orders
            if order.sample_id == sample.sample_id
            and order.status not in TERMINAL_STATUSES
        )
        status = determine_stock_status(sample.stock, demand)
        output_func(f"{sample.name} | 재고: {sample.stock} | {status}")
