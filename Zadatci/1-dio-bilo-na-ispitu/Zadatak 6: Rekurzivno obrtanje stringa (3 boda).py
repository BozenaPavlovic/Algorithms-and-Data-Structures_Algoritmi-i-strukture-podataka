# ==============================================================================
# ZADATAK 6: Rekurzivno obrtanje stringa (3 boda)
#
# TEKST ZADATKA:
# Napišite rekurzivnu funkciju obrni(s) koja prima niz znakova s i vraća 
# obrnuti niz znakova.
#
# PRIMJER:
# >>> obrni('abcd')
# => 'dcba'
# ==============================================================================

def obrni(s):
    # Bazni slučaj: ako string ima samo 1 znak, on je već obrnut
    if len(s) == 1:
        return s
    # Rekurzivni korak: uzmi zadnji znak i ispred njega spoji rekurzivno izvrnut ostatak stringa
    return s[-1] + obrni(s[0:-1])
