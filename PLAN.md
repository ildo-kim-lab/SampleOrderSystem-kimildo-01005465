# PLAN.md (이번 증분)

## 목표
콘솔에서 이름으로 시료를 검색할 수 있다.

## 검증할 동작
`search_samples(registry, keyword, output_func)`를 호출하면, 이름에
`keyword`가 포함된 시료만 `output_func`로 출력된다.

## 근거
- `docs/PRD.md` 5.2 시료관리 — 시료 검색: 이름 등 속성으로 특정 시료를 검색

## 범위 외
- 이름 외 다른 속성(ID 등) 검색, 메인 메뉴와의 라우팅 연결은 다음 증분에서 다룬다.
