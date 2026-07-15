from sample_order_system.console.view import format_main_menu


def test_format_main_menu_lists_all_menu_items():
    menu = format_main_menu()

    assert "시료관리" in menu
    assert "주문" in menu
    assert "모니터링" in menu
    assert "출고 처리" in menu
    assert "생산 라인" in menu
    assert "더미 데이터" in menu
