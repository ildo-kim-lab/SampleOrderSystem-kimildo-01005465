# PLAN.md (이번 증분)

## 목표
`Order.complete_production()`은 PRODUCING 상태의 주문에서만 호출할 수
있다.

## 검증할 동작
`RESERVED` 상태인 주문에 대해 `complete_production()`을 호출하면
`ValueError`가 발생한다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 생산 완료는 PRODUCING(생산 중) 주문에
  대해서만 의미가 있다.

## 범위 외
- 이 증분으로 `Order`의 상태 전제 조건 강화(approve/release/
  complete_production) 항목이 모두 마무리된다.
