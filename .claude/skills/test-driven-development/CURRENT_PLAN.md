# CURRENT_PLAN.md (이번 증분, 순수 리팩터링)

## 목표
`resolve_sample_menu_choice`/`resolve_order_menu_choice`/
`resolve_production_menu_choice`를 제거한다. `_run_menu_loop`이 각
`_X_MENU_CHOICES` 딕셔너리를 직접 받아쓰기 때문에 이 세 resolver는
실제 라우팅에서 전혀 호출되지 않는 죽은 코드다 (자기 자신의 테스트에서만
호출됨).

## 검증할 동작
새로운 외부 동작 변화는 없다 — 세 함수와 그 전용 테스트를 제거하고,
나머지 테스트가 계속 GREEN임을 확인한다.

## 근거
- Clean Code 리뷰(2차) finding 7: 세 resolver 모두 `run_sample_menu`/
  `run_order_menu`/`run_production_menu`에서 호출되지 않음 (grep으로
  확인). 유지보수자가 이 함수들을 실제 라우팅 지점으로 오인하고 고쳐도
  아무 효과가 없다.

## 범위 외
- `resolve_main_menu_choice`는 `run_app`에서 실제로 호출되므로 그대로
  유지한다.
