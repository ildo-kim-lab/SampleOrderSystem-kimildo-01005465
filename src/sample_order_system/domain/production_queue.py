from collections import deque

from sample_order_system.domain.order import Order


class ProductionQueue:
    def __init__(self) -> None:
        self._orders: deque[Order] = deque()

    def enqueue(self, order: Order) -> None:
        self._orders.append(order)

    def dequeue(self) -> Order:
        return self._orders.popleft()
