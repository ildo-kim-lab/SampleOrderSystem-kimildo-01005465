# PLAN.md (이번 증분)

## 목표
콘솔에서 상태별(RESERVED/CONFIRMED/PRODUCING/RELEASED) 주문 수를 확인할 수
있다. REJECTED는 집계에서 제외한다.

## 검증할 동작
`monitor_order_counts(order_registry, output_func)`를 호출하면 RESERVED,
CONFIRMED, PRODUCING, RELEASED 각각의 개수가 출력되고, REJECTED 개수는
출력되지 않는다.

## 근거
- `docs/PRD.md` 5.5 모니터링 — 주문량확인: 상태별 목록 확인, REJECTED는
  유효한 주문이 아니므로 무시

## 범위 외
- 재고량 확인(여유/부족/고갈 표기), 생산 라인 현황 표기는 다음 증분에서 다룬다.
