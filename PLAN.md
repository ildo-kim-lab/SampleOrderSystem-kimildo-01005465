# PLAN.md (이번 증분)

## 목표
`complete_order_production`도 주문에 명시된 시료 ID가 `SampleRegistry`에
없으면 명확한 예외를 발생시킨다.

## 검증할 동작
`complete_order_production(order, registry)`를 호출했을 때 `registry`에
해당 `sample_id`의 시료가 없으면 `ValueError`가 발생한다.

## 근거
- `approve_order`/`release_order`와 동일한 이유(`docs/PRD.md` 5.6 생산 라인)

## 범위 외
- 이 증분으로 `order_service`의 세 함수 모두 동일한 예외 처리를 갖추게 된다.
