import pytest

from sample_order_system.console.app import run_sample_menu
from sample_order_system.console.state import AppState
from sample_order_system.domain.sample import Sample


def test_run_sample_menu_returns_immediately_on_back_choice():
    state = AppState()
    inputs = iter(["0"])
    outputs = []

    run_sample_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    with pytest.raises(StopIteration):
        next(inputs)


def test_run_sample_menu_registers_sample_then_returns_to_menu():
    state = AppState()
    inputs = iter(["1", "S-001", "Wafer-A", "2.5", "0.9", "0"])
    outputs = []

    run_sample_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    sample = state.sample_registry.find_by_id("S-001")
    assert sample is not None
    assert sample.name == "Wafer-A"


def test_run_sample_menu_lists_samples_then_returns_to_menu():
    state = AppState()
    state.sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=10,
        )
    )
    inputs = iter(["2", "0"])
    outputs = []

    run_sample_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("Wafer-A" in message for message in outputs)


def test_run_sample_menu_searches_samples_by_keyword_then_returns_to_menu():
    state = AppState()
    state.sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
        )
    )
    state.sample_registry.register(
        Sample(
            sample_id="S-002",
            name="Chip-B",
            avg_production_time=1.0,
            yield_rate=0.8,
        )
    )
    inputs = iter(["3", "Wafer", "0"])
    outputs = []

    run_sample_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    combined_output = "\n".join(outputs)
    assert "Wafer-A" in combined_output
    assert "Chip-B" not in combined_output
