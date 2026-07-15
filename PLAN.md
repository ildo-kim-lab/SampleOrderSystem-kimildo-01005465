# PLAN.md (이번 증분)

## 목표
콘솔에서 접수된(RESERVED) 주문 중 하나를 골라 승인 또는 거절할 수 있다.
승인 시 재고 상황(SampleRegistry)에 따라 CONFIRMED/PRODUCING이 자동으로
결정된다.

## 검증할 동작
`approve_order_console(order, sample_registry, output_func)`를 호출하면
`order_service.approve_order`를 통해 실제 재고를 반영한 승인이 이뤄지고,
결과 상태가 `output_func`로 출력된다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절

## 범위 외
- 접수된 주문 목록에서 특정 주문을 선택하는 콘솔 입력/라우팅, 거절 콘솔 핸들러는
  다음 증분에서 다룬다.
