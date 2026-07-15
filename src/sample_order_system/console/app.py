from pathlib import Path
from typing import Callable

from sample_order_system.persistence import (
    load_orders,
    load_production_queue,
    load_samples,
    save_orders,
    save_production_queue,
    save_samples,
)

from sample_order_system.console.controller import (
    list_samples,
    register_sample,
    search_samples,
)
from sample_order_system.console.monitoring_controller import (
    monitor_order_counts,
    monitor_stock_levels,
)
from sample_order_system.console.order_controller import (
    approve_order_console,
    create_order,
    reject_order_console,
)
from sample_order_system.console.production_controller import (
    complete_next_production_console,
    list_waiting_orders,
    show_production_status,
)
from sample_order_system.console.dummy_data import (
    generate_dummy_orders,
    generate_dummy_samples,
)
from sample_order_system.console.release_controller import release_order_console
from sample_order_system.console.selection import select_from_list
from sample_order_system.console.state import AppState
from sample_order_system.console.view import (
    format_main_menu,
    format_order_line,
    format_order_menu,
    format_production_menu,
    format_sample_menu,
)
from sample_order_system.domain.order import Order, OrderStatus

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


_ORDER_MENU_CHOICES = {
    "0": "뒤로가기",
    "1": "접수",
    "2": "승인",
    "3": "거절",
}


_PRODUCTION_MENU_CHOICES = {
    "0": "뒤로가기",
    "1": "생산 현황",
    "2": "대기 주문 확인",
    "3": "생산 완료 처리",
}


def _select_order_by_status(
    state: AppState,
    status: OrderStatus,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
    prompt: str,
) -> Order | None:
    matching_orders = [
        order for order in state.order_registry.get_all() if order.status == status
    ]
    return select_from_list(
        matching_orders,
        format_order_line,
        input_func,
        output_func,
        prompt,
        "대상 주문이 없습니다",
    )


def _run_menu_loop(
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
    menu_text: str,
    choices: dict[str, str],
    handlers: dict[str, Callable[[], None]],
) -> None:
    while True:
        output_func(menu_text)
        choice = input_func("선택: ")
        action = choices.get(choice)
        if action == "뒤로가기":
            return
        handler = handlers.get(action)
        if handler is not None:
            handler()


def run_sample_menu(
    state: AppState,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    def do_search() -> None:
        keyword = input_func("검색어: ")
        search_samples(state.sample_registry, keyword, output_func)

    _run_menu_loop(
        input_func,
        output_func,
        format_sample_menu(),
        _SAMPLE_MENU_CHOICES,
        {
            "등록": lambda: register_sample(state.sample_registry, input_func, output_func),
            "조회": lambda: list_samples(state.sample_registry, output_func),
            "검색": do_search,
        },
    )


def run_order_menu(
    state: AppState,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    def do_approve() -> None:
        selected_order = _select_order_by_status(
            state, OrderStatus.RESERVED, input_func, output_func, "승인할 번호: "
        )
        if selected_order is not None:
            approve_order_console(
                selected_order, state.sample_registry, state.production_queue, output_func
            )

    def do_reject() -> None:
        selected_order = _select_order_by_status(
            state, OrderStatus.RESERVED, input_func, output_func, "거절할 번호: "
        )
        if selected_order is not None:
            reject_order_console(selected_order, output_func)

    _run_menu_loop(
        input_func,
        output_func,
        format_order_menu(),
        _ORDER_MENU_CHOICES,
        {
            "접수": lambda: create_order(
                state.order_registry, state.sample_registry, input_func, output_func
            ),
            "승인": do_approve,
            "거절": do_reject,
        },
    )


def run_production_menu(
    state: AppState,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
) -> None:
    _run_menu_loop(
        input_func,
        output_func,
        format_production_menu(),
        _PRODUCTION_MENU_CHOICES,
        {
            "생산 현황": lambda: show_production_status(
                state.production_line, output_func
            ),
            "대기 주문 확인": lambda: list_waiting_orders(
                state.production_queue, output_func
            ),
            "생산 완료 처리": lambda: complete_next_production_console(
                state.production_queue, state.sample_registry, output_func
            ),
        },
    )


def run_app(
    state: AppState,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
    sample_filepath: Path | None = None,
    order_filepath: Path | None = None,
    queue_filepath: Path | None = None,
) -> None:
    def do_monitoring() -> None:
        monitor_order_counts(state.order_registry, output_func)
        monitor_stock_levels(state.sample_registry, state.order_registry, output_func)

    def do_release() -> None:
        selected_order = _select_order_by_status(
            state, OrderStatus.CONFIRMED, input_func, output_func, "출고할 번호: "
        )
        if selected_order is not None:
            release_order_console(selected_order, state.sample_registry, output_func)

    handlers: dict[str, Callable[[], None]] = {
        "시료관리": lambda: run_sample_menu(state, input_func, output_func),
        "주문": lambda: run_order_menu(state, input_func, output_func),
        "모니터링": do_monitoring,
        "출고 처리": do_release,
        "생산 라인": lambda: run_production_menu(state, input_func, output_func),
    }

    while True:
        output_func(format_main_menu())
        choice = input_func("선택: ")
        if choice == "0":
            if sample_filepath is not None:
                save_samples(state.sample_registry, sample_filepath)
            if order_filepath is not None:
                save_orders(state.order_registry, order_filepath)
            if queue_filepath is not None:
                save_production_queue(state.production_queue, queue_filepath)
            output_func("프로그램을 종료합니다")
            return
        if choice == "9":
            generate_dummy_samples(state.sample_registry)
            generate_dummy_orders(state.order_registry)
            output_func("더미 데이터 생성 완료")
            continue
        menu_name = resolve_main_menu_choice(choice)
        if menu_name is None:
            output_func("잘못된 선택입니다")
            continue
        output_func(f"[{menu_name}]")
        handlers[menu_name]()


def start_app(
    sample_filepath: Path,
    order_filepath: Path,
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
    queue_filepath: Path | None = None,
) -> None:
    state = AppState()
    if sample_filepath.exists():
        state.sample_registry = load_samples(sample_filepath)
    if order_filepath.exists():
        state.order_registry = load_orders(order_filepath)
    if queue_filepath is not None and queue_filepath.exists():
        state.production_queue = load_production_queue(queue_filepath)
    run_app(
        state,
        input_func,
        output_func,
        sample_filepath,
        order_filepath,
        queue_filepath,
    )
