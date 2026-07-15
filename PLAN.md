# PLAN.md (이번 증분)

## 목표
JSON 파일에서 시료 목록을 읽어와 `SampleRegistry`를 복원할 수 있다.

## 검증할 동작
`load_samples(filepath)`는 `save_samples`가 저장한 JSON 파일을 읽어,
동일한 필드를 가진 시료들이 등록된 `SampleRegistry`를 반환한다.

## 근거
- `docs/PRD.md` 5.8 데이터 영속성 — 프로그램 시작 시 저장된 파일 로드

## 범위 외
- 파일이 없을 때의 처리, 주문/생산 큐 로드는 다음 증분들에서 다룬다.
