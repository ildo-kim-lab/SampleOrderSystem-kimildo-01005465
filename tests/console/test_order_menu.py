import pytest

from sample_order_system.console.app import run_order_menu
from sample_order_system.console.state import AppState
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.sample import Sample


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


def test_run_order_menu_displays_menu_items_before_prompting():
    state = AppState()
    inputs = iter(["0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    combined_output = "\n".join(outputs)
    assert "접수" in combined_output
    assert "승인" in combined_output
    assert "거절" in combined_output


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


def test_run_order_menu_approves_selected_reserved_order():
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
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    state.order_registry.register(order)
    inputs = iter(["2", "1", "0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert order.status == OrderStatus.CONFIRMED


def test_run_order_menu_rejects_selected_reserved_order():
    state = AppState()
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    state.order_registry.register(order)
    inputs = iter(["3", "1", "0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert order.status == OrderStatus.REJECTED
