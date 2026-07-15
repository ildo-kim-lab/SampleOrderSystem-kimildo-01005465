from dataclasses import dataclass, field
from enum import Enum


class OrderStatus(Enum):
    RESERVED = "RESERVED"
    REJECTED = "REJECTED"
    PRODUCING = "PRODUCING"
    CONFIRMED = "CONFIRMED"
    RELEASED = "RELEASED"


_TERMINAL_STATUSES = (OrderStatus.REJECTED, OrderStatus.RELEASED)


@dataclass
class Order:
    sample_id: str
    customer_name: str
    quantity: int
    status: OrderStatus = field(default=OrderStatus.RESERVED)

    def _check_status_is(self, expected: OrderStatus, action_label: str) -> None:
        if self.status != expected:
            raise ValueError(
                f"{self.status.value} 상태에서는 {action_label}할 수 없습니다 "
                f"({expected.value} 상태에서만 가능)"
            )

    def reject(self) -> None:
        self._check_status_is(OrderStatus.RESERVED, "거절")
        self.status = OrderStatus.REJECTED

    def approve(self, available_stock: int) -> None:
        self._check_status_is(OrderStatus.RESERVED, "승인")
        if available_stock >= self.quantity:
            self.status = OrderStatus.CONFIRMED
        else:
            self.status = OrderStatus.PRODUCING

    def release(self) -> None:
        self._check_status_is(OrderStatus.CONFIRMED, "출고")
        self.status = OrderStatus.RELEASED

    def complete_production(self) -> None:
        self._check_status_is(OrderStatus.PRODUCING, "생산 완료 처리")
        self.status = OrderStatus.CONFIRMED
