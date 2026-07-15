from collections import Counter
from typing import Callable

from sample_order_system.domain.order import OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry

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
