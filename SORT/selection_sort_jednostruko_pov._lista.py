# ==============================================================================
# VERZIJA 1: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE: 
# 1. Vanjska petlja s 'start' fiksira poziciju, a unutarnja s 'current' traži minimum.
# 2. Kada se pronađe 'min_node', zamjenjuju se isključivo '.data' vrijednosti:
#    'start.data, min_node.data = min_node.data, start.data'
# 3. Pokazivači '.next' ostaju netaknuti. Čvorovi ne mijenjaju mjesta u memoriji.
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def selection_sort_single_data(head):
    if head is None or head.next is None:
        return head
    
    start = head
    while start is not None and start.next is not None:
        min_node = start
        current = start.next
        
        # Traženje najmanjeg elementa u ostatku liste
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        
        # Zamjena podataka ako je pronađen manji element
        if min_node != start:
            start.data, min_node.data = min_node.data, start.data
        
        start = start.next
    
    return head



# ==============================================================================
# VERZIJA 2: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. '.data' je zaključan. Umjesto zamjene vrijednosti, fizički "izrezujemo" 
#    pronađeni 'min_node' iz nesortiranog dijela i dodajemo ga na kraj sortiranog dijela.
# 2. Moramo pratiti prethodnika od minimuma ('prev_min') kako bismo ga mogli izrezati.
# 3. Koristimo 'tail' pokazivač koji označava kraj novog, sortiranog dijela liste.
# ==============================================================================

def selection_sort_single_pointers(head):
    if head is None or head.next is None:
        return head

    tail = None          # Kraj sortiranog dijela liste
    start = head         # Početak nesortiranog dijela liste

    while start is not None:
        min_node = start
        prev_min = None  # Prati čvor ispred min_node
        
        prev = start
        current = start.next

        # Unutarnja petlja: traži minimum i pamti njegovog prethodnika
        while current is not None:
            if current.data < min_node.data:
                min_node = current
                prev_min = prev
            prev = current
            current = current.next

        # Izbacivanje (izrezivanje) min_node iz nesortiranog dijela
        if min_node == start:
            start = start.next
        else:
            prev_min.next = min_node.next

        # Dodavanje min_node na kraj sortiranog dijela (tail)
        if tail is None:
            head = min_node
        else:
            tail.next = min_node

        tail = min_node

    return head
