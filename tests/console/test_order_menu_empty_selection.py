from sample_order_system.console.app import run_order_menu
from sample_order_system.console.state import AppState
from sample_order_system.domain.order import Order


def test_run_order_menu_approve_with_no_reserved_orders_does_not_crash():
    state = AppState()
    inputs = iter(["2", "0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("없습니다" in message for message in outputs)


def test_run_order_menu_approve_with_out_of_range_index_does_not_crash():
    state = AppState()
    state.order_registry.register(
        Order(sample_id="S-001", customer_name="A", quantity=1)
    )
    inputs = iter(["2", "99", "0"])
    outputs = []

    run_order_menu(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("잘못된 번호" in message for message in outputs)
