# PLAN.md (이번 증분)

## 목표
`python -m sample_order_system`으로 실제 콘솔 프로그램을 실행할 수 있다
(실제 `input()`/`print()`와 고정 저장 파일 경로를 사용).

## 검증할 동작
`main()` 함수는 실제 `input`/`print`를 `start_app`에 연결해서 호출한다.
단위 테스트에서는 `input`/`print`를 대체(monkeypatch)해서 `main()`이
`start_app`을 올바른 인자로 호출하는지 확인한다.

## 근거
- `docs/PRD.md` 1. 배경 및 목적 — 콘솔 기반으로 동작

## 범위 외
- 저장 파일 경로를 사용자가 지정하는 옵션(커맨드라인 인자 등)은 다루지 않는다.
