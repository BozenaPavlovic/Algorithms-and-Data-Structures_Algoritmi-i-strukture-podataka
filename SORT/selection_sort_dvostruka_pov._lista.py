# ==============================================================================
# VERZIJA 3: DVOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE:
# 1. Čvorovi sadrže i '.next' i '.prev' pokazivače.
# 2. Kod je u potpunosti IDENTIČAN verziji 1 (jednostruka lista + data swap).
# 3. Budući da prepisujemo isključivo '.data' vrijednosti, struktura pokazivača 
#    se ne mijenja, pa '.prev' pokazivač uopće ne moramo dirati niti koristiti.
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def selection_sort_double_data(head):
    if head is None or head.next is None:
        return head
    
    start = head
    while start is not None and start.next is not None:
        min_node = start
        current = start.next
        
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        
        if min_node != start:
            start.data, min_node.data = min_node.data, start.data
        
        start = start.next
    
    return head


# ==============================================================================
# VERZIJA 4: DVOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. Koristi se ista logika izrezivanja i dodavanja kao u verziji 2.
# 2. Kod izrezivanja i dodavanja 'min_node' moramo ažurirati i '.prev' pokazivače.
# 3. Kod je olakšan jer nam ne treba lokalna varijabla 'prev_min' kao kod jednostruke, 
#    budući da čvor sam zna svog prethodnika preko 'min_node.prev'.
# ==============================================================================

def selection_sort_double_pointers(head):
    if head is None or head.next is None:
        return head

    tail = None
    start = head

    while start is not None:
        min_node = start
        current = start.next

        # Unutarnja petlja: traži minimum
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next

        # Izbacivanje min_node iz nesortiranog dijela liste
        if min_node == start:
            start = start.next
        else:
            # Prespajanje pokazivača prema naprijed i unazad
            min_node.prev.next = min_node.next
            if min_node.next is not None:
                min_node.next.prev = min_node.prev

        # Dodavanje min_node na kraj sortiranog dijela (tail)
        if tail is None:
            head = min_node
            min_node.prev = None
        else:
            tail.next = min_node
            min_node.prev = tail

        tail = min_node

    return head
