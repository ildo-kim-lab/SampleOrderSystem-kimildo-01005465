from dataclasses import dataclass

from sample_order_system.domain.order import Order


@dataclass
class ProductionLine:
    current_order: Order | None = None
    produced_quantity: int = 0
