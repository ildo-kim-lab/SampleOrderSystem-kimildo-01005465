# PLAN.md (이번 증분)

## 목표
`Order.approve()`는 RESERVED 상태의 주문에서만 호출할 수 있다. 그 외 상태
(PRODUCING, CONFIRMED 등 종료 상태가 아니더라도)에서 호출하면 예외가
발생한다.

## 검증할 동작
이미 `PRODUCING` 상태인 주문에 대해 `approve()`를 다시 호출하면
`ValueError`가 발생한다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 승인은 "접수된"(RESERVED) 주문에 대한
  동작이다. 지금까지는 종료 상태(REJECTED/RELEASED)만 막고 있어, PRODUCING/
  CONFIRMED 상태에서 재호출해도 막지 못하는 방어 공백이 있었다.

## 범위 외
- `release()`(CONFIRMED 상태 전제), `complete_production()`(PRODUCING 상태
  전제)의 동일한 강화는 다음 증분들에서 다룬다.
