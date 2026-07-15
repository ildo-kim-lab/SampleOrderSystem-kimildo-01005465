# PLAN.md (이번 증분)

## 목표 (Phase 4 시작)
등록된 시료 목록을 JSON 파일로 저장할 수 있다.

## 검증할 동작
`save_samples(sample_registry, filepath)`를 호출하면, 등록된 각 시료의
필드(시료 ID/이름/평균 생산시간/수율/재고)가 JSON 배열로 파일에 저장된다.

## 근거
- `docs/PRD.md` 5.8 데이터 영속성 — JSON 파일 저장

## 범위 외
- 주문/생산 큐 저장, 파일 로드(복원)는 다음 증분들에서 다룬다.
