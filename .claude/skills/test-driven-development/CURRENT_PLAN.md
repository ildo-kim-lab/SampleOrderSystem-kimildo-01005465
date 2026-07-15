# CURRENT_PLAN.md (이번 증분)

## 목표 (버그 수정)
주문 승인/거절/출고 처리에서 번호 입력란에 숫자가 아닌 값을 넣으면
크래시하는 문제를 고친다. `_select_order_by_status`의
`int(input_func(prompt))` 파싱에 예외 처리가 빠져 있었다.

## 검증할 동작
`_select_order_by_status`를 호출한 상태에서 번호 입력으로 숫자가 아닌
문자열("abc")을 주면, `ValueError`가 그대로 튀어나오지 않고 "숫자 형식이
올바르지 않습니다" 같은 안내 메시지가 출력되며 `None`을 반환한다.

## 근거
- 사용자가 직접 실행해보고 발견한 크래시 버그: 승인할 번호에 "abc"를
  입력하면 `ValueError: invalid literal for int()`가 그대로 튀어나와
  프로그램이 죽음. `register_sample`/`create_order`의 숫자 입력값은 이미
  같은 방식으로 보호돼 있었는데, 이 함수만 빠져 있었다.

## 범위 외
- 없음.
