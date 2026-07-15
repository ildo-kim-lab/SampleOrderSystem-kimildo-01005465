# PLAN.md (이번 증분)

## 목표
주문을 승인할 때, 주문에 명시된 시료 ID가 `SampleRegistry`에 없으면
명확한 예외를 발생시킨다 (이전 증분에서 범위 외로 미뤄뒀던 부분).

## 검증할 동작
`approve_order(order, registry)`를 호출했을 때 `registry`에 해당
`sample_id`의 시료가 없으면 `ValueError`가 발생한다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 승인은 실제 존재하는 시료를 전제로 한다.
  이전 증분(`approve_order` 최초 구현)에서 "시료를 찾지 못했을 때의 예외
  처리는 다음 증분에서 다룬다"고 명시했던 부분.

## 범위 외
- `release_order`, `complete_order_production`의 동일한 예외 처리는
  다음 증분에서 다룬다.
