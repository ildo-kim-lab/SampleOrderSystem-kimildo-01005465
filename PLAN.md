# PLAN.md (이번 증분)

## 목표
이미 종료 상태(REJECTED/RELEASED)인 주문에 대해 `complete_production()`을
호출하면 예외가 발생한다.

## 검증할 동작
`Order.complete_production()`을 `REJECTED` 상태의 주문에 대해 호출하면
`ValueError`가 발생한다.

## 근거
- `docs/PRD.md` 4. 주문 상태 (State Machine), `CLAUDE.md` 도메인 규칙 요약

## 범위 외
- 이 증분으로 `Order`의 모든 상태 전이 메서드에 종료 상태 가드가 적용된다.
