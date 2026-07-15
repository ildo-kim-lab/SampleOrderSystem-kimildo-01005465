# PLAN.md (이번 증분)

## 목표
접수된(RESERVED) 주문을 승인할 때, 재고가 주문 수량 이상으로 충분하면
즉시 CONFIRMED 상태로 전환된다.

## 검증할 동작
`Order.approve(available_stock)`를 주문 수량 이상의 재고 값으로 호출하면
상태가 `OrderStatus.CONFIRMED`가 된다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 재고가 충분한 경우: 주문을 즉시 CONFIRMED
  상태로 전환
- `docs/PRD.md` 4. 주문 상태 (State Machine)

## 범위 외
- 재고 부족 시 PRODUCING 전환 및 생산 라인 등록은 다음 증분에서 다룬다.
- `SampleRegistry`/실제 재고 조회 연동은 다음 증분에서 다룬다 (이번 증분은
  `approve()`가 재고 수치를 인자로 받는 순수 도메인 로직만 다룬다).
