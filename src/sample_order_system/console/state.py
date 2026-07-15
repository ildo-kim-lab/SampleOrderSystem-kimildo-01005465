from dataclasses import dataclass, field

from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.production_line_status import ProductionLine
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import SampleRegistry


@dataclass
class AppState:
    sample_registry: SampleRegistry = field(default_factory=SampleRegistry)
    order_registry: OrderRegistry = field(default_factory=OrderRegistry)
    production_queue: ProductionQueue = field(default_factory=ProductionQueue)
    production_line: ProductionLine = field(default_factory=ProductionLine)
