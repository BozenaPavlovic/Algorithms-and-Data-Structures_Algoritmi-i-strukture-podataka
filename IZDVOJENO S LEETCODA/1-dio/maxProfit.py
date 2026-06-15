# ==============================================================================
# ZADATAK: 121. Best Time to Buy and Sell Stock (Najbolje vrijeme za kupnju i prodaju dionica)
#
# KATEGORIJA: LISTE / KLIZNI PROZOR (Jedan prolaz - linearne složenosti)
#
# TEKST ZADATKA:
# Zadan je niz 'prices' gdje je 'prices[i]' cijena dionice na i-ti dan.
# Želiš maksimizirati svoj profit tako da odabereš JEDAN dan za kupnju dionice i 
# JEDAN DRUGI dan u budućnosti za prodaju te dionice.
# Vrati maksimalni profit koji možeš ostvariti. Ako ne možeš ostvariti profit, vrati 0.
#
# PRIMJER:
# Unos: prices = [7, 1, 5, 3, 6, 4]
# Izlaz: 5
# Objašnjenje: Kupiš 2. dana (cijena = 1), a prodaš 5. dana (cijena = 6). 
# Profit = 6 - 1 = 5. (Uočiti da kupnja na 1 i prodaja na 7 nije dozvoljena jer moraš kupiti prije prodaje).
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Vremenska složenost mora biti O(n), što znači da kroz niz smiješ proći samo JEDNOM.
# Ne smiješ koristiti ugniježđene petlje (for unutar for) jer bi to bilo previše sporo.
# ==============================================================================

def maxProfit(prices):
    # Rubni slučaj: Ako imamo manje od 2 dana, ne možemo kupiti i prodati, profit je 0
    if len(prices) < 2:
        return 0

    # 'min_price' pamti najnižu cijenu na koju smo naišli do sada (kupovna točka)
    min_price = prices[0]
    # 'max_profit' pamti najveću razliku između prodajne i kupovne cijene koju smo vidjeli
    max_profit = 0

    # Prolazimo kroz cijene počevši od drugog dana (indeks 1)
    for price in prices[1:]:
        # Ako je današnja cijena manja od našeg dosadašnjeg minimuma,
        # ažuriramo 'min_price' jer je ovo bolji dan za kupnju u budućnosti
        if price < min_price:
            min_price = price  
            
        # Inače, ako je današnja cijena veća, provjeravamo koliki bismo profit ostvarili 
        # da smo kupili po 'min_price', a prodali danas ('price').
        # Ako je taj profit veći od dosadašnjeg maksimalnog, ažuriramo 'max_profit'.
        elif price - min_price > max_profit:
            max_profit = price - min_price  

    # Vraćamo najveći mogući ostvareni profit
    return max_profit
