# ==============================================================================
# ZADATAK 13: i-ti član na stogu bez uništavanja stoga
#
# TEKST ZADATKA:
# Napišite funkciju koja vraća i-ti član na stogu iz klase Stog (i=0 označava 
# vrh stoga). Stog nakon izlaska iz funkcije mora ostati nepromijenjen, 
# a smiju se koristiti samo osnovne metode za rad sa stogovima: dodaj i skini.
# ==============================================================================

def dohvati_iti_clan_stoga(stog, i):
    pomocni_stog = Stog()  # Pretpostavlja se klasa Stog iz teksta zadatka
    trazeni_element = None
    brojac = 0
    
    # Skidamo elemente dok ne dođemo do i-tog indeksa
    while stog.velicina() > 0:
        trenutni = stog.skini()
        if brojac == i:
            trazeni_element = trenutni
        
        # Svaki skinuti element čuvamo na pomoćnom stogu
        pomocni_stog.dodaj(trenutni)
        
        if brojac == i:
            break
        brojac += 1
        
    # Vraćamo elemente natrag na originalni stog kako bi ostao nepromijenjen
    while pomocni_stog.velicina() > 0:
        stog.dodaj(pomocni_stog.skini())
        
    return trazeni_element
