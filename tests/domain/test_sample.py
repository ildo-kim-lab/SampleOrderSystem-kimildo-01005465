import pytest

from sample_order_system.domain.sample import Sample, SampleRegistry


def test_registered_sample_appears_in_get_all():
    registry = SampleRegistry()
    sample = Sample(
        sample_id="S-001",
        name="Wafer-A",
        avg_production_time=2.5,
        yield_rate=0.9,
    )

    registry.register(sample)

    assert sample in registry.get_all()


def test_sample_reports_its_stock_quantity():
    sample = Sample(
        sample_id="S-001",
        name="Wafer-A",
        avg_production_time=2.5,
        yield_rate=0.9,
        stock=50,
    )

    assert sample.stock == 50


def test_decrease_stock_reduces_stock_by_given_quantity():
    sample = Sample(
        sample_id="S-001",
        name="Wafer-A",
        avg_production_time=2.5,
        yield_rate=0.9,
        stock=50,
    )

    sample.decrease_stock(10)

    assert sample.stock == 40


def test_increase_stock_adds_given_quantity():
    sample = Sample(
        sample_id="S-001",
        name="Wafer-A",
        avg_production_time=2.5,
        yield_rate=0.9,
        stock=50,
    )

    sample.increase_stock(12)

    assert sample.stock == 62


def test_find_by_id_returns_registered_sample():
    registry = SampleRegistry()
    sample = Sample(
        sample_id="S-001",
        name="Wafer-A",
        avg_production_time=2.5,
        yield_rate=0.9,
    )
    registry.register(sample)

    assert registry.find_by_id("S-001") is sample


def test_register_raises_on_duplicate_sample_id():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
        )
    )

    with pytest.raises(ValueError, match="S-001"):
        registry.register(
            Sample(
                sample_id="S-001",
                name="Wafer-A-Duplicate",
                avg_production_time=1.0,
                yield_rate=0.8,
            )
        )
