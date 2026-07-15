# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
`persistence._dict_to_order`와 `console/dummy_data.generate_dummy_orders`가
`order.status = X`로 생성 후 상태 필드를 직접 대입하던 것을, `Order(...,
status=X)` 생성자 인자로 바꾼다. (Clean Code 리뷰 finding 2)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 테스트(`test_load_orders_restores_...`,
`test_generate_dummy_orders_covers_all_five_statuses` 등)가 리팩터링 전후
모두 그대로 통과해야 한다. Order는 이미 `status` 필드를 생성자 인자로
받으므로 별도 메서드 추가 없이 대입 방식만 바꾼다.

## 근거
- `CLAUDE.md`: "주문 상태 전이는 반드시 하나의 함수/클래스(상태 머신)를
  통해서만 이루어져야 한다." 생성 이후 상태 필드를 직접 덮어쓰는 대신,
  생성 시점에 상태를 지정하는 방식으로 전이 메서드 우회를 없앤다.

## 범위 외
- 없음 (이 증분으로 finding 2가 마무리된다). 순수 리팩터링이므로 RED 단계
  없이 진행하고, 리팩터링 전후 테스트가 계속 GREEN임을 확인한다.
