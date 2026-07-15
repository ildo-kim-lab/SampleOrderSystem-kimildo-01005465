from typing import Callable

from sample_order_system.console.state import AppState
from sample_order_system.console.view import format_main_menu

_MAIN_MENU_CHOICES = {
    "1": "시료관리",
    "2": "주문",
    "3": "모니터링",
    "4": "출고 처리",
    "5": "생산 라인",
}


def resolve_main_menu_choice(choice: str) -> str | None:
    return _MAIN_MENU_CHOICES.get(choice)


def run_app(
    state: AppState,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    while True:
        output_func(format_main_menu())
        choice = input_func("선택: ")
        if choice == "0":
            output_func("프로그램을 종료합니다")
            return
        menu_name = resolve_main_menu_choice(choice)
        if menu_name is None:
            output_func("잘못된 선택입니다")
            continue
        output_func(f"[{menu_name}]")
