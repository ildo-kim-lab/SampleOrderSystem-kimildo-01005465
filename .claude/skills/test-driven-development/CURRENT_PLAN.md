# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
`console/app.py`의 `_select_order_by_status`에 누락된 반환 타입 힌트
(`-> Order | None`)를 추가한다. (Clean Code 리뷰 finding 8)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 타입 힌트만 추가하는 것이므로 기존 테스트가
그대로 통과해야 한다.

## 근거
- `CLAUDE.md` 코딩 컨벤션: "타입 힌트를 모든 함수 시그니처에 명시한다."
  `_select_order_by_status`는 실제로 `Order | None`을 반환하는데 시그니처에
  반환 타입이 없었다.

## 범위 외
- 없음 (이 증분으로 Clean Code 리뷰 8개 항목이 모두 마무리된다). 순수
  리팩터링이므로 RED 단계 없이 진행하고, 테스트가 계속 GREEN임을 확인한다.
