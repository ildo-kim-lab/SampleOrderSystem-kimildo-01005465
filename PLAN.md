# PLAN.md (이번 증분)

## 목표
접수된(RESERVED) 주문을 거절하면 즉시 REJECTED 상태로 전환된다.

## 검증할 동작
`Order.reject()`를 호출하면 상태가 `OrderStatus.REJECTED`로 바뀐다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 주문거절: 즉시 REJECTED 상태로 전환
- `docs/PRD.md` 4. 주문 상태 (State Machine) — REJECTED는 종료 상태

## 범위 외
- 승인(재고 확인 포함), 종료 상태에서의 잘못된 전이 방지(예외 처리)는
  다음 증분에서 다룬다.
