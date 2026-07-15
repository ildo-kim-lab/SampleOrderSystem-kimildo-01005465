# CURRENT_PLAN.md (이번 증분)

## 목표 (버그 수정)
`generate_dummy_orders`도 `generate_dummy_samples`와 마찬가지로 멱등하게
만든다. 이미 생성된 더미 고객(Customer A~E) 이름의 주문이 있으면 다시
등록하지 않는다.

## 검증할 동작
`generate_dummy_orders(registry)`를 같은 registry에 대해 두 번 호출해도
주문 개수는 여전히 5개(중복 없이)로 유지된다.

## 근거
- 점검 중 발견한 실제 버그: "9"(더미 데이터 생성)를 두 번 누르면
  `generate_dummy_orders`가 매번 무조건 5개를 새로 등록해서, 모니터링
  화면의 상태별 주문 수가 전부 2배로 뻥튀기됨 (재현 확인함).
- `generate_dummy_samples`는 이미 같은 방식(중복이면 건너뛰기)으로
  멱등하게 고쳤는데, `generate_dummy_orders`만 비대칭적으로 빠져 있었다.

## 범위 외
- `Order`에 고유 ID가 없어 "이미 생성된 더미 주문"을 판별할 표준적인
  방법이 없다. 이번 증분에서는 고정된 더미 고객명(Customer A~E)이 이미
  등록돼 있는지로 판별하는 실용적인 방법을 쓴다.
