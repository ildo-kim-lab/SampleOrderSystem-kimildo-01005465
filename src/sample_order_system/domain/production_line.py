import math


def calculate_production_quantity(shortage: int, yield_rate: float) -> int:
    return math.ceil(shortage / yield_rate)
