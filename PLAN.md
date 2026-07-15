# PLAN.md (이번 증분)

## 목표
생산이 완료되면, 주문 수량과 현재 재고의 부족분을 수율로 나눈 실 생산량만큼
재고가 증가하고, 주문 상태는 CONFIRMED로 전환된다.

## 검증할 동작
`complete_order_production(order, registry)`를 호출하면 `order.status`가
`CONFIRMED`가 되고, `sample.stock`이 `ceil((order.quantity - 기존 stock) / yield_rate)`
만큼 늘어난다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 실 생산량: ceil(부족분/수율), 생산 완료 시
  PRODUCING → CONFIRMED

## 범위 외
- 생산 큐(ProductionQueue) 연동, 생산 시간 추적/현황 표기는 다음 증분에서 다룬다.
