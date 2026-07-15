import pytest

from sample_order_system.console.app import run_sample_menu
from sample_order_system.console.state import AppState


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
