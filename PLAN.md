# PLAN.md (이번 증분)

## 목표
주문을 출고 처리하면, 해당 시료의 재고가 주문 수량만큼 차감되고
주문 상태는 RELEASED로 전환된다.

## 검증할 동작
`release_order(order, registry)`를 호출하면 `order.status`가 `RELEASED`가 되고,
`order.sample_id`에 해당하는 시료의 `stock`이 `order.quantity`만큼 줄어든다.

## 근거
- `docs/PRD.md` 5.7 출고 처리 — CONFIRMED 상태 주문에 대해 출고 실행, 실행 시
  상태 CONFIRMED → RELEASED
- `docs/PRD.md` 3. 용어집 — 재고(Stock): 출고 가능한 보유 수량 (출고 시 감소)

## 범위 외
- 생산 완료 시 재고 증가 연동은 다음 증분에서 다룬다.
- 시료를 찾지 못했을 때의 예외 처리는 이전 증분과 동일하게 범위 외.
