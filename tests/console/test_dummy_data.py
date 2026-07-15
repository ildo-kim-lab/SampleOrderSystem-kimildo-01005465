from sample_order_system.console.dummy_data import generate_dummy_samples
from sample_order_system.domain.sample import SampleRegistry


def test_generate_dummy_samples_creates_varied_stock_levels():
    registry = SampleRegistry()

    generate_dummy_samples(registry)

    samples = registry.get_all()
    assert len(samples) >= 3
    stocks = [sample.stock for sample in samples]
    assert 0 in stocks
    assert len(set(stocks)) > 1
