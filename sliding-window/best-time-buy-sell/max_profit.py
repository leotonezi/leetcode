# Brute force
def max_profit(self, prices):
    sorted_array = sorted(prices)
    min_value = sorted_array[0]

    day_buy = 0
    day_sell = 0
    max_value = 0
    for i, x in enumerate(prices):
        if x == min_value:
            day_buy = i
        if max_value < x and i > day_buy:
            max_value = x
            day_sell = i

    if day_buy > day_sell:
        return 0

    return max_value - min_value


# Great solution
def max_profit_best(self, prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Calculate profit if we sell today
        max_profit = max(max_profit, price - min_price)

    return max_profit
