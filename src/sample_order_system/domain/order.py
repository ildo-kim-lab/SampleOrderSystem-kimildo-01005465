from dataclasses import dataclass, field
from enum import Enum


class OrderStatus(Enum):
    RESERVED = "RESERVED"
    REJECTED = "REJECTED"
    PRODUCING = "PRODUCING"
    CONFIRMED = "CONFIRMED"
    RELEASED = "RELEASED"


@dataclass
class Order:
    sample_id: str
    customer_name: str
    quantity: int
    status: OrderStatus = field(default=OrderStatus.RESERVED)

    def reject(self) -> None:
        self.status = OrderStatus.REJECTED

    def approve(self, available_stock: int) -> None:
        if available_stock >= self.quantity:
            self.status = OrderStatus.CONFIRMED
        else:
            self.status = OrderStatus.PRODUCING

    def release(self) -> None:
        self.status = OrderStatus.RELEASED
