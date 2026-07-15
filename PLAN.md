# PLAN.md (이번 증분)

## 목표
이미 REJECTED 또는 RELEASED 상태인 주문에 대해 `reject()`를 호출하면
예외가 발생한다 (종료 상태에서는 더 이상 전이가 없어야 한다).

## 검증할 동작
`Order.reject()`를 `REJECTED` 또는 `RELEASED` 상태의 주문에 대해 호출하면
`ValueError`가 발생한다.

## 근거
- `docs/PRD.md` 4. 주문 상태 (State Machine) — REJECTED, RELEASED는 종료
  상태이며 이후 상태 변경 불가
- `CLAUDE.md` 도메인 규칙 요약 — REJECTED, RELEASED는 종료 상태, 이후 전이가
  발생하면 버그로 간주

## 범위 외
- `approve()`, `release()`, `complete_production()`의 동일한 가드는 다음
  증분들에서 다룬다.
