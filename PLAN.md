# PLAN.md (이번 증분)

## 목표
`release_order`도 주문에 명시된 시료 ID가 `SampleRegistry`에 없으면 명확한
예외를 발생시킨다.

## 검증할 동작
`release_order(order, registry)`를 호출했을 때 `registry`에 해당
`sample_id`의 시료가 없으면 `ValueError`가 발생한다.

## 근거
- `approve_order`와 동일한 이유(`docs/PRD.md` 5.7 출고 처리)

## 범위 외
- `complete_order_production`의 동일한 예외 처리는 다음 증분에서 다룬다.
