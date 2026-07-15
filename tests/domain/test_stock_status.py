import pytest

from sample_order_system.domain.stock_status import determine_stock_status


@pytest.mark.parametrize(
    "stock,demand,expected",
    [
        (0, 10, "고갈"),
        (5, 10, "부족"),
        (10, 10, "여유"),
        (20, 10, "여유"),
    ],
)
def test_determine_stock_status(stock, demand, expected):
    assert determine_stock_status(stock, demand) == expected
