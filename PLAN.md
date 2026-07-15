# PLAN.md (이번 증분)

## 목표
콘솔에서 주문 접수 메뉴를 통해, 사용자가 입력한 값(시료 ID/고객명/주문 수량)으로
새 주문(RESERVED 상태)을 `OrderRegistry`에 등록할 수 있다.

## 검증할 동작
`create_order(order_registry, input_func, output_func)`를 호출하면,
`input_func`가 반환한 값들로 만들어진 `RESERVED` 상태의 주문이
`order_registry`에 등록된다.

## 근거
- `docs/PRD.md` 5.3 시료 주문 (예약) — 입력값: 시료 ID, 고객명, 주문 수량,
  생성 시 상태는 RESERVED

## 범위 외
- 메인 메뉴와의 실제 라우팅 연결, 존재하지 않는 시료 ID에 대한 검증은
  다음 증분에서 다룬다.
