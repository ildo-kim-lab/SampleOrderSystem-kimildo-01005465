# PLAN.md (이번 증분)

## 목표
메인 메뉴에서 "9"를 선택하면 더미 시료/주문 데이터가 한 번에 생성된다.

## 검증할 동작
`run_app`에 입력으로 "9"(더미 데이터 생성), "0"(종료)을 주면,
`state.sample_registry`와 `state.order_registry`에 더미 데이터가 채워진다.

## 근거
- `docs/PLAN.md` Phase 2 — Dummy Data Generator

## 범위 외
- 메인 메뉴 화면 텍스트(`format_main_menu`)에 "9" 항목을 명시적으로 추가하는
  것은 이번 증분에서 함께 처리한다(범위 내). 그 외 UX 개선은 다루지 않는다.
