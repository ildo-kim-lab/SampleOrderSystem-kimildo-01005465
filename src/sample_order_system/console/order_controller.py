from typing import Callable

from sample_order_system.console.selection import select_from_list
from sample_order_system.console.view import format_sample_line
from sample_order_system.domain.order import Order
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.order_service import approve_order
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import SampleRegistry


def create_order(
    order_registry: OrderRegistry,
    sample_registry: SampleRegistry,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    samples = sample_registry.get_all()
    selected_sample = select_from_list(
        samples,
        format_sample_line,
        input_func,
        output_func,
        "시료 번호: ",
        "등록된 시료가 없습니다",
    )
    if selected_sample is None:
        return

    try:
        quantity = int(input_func("주문 수량: "))
    except ValueError:
        output_func("숫자 형식이 올바르지 않습니다")
        return

    customer_name = input_func("고객명: ")

    order = Order(
        sample_id=selected_sample.sample_id,
        customer_name=customer_name,
        quantity=quantity,
    )
    order_registry.register(order)
    output_func(
        f"주문 접수 완료 ({customer_name}, {selected_sample.sample_id} x {quantity})"
    )


def approve_order_console(
    order: Order,
    sample_registry: SampleRegistry,
    production_queue: ProductionQueue,
    output_func: Callable[[str], None],
) -> None:
    approve_order(order, sample_registry, production_queue)
    output_func(f"주문 승인 처리됨 -> {order.status.value}")


def reject_order_console(
    order: Order,
    output_func: Callable[[str], None],
) -> None:
    order.reject()
    output_func(f"주문 거절 처리됨 -> {order.status.value}")
