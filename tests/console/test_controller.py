from sample_order_system.console.controller import register_sample
from sample_order_system.domain.sample import SampleRegistry


def test_register_sample_adds_sample_with_entered_values():
    registry = SampleRegistry()
    inputs = iter(["S-001", "Wafer-A", "2.5", "0.9"])
    outputs = []

    register_sample(
        registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    sample = registry.find_by_id("S-001")
    assert sample is not None
    assert sample.name == "Wafer-A"
    assert sample.avg_production_time == 2.5
    assert sample.yield_rate == 0.9
