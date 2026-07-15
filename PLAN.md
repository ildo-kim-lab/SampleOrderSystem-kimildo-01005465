# PLAN.md (이번 증분)

## 목표
CONFIRMED 상태의 주문에 대해 출고를 실행하면 RELEASED 상태로 전환된다.

## 검증할 동작
`Order.release()`를 호출하면 상태가 `OrderStatus.RELEASED`가 된다.

## 근거
- `docs/PRD.md` 5.7 출고 처리 — CONFIRMED 상태 주문 대상으로 출고 실행,
  실행 시 상태 CONFIRMED → RELEASED
- `docs/PRD.md` 4. 주문 상태 (State Machine) — RELEASED는 종료 상태

## 범위 외
- CONFIRMED가 아닌 상태에서 release()를 호출했을 때의 예외 처리는
  다음 증분(잘못된 전이 방지)에서 다룬다.
