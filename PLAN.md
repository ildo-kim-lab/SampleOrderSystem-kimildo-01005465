# PLAN.md (이번 증분)

## 목표
생산 큐(ProductionQueue)에 대기 중인 주문들을 JSON 파일로 저장할 수 있다.

## 검증할 동작
`save_production_queue(queue, filepath)`를 호출하면, 큐에 있는 각 주문의
필드(시료 ID/고객명/수량/상태)가 FIFO 순서 그대로 JSON 배열로 저장된다.

## 근거
- `docs/PRD.md` 5.8 데이터 영속성 — 생산 큐 데이터도 저장 대상

## 범위 외
- 생산 큐 로드(복원), `run_app`과의 실제 연동은 다음 증분들에서 다룬다.
