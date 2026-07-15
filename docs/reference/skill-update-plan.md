agentic-tdd 를 설명하겠습니다.
기존 tdd와 다른 점은 아래와 같아요.
RED단계에서 Plan.md를 생성해서, 인간에게 검수를 받는다
검수 후 commit 여부를 문의한다.
GREEN단계에서는 생성된 goal이 달성이 되도록 구현하고, 테스트를 실제 통과하도록 체크한다
GREEN단계 이후 REVIEW 단계를 수행한다
REVIEW는 인간이 수행하며, GREEN단계의 코드 수정, Plan외의 구현, Refactoring 필요 여부를 확인한다
REVIEW 후 commit 여부를 문의한다.