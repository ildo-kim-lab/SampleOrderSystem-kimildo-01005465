---
name: verify
description: SampleOrderSystem 콘솔 앱을 실제로 빌드/실행/구동해서 변경 사항을 검증하는 절차
---

# SampleOrderSystem 검증 (Verify)

이 프로젝트는 순수 콘솔(REPL) 앱이다. 표면(surface)은 **터미널**이며,
`input()`/`print()`를 통해 사용자와 상호작용한다. 검증은 반드시 실제로
이 프로세스를 띄워서 관찰해야 하며, `pytest`만 돌리는 것은 검증이 아니다
(그건 CI가 하는 일이다).

## 빌드 / 실행

저장소 루트의 `main.py`가 `src`를 `sys.path`에 넣어주는 얇은 래퍼이므로,
`PYTHONPATH` 없이 그냥 실행하면 된다. 한글 출력이 깨지지 않도록
`PYTHONIOENCODING=utf-8`은 설정해두는 게 안전하다 (환경에 따라 없어도
되는 경우도 있음).

```bash
# 저장소 루트에서 (권장)
PYTHONIOENCODING=utf-8 python main.py

# 또는 (PYTHONPATH=src를 직접 지정해야 함)
PYTHONPATH=src PYTHONIOENCODING=utf-8 python -m sample_order_system
```

PyCharm 등 IDE에서는 `main.py`를 그냥 우클릭 → Run 하면 된다 (Working
directory가 기본값인 프로젝트 루트로 잡히므로 별도 설정 불필요).

앱은 현재 작업 디렉터리에 `samples.json`/`orders.json`/`queue.json`을
저장·복원한다. **검증용으로 실행할 때는 반복 실행으로 지저분해지지
않도록 임시 디렉터리에서 실행하거나, 끝나고 이 세 파일을 지운다.**

```bash
rm -f samples.json orders.json queue.json   # 검증 후 정리
```

## 구동 (드라이브)

메뉴는 매번 다음과 같이 출력된다:

```
===== SampleOrderSystem =====
1. 시료관리
2. 주문(접수/승인/거절)
3. 모니터링
4. 출고 처리
5. 생산 라인
9. 더미 데이터 생성
0. 종료

선택:
```

손으로 입력을 타이핑하는 대신, heredoc으로 입력 시퀀스를 한 번에
흘려보내는 방식이 가장 재현하기 쉽다 (Bash 도구에서 `printf '...\n' |`
파이프는 이 환경에서 한글이 깨져 보일 수 있으니 **heredoc(`<<'EOF'`)을
사용할 것** — 실제 바이트는 정상이지만 표시가 지저분해서 확인이 어렵다).

### 자주 쓰는 시나리오

**더미 데이터로 전체 주문 흐름 (접수→승인→출고) 확인:**

```bash
PYTHONIOENCODING=utf-8 python main.py <<'EOF'
9
2
1
S-100
LiveCustomer
5
2
1
0
4
1
0
EOF
```
(9=더미 데이터, 2=주문메뉴, 1=접수, ...주문 입력..., 2=승인, 1번 선택,
0=주문메뉴에서 뒤로가기, 4=출고 처리, 1번 선택, 0=종료)

**시료 등록 + 조회 확인:**

```bash
PYTHONIOENCODING=utf-8 python main.py <<'EOF'
1
1
S-001
Wafer-A
2.5
0.9
2
0
0
EOF
```
(1=시료관리, 1=등록, ...입력..., 2=조회, 0=뒤로가기, 0=종료)

## 저장 파일 확인

종료 후 `cat samples.json` / `cat orders.json` / `cat queue.json`으로
실제 저장된 상태(재고 차감, 주문 상태 전이)가 기대한 대로인지 확인한다.
`orders.json`의 `status` 필드가 RESERVED/REJECTED/PRODUCING/CONFIRMED/
RELEASED 중 기대한 값인지가 핵심 확인 포인트다.

## 자동화된 회귀 방지 (참고)

`tests/test_console_smoke.py`가 이 구동 절차와 동일한 시나리오를
subprocess로 자동 실행해서 pytest로 확인한다 (`pytest
tests/test_console_smoke.py -v`). 이 파일은 회귀 방지용 자동 테스트이며,
사람이 직접 구동해서 눈으로 확인하는 이 SKILL의 절차를 대체하지는
않는다 — 새 기능을 검증할 때는 여전히 위 방식으로 직접 구동해서
관찰할 것.

## 알게 된 것 (Gotchas)

- `python -m sample_order_system`은 저장소 루트가 아닌 다른 디렉터리에서
  실행하면 `ModuleNotFoundError`가 난다 (PYTHONPATH가 `src`를 상대경로로
  가리키기 때문). `python main.py`는 스크립트 자신의 위치 기준으로
  `src`를 찾으므로 이 문제가 없다.
- 잘못된 메인 메뉴 번호("99" 등)는 "잘못된 선택입니다"만 출력하고
  루프를 계속한다 (크래시 없음).
- 숫자 입력란에 문자를 넣으면(`avg_production_time`, `주문 수량` 등)
  "숫자 형식이 올바르지 않습니다"로 안내하고 해당 입력을 취소한다
  (크래시 없음).
- 승인/거절/출고 대상 주문이 하나도 없을 때 번호를 입력하라고 하지
  않고 "대상 주문이 없습니다"만 출력하고 메뉴로 돌아간다.
