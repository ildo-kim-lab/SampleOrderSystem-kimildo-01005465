from sample_order_system.console.dummy_data import (
    generate_dummy_orders,
    generate_dummy_samples,
)
from sample_order_system.domain.order import OrderStatus
from sample_order_system.domain.order_registry import OrderRegistry
from sample_order_system.domain.sample import SampleRegistry


def test_generate_dummy_samples_creates_varied_stock_levels():
    registry = SampleRegistry()

    generate_dummy_samples(registry)

    samples = registry.get_all()
    assert len(samples) >= 3
    stocks = [sample.stock for sample in samples]
    assert 0 in stocks
    assert len(set(stocks)) > 1


def test_generate_dummy_samples_is_idempotent_when_called_twice():
    registry = SampleRegistry()
    generate_dummy_samples(registry)

    generate_dummy_samples(registry)

    assert len(registry.get_all()) == 3


def test_generate_dummy_orders_covers_all_five_statuses():
    registry = OrderRegistry()

    generate_dummy_orders(registry)

    statuses = {order.status for order in registry.get_all()}
    assert statuses == {
        OrderStatus.RESERVED,
        OrderStatus.REJECTED,
        OrderStatus.PRODUCING,
        OrderStatus.CONFIRMED,
        OrderStatus.RELEASED,
    }
