# PLAN.md (이번 증분)

## 목표
고객이 시료를 주문(예약)하면, 그 주문은 `RESERVED` 상태로 생성된다.

## 검증할 동작
`Order`를 시료 ID, 고객명, 주문 수량으로 생성하면 상태가 `OrderStatus.RESERVED`다.

## 근거
- `docs/PRD.md` 5.3 시료 주문 (예약) — 입력값: 시료 ID, 고객명, 주문 수량,
  생성 시 상태는 `RESERVED`
- `docs/PRD.md` 4. 주문 상태 (State Machine)

## 범위 외
- 승인/거절, 재고 확인, 생산 라인 연동, 콘솔 UI는 이번 증분에 포함하지 않는다.
