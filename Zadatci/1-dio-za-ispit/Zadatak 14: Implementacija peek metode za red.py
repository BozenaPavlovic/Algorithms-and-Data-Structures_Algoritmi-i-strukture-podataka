# ==============================================================================
# ZADATAK 14: Prvi član na izlazu iz reda (peek metoda)
#
# TEKST ZADATKA:
# Napišite funkciju koja vraća prvi član na izlazu iz reda iz klase Red, 
# ali tako da nakon izlaska iz funkcije taj član ostane na redu (tzv. peek metoda). 
# Smiju se koristiti samo osnovne funkcije za rad s redovima: dodaj i skini.
# ==============================================================================

def peek_reda(red):
    if red.velicina() == 0:
        return None
        
    # Skinemo prvi element (to je naš traženi element na izlazu)
    prvi = red.skini()
    
    # Privremeno ga stavimo na kraj reda
    red.dodaj(prvi)
    
    # Rotiramo sve ostale elemente kružno da se početni redoslijed vrati
    for _ in range(red.velicina() - 1):
        red.dodaj(red.skini())
        
    return prvi
