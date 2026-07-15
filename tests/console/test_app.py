import pytest

from sample_order_system.console.app import resolve_main_menu_choice


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
