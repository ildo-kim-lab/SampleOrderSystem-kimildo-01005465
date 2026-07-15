# PLAN.md (이번 증분)

## 목표
생산 라인에서 생산이 완료되면, PRODUCING 상태의 주문이 CONFIRMED로 전환된다.

## 검증할 동작
`Order.complete_production()`을 호출하면 상태가 `OrderStatus.CONFIRMED`가 된다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 생산 완료 시 해당 주문 상태 PRODUCING → CONFIRMED

## 범위 외
- 생산 큐(FIFO), 생산 라인이 실제로 생산량/시간을 추적하며 진행 상태를
  보여주는 로직은 다음 증분에서 다룬다.
