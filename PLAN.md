# PLAN.md (이번 증분)

## 목표
생산 라인이 실 생산량에 대해 소요될 총 생산 시간을 계산할 수 있다.

## 검증할 동작
`calculate_total_production_time(avg_production_time, production_quantity)`는
`avg_production_time * production_quantity` 값을 반환한다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 총 생산 시간: 평균 생산 시간 * 실 생산량

## 범위 외
- 생산 큐(FIFO), 생산 완료 시 상태 전이는 다음 증분에서 다룬다.
