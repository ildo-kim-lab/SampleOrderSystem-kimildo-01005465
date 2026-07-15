# CURRENT_PLAN.md (이번 증분)

## 목표 (CleanCode, 순수 리팩터링)
`SampleRegistry`의 내부 저장소를 리스트(선형 탐색)에서 `sample_id`를 키로
하는 딕셔너리로 바꿔, `find_by_id`/`register`의 중복 체크를 O(1)로
만든다. (Clean Code 리뷰 finding 5)

## 검증할 동작
새로운 외부 동작 변화는 없다 — 기존 `tests/domain/test_sample.py`의 모든
테스트(get_all 순서 포함)가 리팩터링 전후 모두 그대로 통과해야 한다.
Python 3.7+ 딕셔너리는 삽입 순서를 보존하므로 `get_all()`의 순서도
유지된다.

## 근거
- Clean Code 리뷰 finding 5: `find_by_id`가 리스트를 선형 탐색하고,
  `register`가 매 등록마다 `find_by_id`로 중복 체크를 하여
  `persistence.load_samples`처럼 N개를 반복 등록하는 경로가 O(N²)이 된다.

## 범위 외
- `OrderRegistry`의 동일한 개선은 다루지 않는다(이번 finding은 SampleRegistry
  한정). 순수 리팩터링이므로 RED 단계 없이 진행하고, 리팩터링 전후 테스트가
  계속 GREEN임을 확인한다.
