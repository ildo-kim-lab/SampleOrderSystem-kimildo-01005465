from sample_order_system.console.state import AppState
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.production_line_status import ProductionLine
from sample_order_system.domain.production_queue import ProductionQueue
from sample_order_system.domain.sample import SampleRegistry


def test_app_state_initializes_empty_registries():
    state = AppState()

    assert isinstance(state.sample_registry, SampleRegistry)
    assert isinstance(state.order_registry, OrderRegistry)
    assert isinstance(state.production_queue, ProductionQueue)
    assert isinstance(state.production_line, ProductionLine)
    assert state.sample_registry.get_all() == []
    assert state.order_registry.get_all() == []
