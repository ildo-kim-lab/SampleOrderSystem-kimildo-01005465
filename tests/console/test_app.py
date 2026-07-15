import pytest

from sample_order_system.console.app import (
    resolve_main_menu_choice,
    resolve_order_menu_choice,
    resolve_sample_menu_choice,
    run_app,
)
from sample_order_system.console.state import AppState
from sample_order_system.domain.order import Order, OrderStatus
from sample_order_system.domain.sample import Sample


@pytest.mark.parametrize(
    "choice,expected",
    [
        ("1", "시료관리"),
        ("2", "주문"),
        ("3", "모니터링"),
        ("4", "출고 처리"),
        ("5", "생산 라인"),
        ("9", None),
        ("abc", None),
    ],
)
def test_resolve_main_menu_choice(choice, expected):
    assert resolve_main_menu_choice(choice) == expected


def test_run_app_exits_on_zero_choice():
    inputs = iter(["0"])
    outputs = []

    run_app(
        AppState(),
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("종료" in message for message in outputs)


def test_run_app_reports_invalid_choice_and_continues():
    inputs = iter(["99", "0"])
    outputs = []

    run_app(
        AppState(),
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("잘못된 선택" in message for message in outputs)
    assert any("종료" in message for message in outputs)


def test_run_app_enters_selected_menu():
    inputs = iter(["1", "0", "0"])
    outputs = []

    run_app(
        AppState(),
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert any("[시료관리]" in message for message in outputs)


def test_run_app_routes_sample_menu_choice_to_registration():
    state = AppState()
    inputs = iter(["1", "1", "S-001", "Wafer-A", "2.5", "0.9", "0", "0"])
    outputs = []

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    sample = state.sample_registry.find_by_id("S-001")
    assert sample is not None
    assert sample.name == "Wafer-A"


def test_run_app_routes_order_menu_choice_to_creation():
    state = AppState()
    inputs = iter(["2", "1", "S-001", "ACME Corp", "10", "0", "0"])
    outputs = []

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    orders = state.order_registry.get_all()
    assert len(orders) == 1
    assert orders[0].sample_id == "S-001"


def test_run_app_routes_monitoring_menu_choice():
    state = AppState()
    order = Order(sample_id="S-001", customer_name="A", quantity=1)
    state.order_registry.register(order)
    inputs = iter(["3", "0"])
    outputs = []

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    combined_output = "\n".join(outputs)
    assert "RESERVED: 1" in combined_output


def test_run_app_routes_release_menu_choice():
    state = AppState()
    state.sample_registry.register(
        Sample(
            sample_id="S-001",
            name="Wafer-A",
            avg_production_time=2.5,
            yield_rate=0.9,
            stock=50,
        )
    )
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=10)
    order.status = OrderStatus.CONFIRMED
    state.order_registry.register(order)
    inputs = iter(["4", "1", "0"])
    outputs = []

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert order.status == OrderStatus.RELEASED
    assert state.sample_registry.find_by_id("S-001").stock == 40


def test_run_app_routes_production_line_menu_choice():
    state = AppState()
    order = Order(sample_id="S-001", customer_name="ACME Corp", quantity=3)
    state.production_queue.enqueue(order)
    inputs = iter(["5", "0"])
    outputs = []

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    combined_output = "\n".join(outputs)
    assert "생산 중인 주문 없음" in combined_output
    assert "S-001 | ACME Corp | 수량: 3" in combined_output


def test_run_app_routes_dummy_data_menu_choice():
    state = AppState()
    inputs = iter(["9", "0"])
    outputs = []

    run_app(
        state,
        input_func=lambda prompt="": next(inputs),
        output_func=outputs.append,
    )

    assert len(state.sample_registry.get_all()) >= 3
    assert len(state.order_registry.get_all()) == 5


@pytest.mark.parametrize(
    "choice,expected",
    [
        ("1", "등록"),
        ("2", "조회"),
        ("3", "검색"),
        ("0", "뒤로가기"),
        ("9", None),
    ],
)
def test_resolve_sample_menu_choice(choice, expected):
    assert resolve_sample_menu_choice(choice) == expected


@pytest.mark.parametrize(
    "choice,expected",
    [
        ("1", "접수"),
        ("2", "승인"),
        ("3", "거절"),
        ("0", "뒤로가기"),
        ("9", None),
    ],
)
def test_resolve_order_menu_choice(choice, expected):
    assert resolve_order_menu_choice(choice) == expected
