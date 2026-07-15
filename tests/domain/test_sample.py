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
