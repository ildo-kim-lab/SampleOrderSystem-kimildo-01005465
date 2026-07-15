# PLAN.md (이번 증분)

## 목표
콘솔에서 시료별 재고 수량과 주문 대비 상태(여유/부족/고갈)를 확인할 수 있다.
수요는 아직 출고되지 않은(RELEASED/REJECTED가 아닌) 주문 수량의 합으로 계산한다.

## 검증할 동작
`monitor_stock_levels(sample_registry, order_registry, output_func)`를
호출하면, 각 시료의 이름과 `determine_stock_status(stock, demand)` 결과가
`output_func`로 출력된다.

## 근거
- `docs/PRD.md` 5.5 모니터링 — 재고량확인: 시료별 현재 재고 수량, 주문대비
  재고 수량에 따른 상태(여유/부족/고갈) 표기

## 범위 외
- 생산 라인 현황/대기 큐 표시는 다음 증분에서 다룬다.
