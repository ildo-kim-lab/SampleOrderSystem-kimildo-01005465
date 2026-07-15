# PLAN.md (이번 증분)

## 목표
JSON 파일에서 생산 큐 데이터를 읽어와 `ProductionQueue`를 FIFO 순서 그대로
복원할 수 있다.

## 검증할 동작
`load_production_queue(filepath)`는 `save_production_queue`가 저장한 JSON
파일을 읽어, 동일한 순서로 주문이 채워진 `ProductionQueue`를 반환한다.

## 근거
- `docs/PRD.md` 5.8 데이터 영속성

## 범위 외
- `run_app`/`start_app`과의 실제 연동은 다음 증분에서 다룬다.
