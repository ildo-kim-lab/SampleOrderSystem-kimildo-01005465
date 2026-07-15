from sample_order_system.console.controller import (
    list_samples,
    register_sample,
    search_samples,
)
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


def test_register_sample_reports_friendly_message_on_duplicate_id():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
        )
    )
    inputs = iter(["S-001", "Wafer-A-Duplicate", "1.0", "0.8"])
    outputs = []

    register_sample(
        registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("이미 등록된" in message for message in outputs)


def test_register_sample_reports_friendly_message_on_non_numeric_input():
    registry = SampleRegistry()
    inputs = iter(["S-001", "Wafer-A", "abc", "0.9"])
    outputs = []

    register_sample(
        registry,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("숫자" in message for message in outputs)
    assert registry.find_by_id("S-001") is None


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


def test_search_samples_outputs_only_matching_name():
    registry = SampleRegistry()
    registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
        )
    )
    registry.register(
        Sample(
            sample_id="S-002",
            name="Chip-B",
            avg_production_time=1.0,
            yield_rate=0.8,
        )
    )
    outputs = []

    search_samples(registry, keyword="Wafer", output_func=outputs.append)

    combined_output = "\n".join(outputs)
    assert "Wafer-A" in combined_output
    assert "Chip-B" not in combined_output
