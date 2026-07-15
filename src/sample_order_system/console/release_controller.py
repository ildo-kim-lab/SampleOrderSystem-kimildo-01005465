from typing import Callable

from sample_order_system.domain.order import Order
from sample_order_system.domain.order_service import release_order
from sample_order_system.domain.sample import SampleRegistry


def release_order_console(
    order: Order,
    sample_registry: SampleRegistry,
    output_func: Callable[[str], None],
) -> None:
    release_order(order, sample_registry)
    output_func(f"출고 처리됨 -> {order.status.value}")
