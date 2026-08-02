# ==============================================================================
# VERZIJA 3: DVOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE:
# 1. Čvorovi sadrže i '.next' i '.prev' pokazivače.
# 2. Baš kao i kod Bubble i Selection sorta sa zamjenom podataka, kod je 
#    POTPUNO IDENTIČAN verziji 1 za jednostruku listu.
# 3. Budući da se mijenjaju isključivo vrijednosti u '.data', pokazivač '.prev' 
#    se uopće ne mora koristiti niti ažurirati u kodu.
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertion_sort_double_data(head):
    if head is None or head.next is None:
        return head
    
    current = head.next
    while current is not None:
        start = head
        while start != current:
            if start.data > current.data:
                start.data, current.data = current.data, start.data
            start = start.next
        current = current.next
        
    return head


# ==============================================================================
# VERZIJA 4: DVOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. Ovo je jedina verzija u kojoj se koristi stvarna snaga dvostruke liste! 
#    'current' ide prema naprijed, a kada nađe manji element, s ugniježđenom petljom 
#    idemo UNATRAG pomoću '.prev' i tražimo mjesto za umetanje.
# 2. Čvor se fizički izrezuje sa svoje pozicije i umeće unazad na novu poziciju.
# 3. Moraju se ažurirati i '.next' i '.prev' pokazivači za sve susjedne čvorove.
# ==============================================================================

def insertion_sort_double_pointers(head):
    if head is None or head.next is None:
        return head

    current = head.next
    while current is not None:
        next_node = current.next # Spremamo idući čvor prije prespajanja
        
        # Ako je trenutni čvor manji od svog prethodnika, moramo ga pomaknuti unazad
        if current.data < current.prev.data:
            # 1. Izbacujemo 'current' iz trenutne pozicije (krpamo rupu)
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            
            # 2. Idemo unazad kroz listu i tražimo gdje ga umetnuti
            prev = current.prev
            while prev.prev is not None and prev.prev.data > current.data:
                prev = prev.prev
                
            # 3. Umećemo 'current' ispred čvora 'prev'
            if prev.prev is None and prev.data > current.data:
                # Umetanje na sam početak liste (novi head)
                current.next = prev
                current.prev = None
                prev.prev = current
                head = current
            else:
                # Umetanje u sredinu (između prev.prev i prev)
                current.next = prev
                current.prev = prev.prev
                if prev.prev is not None:
                    prev.prev.next = current
                prev.prev = current
                
        current = next_node

    return head
