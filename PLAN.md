# PLAN.md (이번 증분)

## 목표
콘솔에서 현재 생산 중인 시료/주문 정보와 현재까지의 생산량을 확인할 수 있다.

## 검증할 동작
`show_production_status(line, output_func)`를 호출하면, `line.current_order`가
있을 때 시료 ID/고객명/생산량이 출력되고, 없을 때는 "생산 중인 주문 없음"이
출력된다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 생산 현황표기

## 범위 외
- 생산 완료(complete_production_console)와 ProductionLine 상태의 실제 연동은
  다음 증분에서 다룬다.
