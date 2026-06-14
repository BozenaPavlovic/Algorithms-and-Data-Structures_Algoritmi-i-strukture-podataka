def maxProfit(prices: list[int]) -> int:
    # Ako niz ima manje od 2 elementa, ne možemo kupiti i prodati
    if len(prices) < 2:
        return 0

    # Inicijaliziramo najnižu cijenu na prvi dan, a profit na 0
    min_price = prices[0]
    max_profit = 0

    # Prolazimo kroz cijene počevši od drugog dana
    for price in prices[1:]:
        # Ako je današnja cijena manja od dosadašnje najniže, to nam je nova točka kupnje
        if price < min_price:
            min_price = price
        # Inače, računamo potencijalni profit ako bismo prodali danas
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit