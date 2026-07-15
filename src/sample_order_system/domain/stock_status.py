def determine_stock_status(stock: int, demand: int) -> str:
    if stock == 0:
        return "고갈"
    if stock < demand:
        return "부족"
    return "여유"
