# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
`monitoring_controller.py`의 `_INACTIVE_STATUSES`가 `domain/order.py`의
`_TERMINAL_STATUSES`와 동일한 두 상태(REJECTED, RELEASED)를 별도 이름으로
재정의하던 것을 없앤다. `order.py`의 상수를 공개(`TERMINAL_STATUSES`)로
바꿔 export하고, `monitoring_controller.py`가 이를 재사용하도록 한다.
(Clean Code 리뷰 finding 6)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 `tests/console/test_monitoring_controller.py`
테스트가 리팩터링 전후 모두 그대로 통과해야 한다.

## 근거
- Clean Code 리뷰 finding 6: 같은 두 상태가 서로 다른 모듈에 중복 정의돼
  있어, 종료 상태가 하나 더 생기면(예: CANCELLED) 도메인 규칙과 모니터링
  쪽을 각각 갱신해야 하고 하나만 고치면 재고 수요 계산이 조용히 틀어진다.

## 범위 외
- 없음 (이 증분으로 finding 6이 마무리된다). 순수 리팩터링이므로 RED 단계
  없이 진행하고, 리팩터링 전후 테스트가 계속 GREEN임을 확인한다.
