# ==============================================================================
# ZADATAK 5: Rekurzivno množenje (3 boda)
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju mnozenje(m, n) koja vraća umnožak dva prirodna 
# broja m i n, ali samo korištenjem operacija zbrajanja i oduzimanja.
#
# PRIMJER:
# >>> mnozenje(3, 4)
# => 12
# ==============================================================================

def mnozenje(m, n):
    # Bazni slučaj: bilo koji broj pomnožen s 0 daje 0
    if n == 0:
        return 0
    # Rekurzivni korak: dodajemo m na zbroj, a n smanjujemo za 1 prema nuli
    return m + mnozenje(m, n - 1)
