# PLAN.md (이번 증분)

## 목표
콘솔에서 접수된 주문을 거절하면 즉시 REJECTED 상태로 전환되고, 결과가
출력된다.

## 검증할 동작
`reject_order_console(order, output_func)`를 호출하면 `order.status`가
`REJECTED`가 되고, 그 결과가 `output_func`로 출력된다.

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — 주문거절: 즉시 REJECTED 상태로 전환

## 범위 외
- 접수된 주문 목록에서 특정 주문을 선택하는 콘솔 입력/라우팅은 다음 증분에서 다룬다.
