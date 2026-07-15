# CURRENT_PLAN.md (이번 증분)

## 목표 (버그 수정)
더미 데이터 생성("9")을 두 번 누르면 앱이 크래시하는 문제를 고친다.
`generate_dummy_samples`가 이미 등록된 고정 ID(S-001 등)를 다시
등록하려다 `SampleRegistry.register()`의 중복 체크에 걸려 `ValueError`가
그대로 튀어나오던 것을, 이미 등록된 시료는 건너뛰도록(멱등하게) 고친다.

## 검증할 동작
`generate_dummy_samples(registry)`를 같은 registry에 대해 두 번 호출해도
예외가 발생하지 않고, 시료 개수는 여전히 3개(중복 없이)로 유지된다.

## 근거
- 사용자가 직접 실행해보고 발견한 크래시 버그: "9"를 두 번 누르면
  `ValueError: 이미 등록된 시료 ID입니다: S-001`가 그대로 튀어나와
  프로그램이 죽음.

## 범위 외
- `generate_dummy_orders`는 주문에 고유 ID 제약이 없어(같은 고객/시료로
  여러 주문 가능) 재호출해도 크래시하지 않으므로 이번 증분에서 다루지
  않는다.
