import math


def calculate_production_quantity(shortage: int, yield_rate: float) -> int:
    return math.ceil(shortage / yield_rate)


def calculate_total_production_time(
    avg_production_time: float, production_quantity: int
) -> float:
    return avg_production_time * production_quantity
