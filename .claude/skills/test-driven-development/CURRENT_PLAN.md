# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
`console/app.py`의 메뉴 라우팅 3곳(run_sample_menu, run_order_menu,
run_app)이 각자 반복하던 "선택 → resolve → if/elif 분기" 패턴을, 공용
서브메뉴 루프 헬퍼(`_run_menu_loop`)와 액션→핸들러 딕셔너리로 통일한다.
(Clean Code 리뷰 finding 3)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 콘솔 라우팅 테스트
(`tests/console/test_app.py`, `test_sample_menu.py`, `test_order_menu.py`,
`test_order_menu_empty_selection.py` 등)가 리팩터링 전후 모두 그대로
통과해야 한다.

## 근거
- Clean Code 리뷰 finding 3: 세 곳이 독립적으로 choices-dict + resolver +
  if/elif를 반복 구현하고 있어, 메뉴 항목 추가/변경 시 세 곳을 모두
  고쳐야 하는 유지보수 비용이 있었다.

## 범위 외
- 없음 (이 증분으로 finding 3이 마무리된다). 순수 리팩터링이므로 RED 단계
  없이 진행하고, 리팩터링 전후 테스트가 계속 GREEN임을 확인한다.
