# ==============================================================================
# ZADATAK 2: Konkatenacija dvostruko povezanih lista (5 bodova)
#
# TEKST ZADATKA:
# Napišite brz i učinkovit algoritam (funkciju) za konkatenaciju dvaju dvostruko 
# povezanih lista koje imaju header i trailer sentinel čvorove, u jednu listu 
# koju algoritam treba vratiti. Algoritam ne bi trebao prepisivati elemente lista 
# u nove liste (brz i učinkovit). Funkcija treba imati prototip 
# concatenate(list1, list2) i treba vratiti objekt iz iste te klase. 
# Svaka lista ima atribute header, trailer i size.
# ==============================================================================

def concatenate(list1, list2):
    # Ako je prva lista prazna, rezultat je jednostavno druga lista
    if list1.size == 0:
        return list2
    # Ako je druga lista prazna, rezultat je prva lista
    if list2.size == 0:
        return list1
        
    # Ključni korak spajanja: preusmjeravamo veze između krajeva lista
    # Spajamo zadnji stvarni element prve liste s prvim stvarnim elementom druge liste
    list1.trailer.prev.next = list2.header.next
    list2.header.next.prev = list1.trailer.prev
    
    # Trailer od list2 sada postaje službeni trailer od list1
    list1.trailer = list2.trailer
    
    # Ažuriramo veličinu spojene liste
    list1.size += list2.size
    
    # Vraćamo objekt iste klase (list1) koji je sada proširen s elementima list2
    return list1
