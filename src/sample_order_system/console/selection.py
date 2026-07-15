from typing import Callable, TypeVar

T = TypeVar("T")


def select_from_list(
    items: list[T],
    format_item: Callable[[T], str],
    input_func: Callable[[str], str],
    output_func: Callable[[str], None],
    prompt: str,
    empty_message: str,
) -> T | None:
    if not items:
        output_func(empty_message)
        return None
    for index, item in enumerate(items, start=1):
        output_func(f"{index}. {format_item(item)}")
    try:
        index_choice = int(input_func(prompt))
    except ValueError:
        output_func("숫자 형식이 올바르지 않습니다")
        return None
    if not 1 <= index_choice <= len(items):
        output_func("잘못된 번호입니다")
        return None
    return items[index_choice - 1]
