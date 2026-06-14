# ==============================================================================
# ZADATAK: 50. Pow(x, n) (Rekurzivno - Divide & Conquer)
#
# TEKST ZADATKA:
# Implementirajte funkciju koja izračunava x potencirano na eksponent n (x^n).
# Zadatak je potrebno riješiti efikasno, s vremenskom složenošću O(log n).
#
# PRIMJER:
# Unos: x = 2.00000, n = 10
# Izlaz: 1024.00000
#
# ZAHTJEV NA ISPITU:
# Obično množenje x-a samog sa sobom n puta u petlji daje složenost O(n), što
# na ispitu nosi 0 bodova. Trik je u rastavljanju problema na pola:
# Umjesto 2^10 računamo (2^5) * (2^5). Time drastično smanjujemo broj koraka.
# ==============================================================================

def myPow(x, n):
    # 1. BAZNI SLUČAJ: Bilo koji broj na potenciju 0 je 1.0
    # Ovo je ujedno i trenutak kada rekurzija dotiče dno i kreće se vraćati natrag.
    if n == 0:
        return 1.0

    # 2. RJEŠAVANJE NEGATIVNIH POTENCIJA: 
    # Ako je n negativan (npr. 2^-3), matematički je to isto kao (1/2)^3.
    # Preokrenemo bazu x i pretvorimo n u pozitivan broj.
    if n < 0:
        x = 1 / x
        n = -n

    # 3. REKURZIVNI KORAK (Divide & Conquer):
    # Izračunamo samo JEDNU polovicu potencije (koristimo cjelobrojno dijeljenje //).
    # Računalo će skočiti dublje u rekurziju i donijeti nam gotov rezultat te polovice.
    half = myPow(x, n // 2)

    # 4. SPAJANJE REZULTATA:
    # Ako je n paran (npr. n = 10): 2^10 je isto što i 2^5 * 2^5.
    if n % 2 == 0:
        return half * half
    
    # Ako je n neparan (npr. n = 11): cjelobrojno dijeljenje 11 // 2 dalo je 5.
    # Zato moramo pomnožiti half * half i dodati još jedno množenje s bazom x (2^5 * 2^5 * 2^1).
    else:
        return half * half * x
