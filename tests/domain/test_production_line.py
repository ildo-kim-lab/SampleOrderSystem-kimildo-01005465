from sample_order_system.domain.production_line import (
    calculate_production_quantity,
    calculate_total_production_time,
)


def test_calculate_production_quantity_rounds_up_by_yield_rate():
    result = calculate_production_quantity(shortage=10, yield_rate=0.9)

    assert result == 12


def test_calculate_total_production_time_multiplies_avg_time_by_quantity():
    result = calculate_total_production_time(
        avg_production_time=2.5, production_quantity=12
    )

    assert result == 30.0
