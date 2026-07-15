# PLAN.md (이번 증분)

## 목표
콘솔에서 시료 등록 메뉴를 통해, 사용자가 입력한 값(시료 ID/이름/평균
생산시간/수율)으로 새 시료를 `SampleRegistry`에 등록할 수 있다.

## 검증할 동작
`register_sample(registry, input_func, output_func)`를 호출하면,
`input_func`가 반환한 값들로 만들어진 시료가 `registry`에 등록된다.
`input_func`/`output_func`는 콘솔 I/O 경계를 테스트에서 대체하기 위한
주입점이다 (`CLAUDE.md`: mock은 외부 경계에서만).

## 근거
- `docs/PRD.md` 5.2 시료관리 — 시료 등록: 입력값 시료 ID, 이름, 평균 생산시간, 수율

## 범위 외
- 메인 메뉴와의 실제 라우팅 연결, 입력값 형식 오류 처리(숫자가 아닌 값 등)는
  다음 증분에서 다룬다.
