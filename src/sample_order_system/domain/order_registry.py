from sample_order_system.domain.order import Order


class OrderRegistry:
    def __init__(self) -> None:
        self._orders: list[Order] = []

    def register(self, order: Order) -> None:
        self._orders.append(order)

    def get_all(self) -> list[Order]:
        return list(self._orders)
