# PLAN.md (이번 증분)

## 목표
`Order.release()`는 CONFIRMED 상태의 주문에서만 호출할 수 있다.

## 검증할 동작
`RESERVED` 상태인 주문에 대해 `release()`를 호출하면 `ValueError`가
발생한다.

## 근거
- `docs/PRD.md` 5.7 출고 처리 — CONFIRMED 상태 주문에 대해서만 출고를
  실행한다.

## 범위 외
- `complete_production()`(PRODUCING 상태 전제)의 동일한 강화는 다음 증분에서
  다룬다.
