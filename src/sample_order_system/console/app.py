_MAIN_MENU_CHOICES = {
    "1": "시료관리",
    "2": "주문",
    "3": "모니터링",
    "4": "출고 처리",
    "5": "생산 라인",
}


def resolve_main_menu_choice(choice: str) -> str | None:
    return _MAIN_MENU_CHOICES.get(choice)
