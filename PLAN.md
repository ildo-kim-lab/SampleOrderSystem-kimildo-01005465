# PLAN.md (이번 증분)

## 목표
콘솔에서 CONFIRMED 상태 주문에 대해 출고를 실행하면 RELEASED로 전환되고,
재고가 차감되며, 결과가 출력된다.

## 검증할 동작
`release_order_console(order, sample_registry, output_func)`를 호출하면
`order_service.release_order`를 통해 주문이 RELEASED로 전환되고 재고가
차감되며, 결과가 `output_func`로 출력된다.

## 근거
- `docs/PRD.md` 5.7 출고 처리

## 범위 외
- CONFIRMED 주문 목록에서 특정 주문을 선택하는 콘솔 입력/라우팅은 다음 증분에서
  다룬다.
