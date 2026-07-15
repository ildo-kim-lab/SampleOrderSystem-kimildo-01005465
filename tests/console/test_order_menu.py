import pytest

from sample_order_system.console.app import run_order_menu
from sample_order_system.console.state import AppState


def test_run_order_menu_returns_immediately_on_back_choice():
    state = AppState()
    inputs = iter(["0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    with pytest.raises(StopIteration):
        next(inputs)


def test_run_order_menu_creates_order_then_returns_to_menu():
    state = AppState()
    inputs = iter(["1", "S-001", "ACME Corp", "10", "0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    orders = state.order_registry.get_all()
    assert len(orders) == 1
    assert orders[0].sample_id == "S-001"
    assert orders[0].quantity == 10
