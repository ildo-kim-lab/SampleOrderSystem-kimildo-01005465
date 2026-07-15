from typing import Callable

from sample_order_system.console.view import format_order_line
from sample_order_system.domain.order import Order
from sample_order_system.domain.order_service import complete_order_production
from sample_order_system.domain.production_line_status import ProductionLine
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import SampleRegistry


def complete_production_console(
    order: Order,
    sample_registry: SampleRegistry,
    output_func: Callable[[str], None],
) -> None:
    complete_order_production(order, sample_registry)
    output_func(f"생산 완료 처리됨 -> {order.status.value}")


def list_waiting_orders(
    queue: ProductionQueue,
    output_func: Callable[[str], None],
) -> None:
    for order in queue.list_all():
        output_func(format_order_line(order))


def show_production_status(
    line: ProductionLine,
    output_func: Callable[[str], None],
) -> None:
    order = line.current_order
    if order is None:
        output_func("생산 중인 주문 없음")
        return
    output_func(
        f"{order.sample_id} | {order.customer_name} | 생산량: {line.produced_quantity}"
    )


def complete_next_production_console(
    queue: ProductionQueue,
    sample_registry: SampleRegistry,
    output_func: Callable[[str], None],
) -> None:
    if not queue.list_all():
        output_func("대기 중인 생산이 없습니다")
        return
    order = queue.dequeue()
    complete_order_production(order, sample_registry)
    output_func(f"생산 완료 처리됨 -> {order.status.value} ({format_order_line(order)})")
