from typing import Callable

from sample_order_system.console.controller import (
    list_samples,
    register_sample,
    search_samples,
)
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


_SAMPLE_MENU_CHOICES = {
    "0": "뒤로가기",
    "1": "등록",
    "2": "조회",
    "3": "검색",
}


def resolve_sample_menu_choice(choice: str) -> str | None:
    return _SAMPLE_MENU_CHOICES.get(choice)


_ORDER_MENU_CHOICES = {
    "0": "뒤로가기",
    "1": "접수",
    "2": "승인",
    "3": "거절",
}


def resolve_order_menu_choice(choice: str) -> str | None:
    return _ORDER_MENU_CHOICES.get(choice)


def run_sample_menu(
    state: AppState,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    while True:
        choice = input_func("선택: ")
        action = resolve_sample_menu_choice(choice)
        if action == "뒤로가기":
            return
        if action == "등록":
            register_sample(state.sample_registry, input_func, output_func)
        elif action == "조회":
            list_samples(state.sample_registry, output_func)
        elif action == "검색":
            keyword = input_func("검색어: ")
            search_samples(state.sample_registry, keyword, output_func)


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
        if menu_name == "시료관리":
            run_sample_menu(state, input_func, output_func)
