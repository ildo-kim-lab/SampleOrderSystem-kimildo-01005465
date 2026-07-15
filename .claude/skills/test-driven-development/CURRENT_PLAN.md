# CURRENT_PLAN.md (이번 증분, 순수 리팩터링)

## 목표
`complete_production_console`이 `complete_next_production_console`로
완전히 대체되어 어디서도 호출되지 않는 죽은 코드가 되었으므로 제거한다.

## 검증할 동작
새로운 외부 동작 변화는 없다 — 삭제 대상 함수를 참조하는 프로덕션
코드가 없음을 확인한 뒤 제거하고, 전체 테스트가 계속 GREEN임을
확인한다.

## 근거
- Clean Code 리뷰(2차) finding 3: `complete_production_console`은
  `console/app.py` 어디에서도 import/호출되지 않는다 (grep으로 확인,
  호출부는 자기 자신의 테스트뿐).

## 범위 외
- 없음. 순수 리팩터링이므로 RED 단계 없이 진행한다.
