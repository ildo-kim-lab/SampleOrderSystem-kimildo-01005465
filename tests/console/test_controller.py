from sample_order_system.console.controller import list_samples, register_sample
from sample_order_system.domain.sample import Sample, SampleRegistry


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


def test_list_samples_outputs_name_and_stock_for_each_sample():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=42,
        )
    )
    outputs = []

    list_samples(registry, output_func=outputs.append)

    combined_output = "\n".join(outputs)
    assert "Wafer-A" in combined_output
    assert "42" in combined_output
