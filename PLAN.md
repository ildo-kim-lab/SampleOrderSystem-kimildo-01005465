# PLAN.md (이번 증분)

## 목표
주문을 승인할 때, 주문에 명시된 시료의 실제 재고(SampleRegistry 조회 결과)를
기준으로 승인 로직(CONFIRMED/PRODUCING 분기)이 동작한다.

## 검증할 동작
`approve_order(order, registry)`를 호출하면, `order.sample_id`에 해당하는
시료를 `registry`에서 찾아 그 `stock`을 `Order.approve()`에 전달한다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 승인시 재고 상황에 따라 자동으로 처리

## 범위 외
- 출고 시 재고 차감, 생산 완료 시 재고 증가 연동은 다음 증분에서 다룬다.
- 시료를 찾지 못했을 때의 예외 처리는 다음 증분에서 다룬다.
