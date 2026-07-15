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

    def reject(self) -> None:
        if self.status in _TERMINAL_STATUSES:
            raise ValueError(f"종료 상태({self.status.value})에서는 거절할 수 없습니다")
        self.status = OrderStatus.REJECTED

    def approve(self, available_stock: int) -> None:
        if self.status in _TERMINAL_STATUSES:
            raise ValueError(f"종료 상태({self.status.value})에서는 승인할 수 없습니다")
        if available_stock >= self.quantity:
            self.status = OrderStatus.CONFIRMED
        else:
            self.status = OrderStatus.PRODUCING

    def release(self) -> None:
        self.status = OrderStatus.RELEASED

    def complete_production(self) -> None:
        self.status = OrderStatus.CONFIRMED
