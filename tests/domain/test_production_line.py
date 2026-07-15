from sample_order_system.domain.production_line import calculate_production_quantity


def test_calculate_production_quantity_rounds_up_by_yield_rate():
    result = calculate_production_quantity(shortage=10, yield_rate=0.9)

    assert result == 12
