# PLAN.md (이번 증분)

## 목표
더미 주문 데이터를 한 번에 생성해서, 5가지 주문 상태
(RESERVED/REJECTED/PRODUCING/CONFIRMED/RELEASED)가 모두 포함된 데이터로
모니터링 화면을 바로 테스트할 수 있다.

## 검증할 동작
`generate_dummy_orders(order_registry)`를 호출하면, 5가지 상태를 각각 가진
주문이 최소 하나씩 등록된다.

## 근거
- `docs/PLAN.md` Phase 2 — Dummy Data Generator: 여러 상태의 주문을 미리 채움

## 범위 외
- 콘솔 메뉴 연결(더미 데이터 생성 메뉴 항목 추가)은 다음 증분에서 다룬다.
