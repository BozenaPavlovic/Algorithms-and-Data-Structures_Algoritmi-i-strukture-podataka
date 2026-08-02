# ==============================================================================
# VERZIJA 1: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE: 
# 1. Koristi ugniježđene petlje gdje 'current' prolazi kroz cijelu listu od početka.
# 2. Unutarnja petlja 'start' svaki put kreće od 'head' i ide do 'current'.
# 3. Ako je podatak u 'start' veći od podataka u 'current', njihove '.data' vrijednosti 
#    se zamjenjuju. Pokazivači '.next' se NE DIRAJU.
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_sort_single_data(head):
    if head is None or head.next is None:
        return head
    
    current = head.next
    while current is not None:
        start = head
        # Prolazimo kroz već sortirani dio liste ispred 'current'
        while start != current:
            if start.data > current.data:
                # Zamjena podataka (data swap)
                start.data, current.data = current.data, start.data
            start = start.next
        current = current.next
        
    return head


# ==============================================================================
# VERZIJA 2: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. Kreira se potpuno nova prazna lista 'sorted_head = None'.
# 2. Uzimamo jedan po jedan čvor iz originalne liste i tražimo mu ispravno mjesto 
#    unutar nove 'sorted_head' liste prolaskom s 'prev' i 'current' od početka.
# 3. Fizički se mijenjaju '.next' pokazivači kako bi se čvor umetnuo između dva čvora.
# ==============================================================================

def insertion_sort_single_pointers(head):
    if head is None or head.next is None:
        return head

    sorted_head = None # Početak nove, sortirane liste
    current = head     # Čvor kojeg trenutno umećemo

    while current is not None:
        next_node = current.next # Spremo idući jer ćemo current.next prepisati
        
        # Tražimo mjesto za umetanje unutar sortirane liste
        if sorted_head is None or sorted_head.data >= current.data:
            # Umetanje na sam početak sortirane liste
            current.next = sorted_head
            sorted_head = current
        else:
            # Traženje pozicije u sredini ili na kraju sortirane liste
            prev = sorted_head
            while prev.next is not None and prev.next.data < current.data:
                prev = prev.next
                
            # Umetanje čvora između 'prev' i 'prev.next'
            current.next = prev.next
            prev.next = current
            
        current = next_node

    return sorted_head
