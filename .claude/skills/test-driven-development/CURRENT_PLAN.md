# CURRENT_PLAN.md (이번 증분, 순수 리팩터링)

## 목표
`create_order`(order_controller.py)와 `_select_order_by_status`(app.py)가
각자 구현하고 있던 "번호가 붙은 목록 출력 → 정수 파싱(예외 처리 포함) →
범위 검증" 패턴을 공용 제네릭 헬퍼로 통일한다.

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 `test_order_controller.py`,
`test_order_menu_empty_selection.py`, `test_app.py` 등의 관련 테스트가
리팩터링 전후 모두 그대로 통과해야 한다.

## 근거
- Clean Code 리뷰(2차) finding 4: 두 곳이 동일한 "번호로 목록에서 선택"
  패턴을 독자적으로 구현하고 있어, 선택 UX를 바꾸려면(예: 취소 옵션
  추가) 두 곳을 각각 고쳐야 한다.

## 범위 외
- 없음. 순수 리팩터링이므로 RED 단계 없이 진행한다.
