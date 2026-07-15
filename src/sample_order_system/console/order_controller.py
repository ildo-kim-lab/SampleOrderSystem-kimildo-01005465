from typing import Callable

from sample_order_system.domain.order import Order
from sample_order_system.domain.order_registry import OrderRegistry


def create_order(
    order_registry: OrderRegistry,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    sample_id = input_func("시료 ID: ")
    customer_name = input_func("고객명: ")
    quantity = int(input_func("주문 수량: "))

    order = Order(
        sample_id=sample_id,
        customer_name=customer_name,
        quantity=quantity,
    )
    order_registry.register(order)
    output_func(f"주문 접수 완료 ({customer_name}, {sample_id} x {quantity})")
