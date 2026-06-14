def maxProfit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price  # Našli smo novu najnižu točku za kupnju
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Našli smo bolji profit

    return max_profit