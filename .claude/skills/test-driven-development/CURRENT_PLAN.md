# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
`persistence.py`의 save_samples/load_samples, save_orders/load_orders,
save_production_queue/load_production_queue 3쌍이 반복하던 "리스트 생성 →
json.dumps → write_text" / "read_text → json.loads → 루프 register"
골격을, 공용 제네릭 헬퍼(`save_json_list`/`load_json_list`)로 통일한다.
(Clean Code 리뷰 finding 4)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 `tests/test_persistence.py`의 6개
테스트(save/load × samples/orders/production_queue)가 리팩터링 전후 모두
그대로 통과해야 한다.

## 근거
- Clean Code 리뷰 finding 4: 3쌍이 구조적으로 거의 동일한데 손으로 반복
  작성되어 있어, 공통 관심사(원자적 쓰기, 손상된 JSON 처리 등)를 고치려면
  6곳을 모두 손으로 고쳐야 하는 유지보수 비용이 있었다.

## 범위 외
- 없음 (이 증분으로 finding 4가 마무리된다). 순수 리팩터링이므로 RED 단계
  없이 진행하고, 리팩터링 전후 테스트가 계속 GREEN임을 확인한다.
