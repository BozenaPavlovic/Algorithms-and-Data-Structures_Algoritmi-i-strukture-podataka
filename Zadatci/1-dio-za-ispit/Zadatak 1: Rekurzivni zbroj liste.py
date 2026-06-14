# ==============================================================================
# ZADATAK 1: Rekurzivni zbroj
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju zbroj koja vraća zbroj svih vrijednosti 
# u Python listi (koja sadrži samo brojeve).
#
# PRIMJER:
# >>> zbroj([1, 2, 3])
# => 6
# ==============================================================================

def zbroj(lista):
    # Bazni slučaj: ako je lista prazna, zbroj je 0
    if not lista:
        return 0
    # Rekurzivni korak: uzmi prvi element i zbroji ga s ostatkom liste
    return lista[0] + zbroj(lista[1:])
