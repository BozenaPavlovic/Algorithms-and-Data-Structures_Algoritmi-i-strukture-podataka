# ==============================================================================
# ZADATAK 2: Rekurzivno preokretanje
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju preokreni koja preokreće Python listu.
#
# PRIMJER:
# >>> preokreni([1, 2, 3])
# => [3, 2, 1]
# ==============================================================================

def preokreni(lista):
    # Bazni slučaj: ako je lista prazna ili ima jedan element, već je preokrenuta
    if len(lista) <= 1:
        return lista
    # Rekurzivni korak: uzmi zadnji element i na njega nadodaj preokrenut ostatak liste
    return [lista[-1]] + preokreni(lista[:-1])
