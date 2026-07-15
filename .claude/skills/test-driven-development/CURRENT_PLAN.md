# CURRENT_PLAN.md (이번 증분)

## 목표 (기능 누락 수정)
주문 승인 시 재고가 부족해 PRODUCING으로 전환되면, 해당 주문이 실제로
생산 큐(ProductionQueue)에 등록되도록 한다.

## 검증할 동작
`approve_order(order, sample_registry, production_queue)`를 재고가
부족한 상황에서 호출하면, `order.status`가 `PRODUCING`이 되고 동시에
`production_queue`에 그 주문이 들어간다 (`production_queue.dequeue()`로
꺼내면 같은 주문 객체가 나온다).

## 근거
- `docs/PRD.md` 5.4 주문 승인/거절 — "재고가 부족한 경우: 생산 라인에
  자동으로 등록, 주문 상태를 PRODUCING으로 전환"
- 점검 중 발견한 기능 누락: `order_service.approve_order`는 상태만
  PRODUCING으로 바꿀 뿐 `ProductionQueue.enqueue()`를 호출하지 않아서,
  "생산 라인" 메뉴의 "대기 주문 확인"이 실제 플레이에서 항상 비어 있었다.

## 범위 외
- 생산 완료 처리를 실행할 메뉴가 없는 문제(발견 목록 4번)는 이어지는
  별도 증분에서 다룬다. 이번 증분은 "큐에 등록되는 것"까지만 다룬다.
