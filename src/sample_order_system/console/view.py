from sample_order_system.domain.order import Order
from sample_order_system.domain.sample import Sample


def format_sample_line(sample: Sample) -> str:
    return f"{sample.sample_id} | {sample.name} | 재고: {sample.stock}"


def format_order_line(order: Order) -> str:
    return f"{order.sample_id} | {order.customer_name} | 수량: {order.quantity}"


def format_main_menu() -> str:
    return (
        "===== SampleOrderSystem =====\n"
        "1. 시료관리\n"
        "2. 주문(접수/승인/거절)\n"
        "3. 모니터링\n"
        "4. 출고 처리\n"
        "5. 생산 라인\n"
        "9. 더미 데이터 생성\n"
        "0. 종료\n"
    )


def format_sample_menu() -> str:
    return (
        "----- 시료관리 -----\n"
        "1. 등록\n"
        "2. 조회\n"
        "3. 검색\n"
        "0. 뒤로가기\n"
    )


def format_order_menu() -> str:
    return (
        "----- 주문 -----\n"
        "1. 접수\n"
        "2. 승인\n"
        "3. 거절\n"
        "0. 뒤로가기\n"
    )


def format_production_menu() -> str:
    return (
        "----- 생산 라인 -----\n"
        "1. 생산 현황\n"
        "2. 대기 주문 확인\n"
        "3. 생산 완료 처리\n"
        "0. 뒤로가기\n"
    )
