# CURRENT_PLAN.md (이번 증분)

## 목표 (Harness 3계층 — 콘솔 E2E 스모크 검증)
`CLAUDE.md`에 설계해둔 테스트/검증 Harness의 3번째 계층(콘솔 E2E 스모크
검증)을 실제로 구현한다. `python -m sample_order_system`을 서브프로세스로
실행하고 입력 시퀀스를 흘려보내, 더미 데이터 생성 → 시료 조회 → 종료 시
저장까지의 흐름이 실제로 동작하는지 자동으로 확인한다.

## 검증할 동작
`tests/test_console_smoke.py`의 새 테스트가, 실제 `python -m
sample_order_system` 프로세스를 tmp_path를 작업 디렉터리로 실행해서:
1. 더미 데이터 생성("9") 후 출력에 등록된 더미 시료 이름이 보이는지
2. 종료("0") 후 `samples.json`/`orders.json`/`queue.json`이 tmp_path에
   실제로 생성되는지
를 확인한다.

## 근거
- `CLAUDE.md` "테스트/검증 Harness 설계" — 3계층 중 "콘솔 E2E 스모크 검증"이
  설계만 되어 있고 구현되지 않았던 부분.

## 범위 외
- `/verify` 스킬 등록(매 Phase 종료 시 동일 명령 재현)은 다음 증분에서
  다룬다.
