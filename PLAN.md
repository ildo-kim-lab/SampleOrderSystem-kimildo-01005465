# PLAN.md (이번 증분)

## 목표
프로그램 시작 시 저장된 파일이 있으면 이를 로드해서 이전 상태로 이어서
시작하고, 파일이 없으면 빈 상태로 시작한다.

## 검증할 동작
`start_app(sample_filepath, order_filepath, input_func, output_func)`는
파일이 존재하면 그 내용으로 채워진 `AppState`를 사용해 `run_app`을 실행하고,
파일이 없으면 빈 `AppState`로 시작한다 (오류 없이).

## 근거
- `docs/PRD.md` 5.8 데이터 영속성 — 프로그램 시작 시 저장 파일 로드,
  없으면 빈 상태로 시작

## 범위 외
- 콘솔 스크립트 진입점(`__main__`) 연결은 다음 증분에서 다룬다.
