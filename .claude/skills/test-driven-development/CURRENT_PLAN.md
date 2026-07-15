# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
시료 표시 줄(`"{id} | {name} | 재고: {stock}"`)과 주문 표시 줄
(`"{sample_id} | {customer_name} | 수량: {quantity}"`)이 각각 두 곳에
하드코딩된 것을, `console/view.py`의 공용 포맷 함수(`format_sample_line`,
`format_order_line`)로 통일한다. (Clean Code 리뷰 finding 7)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 콘솔 컨트롤러 테스트들
(`test_controller.py`, `test_production_controller.py`,
`test_order_menu_empty_selection.py` 등)이 리팩터링 전후 모두 그대로
통과해야 한다.

## 근거
- Clean Code 리뷰 finding 7: 같은 표시 포맷이 `controller.py`의
  `list_samples`/`search_samples`, 그리고 `production_controller.py`의
  `list_waiting_orders`/`console/app.py`의 `_select_order_by_status`에
  각각 하드코딩되어 있어, 포맷을 바꾸려면 여러 곳을 손으로 맞춰야 한다.

## 범위 외
- 없음 (이 증분으로 finding 7이 마무리된다). 순수 리팩터링이므로 RED 단계
  없이 진행하고, 리팩터링 전후 테스트가 계속 GREEN임을 확인한다.
