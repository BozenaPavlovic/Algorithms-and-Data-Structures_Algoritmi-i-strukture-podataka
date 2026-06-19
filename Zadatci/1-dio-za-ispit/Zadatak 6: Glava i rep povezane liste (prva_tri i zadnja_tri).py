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

class Node:
    def __init__(self, data=None, next_node=None):
        # Inicijalizacija čvora povezane liste
        # data: sprema vrijednost elementa
        # next_node: pokazivač na idući čvor u listi
        self.data = data
        self.next_node = next_node


def first_three(head):
    # Funkcija vraća prva tri elementa liste kao ntorku (tuple)
    result = []
    curr = head
    
    # Prolazimo kroz listu i uzimamo elemente
    # Zaustavljamo se ako je lista gotova ili ako već imamo 3 elementa
    while curr is not None and len(result) < 3:
        result.append(curr.data)
        curr = curr.next_node
        
    return tuple(result)


def last_three(head):
    # Funkcija vraća zadnja tri elementa liste kao ntorku (tuple)
    # Koristimo pomoćnu listu za skupljanje svih vrijednosti
    all_elements = []
    curr = head
    
    # Prolazimo kroz cijelu povezanu listu od početka do kraja
    while curr is not None:
        all_elements.append(curr.data)
        curr = curr.next_node
        
    # Python isječak (slice) [-3:] sigurno vraća zadnja 3 elementa.
    # Ako lista ima manje od 3 elementa, vratit će sve postojeće elemente.
    return tuple(all_elements[-3:])
