# PLAN.md (이번 증분)

## 목표
생산 라인이 재고 부족분을 생산할 때, 수율을 고려한 실 생산량을 계산할 수 있다.

## 검증할 동작
`calculate_production_quantity(shortage, yield_rate)`는 `ceil(shortage / yield_rate)`
값을 반환한다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 실 생산량: ceil(부족분/수율)

## 범위 외
- 총 생산 시간 계산, 생산 큐(FIFO), 생산 완료 시 상태 전이는 다음 증분에서 다룬다.
