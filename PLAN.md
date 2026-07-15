# PLAN.md (이번 증분)

## 목표
접수된(RESERVED) 주문을 승인할 때, 재고가 주문 수량보다 부족하면
PRODUCING 상태로 전환된다 (생산 라인 등록 자체는 다음 증분).

## 검증할 동작
`Order.approve(available_stock)`를 주문 수량보다 적은 재고 값으로 호출하면
상태가 `OrderStatus.PRODUCING`이 된다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 재고가 부족한 경우: 생산 라인에 자동으로
  등록, 주문 상태를 PRODUCING으로 전환
- `docs/PRD.md` 4. 주문 상태 (State Machine)

## 범위 외
- 생산 라인에 실제로 등록하는 로직(생산 큐, 생산량/시간 계산)은 다음 증분에서 다룬다.
