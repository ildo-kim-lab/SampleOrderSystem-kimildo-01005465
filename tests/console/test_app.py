import pytest

from sample_order_system.console.app import (
    resolve_main_menu_choice,
    resolve_order_menu_choice,
    resolve_sample_menu_choice,
    run_app,
)
from sample_order_system.console.state import AppState


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
    inputs = iter(["9", "0"])
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
