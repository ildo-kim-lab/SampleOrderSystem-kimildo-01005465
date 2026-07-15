# CURRENT_PLAN.md (이번 증분)

## 목표 (기능 누락 수정)
생산 큐에서 대기 중인 주문을 꺼내 생산 완료 처리하는 콘솔 핸들러
(`complete_next_production_console`)를 만든다. 생산 큐는 FIFO이므로
항상 맨 앞(가장 먼저 등록된) 주문을 꺼내 처리한다.

## 검증할 동작
`complete_next_production_console(production_queue, sample_registry,
output_func)`를 호출하면:
1. 큐가 비어있지 않으면 맨 앞 주문을 꺼내 `complete_order_production`으로
   생산 완료 처리(PRODUCING → CONFIRMED, 재고 증가)하고 결과를 출력한다.
2. 큐가 비어있으면 안내 메시지를 출력하고 아무 것도 하지 않는다.

## 근거
- 점검 중 발견한 기능 누락(발견 목록 4번): `complete_order_production`
  함수 자체는 있고 단위 테스트도 있지만, 어떤 메뉴에서도 호출되지 않아
  PRODUCING 상태 주문이 영원히 CONFIRMED로 못 넘어감.
- `docs/PRD.md` 5.6 생산 라인 — "대기 주문 확인: 생산 큐의 대기열...
  스케쥴링은 FIFO로 진행"

## 범위 외
- 이 함수를 "생산 라인" 메인 메뉴에 실제로 연결하는 것(하위 메뉴로
  전환)은 다음 증분에서 다룬다.
