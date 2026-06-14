# ==============================================================================
# ZADATAK 6: prva_tri i zadnja_tri elementa povezane liste
#
# TEKST ZADATKA:
# Napišite funkciju prva_tri koja u obliku ntorke (tuple) vraća prva tri elementa 
# jednostruko povezane liste i funkciju zadnja_tri koja vraća zadnja tri elementa 
# jednostruko povezane liste (pod pretpostavkom da lista ima dovoljan broj elemenata). 
# Ako lista nema dovoljan broj elemenata treba vratiti ntorku s dva, jednim ili 
# 0 elemenata (ako je lista prazna).
# ==============================================================================

class Cvor:
    def __init__(self, podatak=None, sljedeci=None):
        self.podatak = podatak
        self.sljedeci = sljedeci

def prva_tri(glava):
    rezultat = []
    curr = glava
    # Uzimamo elemente dok ne skupimo 3 ili dok ne dođemo do kraja liste
    while curr is not None and len(rezultat) < 3:
        rezultat.append(curr.podatak)
        curr = curr.sljedeci
    return tuple(rezultat)

def zadnja_tri(glava):
    # Prvo skupimo sve elemente liste u običnu Python listu
    svi_elementi = []
    curr = glava
    while curr is not None:
        svi_elementi.append(curr.podatak)
        curr = curr.sljedeci
    
    # Uzimamo zadnja tri elementa pomoću isječka (slice)
    # Ako lista ima manje od 3 elementa, [-3:] će uzeti sve što ima
    return tuple(svi_elementi[-3:])
