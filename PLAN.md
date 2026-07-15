# PLAN.md (이번 증분)

## 목표
이미 종료 상태(REJECTED/RELEASED)인 주문에 대해 `release()`를 호출하면
예외가 발생한다.

## 검증할 동작
`Order.release()`를 `REJECTED` 상태의 주문에 대해 호출하면 `ValueError`가
발생한다.

## 근거
- `docs/PRD.md` 4. 주문 상태 (State Machine), `CLAUDE.md` 도메인 규칙 요약

## 범위 외
- `complete_production()`의 동일한 가드는 다음 증분에서 다룬다.
