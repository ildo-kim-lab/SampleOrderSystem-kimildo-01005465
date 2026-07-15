# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode)
`Order.reject()`도 `approve()`/`release()`/`complete_production()`과 동일하게
정확히 하나의 선행 상태(RESERVED)에서만 허용하도록 전제조건을 강화한다.
(Clean Code 리뷰에서 발견된 항목 1: `reject()`만 `_check_not_terminal`을
써서 PRODUCING/CONFIRMED 상태에서도 거절이 가능한 비일관성)

## 검증할 동작
`PRODUCING` 상태인 주문에 대해 `reject()`를 호출하면 `ValueError`가
발생한다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 거절은 접수된(RESERVED) 주문에 대한
  동작이다.
- Clean Code 리뷰 finding 1: `reject()`의 가드가 다른 세 전이 메서드와
  다른 방식(`_check_not_terminal` vs `_check_status_is`)이라 PRODUCING/
  CONFIRMED 상태에서도 거절이 통과되는 비일관성이 있었다.

## 범위 외
- 없음 (이 증분으로 finding 1이 마무리된다).
