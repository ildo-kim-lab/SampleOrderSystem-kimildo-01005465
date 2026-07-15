# PLAN.md (이번 증분)

## 목표
생산 라인의 대기열(생산 큐)은 등록된 순서대로(FIFO) 주문을 처리한다.

## 검증할 동작
`ProductionQueue`에 주문 A, B를 순서대로 `enqueue()`하면, `dequeue()`는
A를 먼저 반환한다.

## 근거
- `docs/PRD.md` 5.6 생산 라인 — 대기 주문 확인: 생산 큐(FIFO)의 대기 목록
- `docs/PRD.md` 3. 용어집 — 생산 큐: PRODUCING 상태 주문이 대기하는 FIFO 큐

## 범위 외
- 큐와 주문 승인(approve)/생산 완료(complete_production) 로직의 연동,
  생산 현황 표기는 다음 증분에서 다룬다.
