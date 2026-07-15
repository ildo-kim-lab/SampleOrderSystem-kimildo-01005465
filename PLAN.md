# PLAN.md (이번 증분)

## 목표
JSON 파일에서 주문 목록을 읽어와 `OrderRegistry`를 복원할 수 있다
(상태 문자열을 `OrderStatus`로 복원).

## 검증할 동작
`load_orders(filepath)`는 `save_orders`가 저장한 JSON 파일을 읽어, 동일한
필드와 상태를 가진 주문들이 등록된 `OrderRegistry`를 반환한다.

## 근거
- `docs/PRD.md` 5.8 데이터 영속성

## 범위 외
- 파일이 없을 때의 처리, 프로그램 시작/종료 시점과의 실제 연동은 다음
  증분들에서 다룬다.
