# ==============================================================================
# ZADATAK 3: Rekurzivni palindrom
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju palindrom koja vraća True ako je zadani 
# string palindrom (isti s lijeva i zdesna), u suprotnom vraća False.
#
# PRIMJER:
# >>> palindrom('abcba')
# => True
# ==============================================================================

def palindrom(string):
    # Bazni slučaj: ako string ima 0 ili 1 znak, onda je sigurno palindrom
    if len(string) <= 1:
        return True
    # Ako se prvi i zadnji znak ne podudaraju, odmah znamo da nije palindrom
    if string[0] != string[-1]:
        return False
    # Rekurzivni korak: provjeri unutrašnjost stringa (bez prvog i zadnjeg znaka)
    return palindrom(string[1:-1])
