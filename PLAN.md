# PLAN.md (이번 증분)

## 목표
프로그램 종료("0") 시 현재 시료/주문 데이터를 지정된 파일에 자동으로
저장한다.

## 검증할 동작
`run_app(state, input_func, output_func, sample_filepath, order_filepath)`에서
"0"을 입력해 종료하면, 두 파일에 현재 상태가 저장된다.

## 근거
- `docs/PRD.md` 5.8 데이터 영속성 — 프로그램 종료 시 저장

## 범위 외
- 프로그램 시작 시 로드하는 것은 다음 증분에서 다룬다.
