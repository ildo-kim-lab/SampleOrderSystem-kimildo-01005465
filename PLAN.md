# PLAN.md (이번 증분)

## 목표
콘솔에서 생산 라인의 생산 완료 처리를 실행하면, 해당 주문이 CONFIRMED로
전환되고 재고가 실 생산량만큼 증가하며, 결과가 출력된다.

## 검증할 동작
`complete_production_console(order, sample_registry, output_func)`를
호출하면 `order_service.complete_order_production`을 통해 주문이
CONFIRMED로 전환되고 재고가 증가하며, 결과가 `output_func`로 출력된다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 생산 완료 시 PRODUCING → CONFIRMED

## 범위 외
- 생산 큐(ProductionQueue)에서 다음 항목을 꺼내는 로직, 생산 현황/대기 큐 표시는
  다음 증분에서 다룬다.
