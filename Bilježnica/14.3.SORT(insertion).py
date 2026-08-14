INSERTION SORT ARR + swaps
JEDNOSTRUKO POVEZANA LISTA Data sawp
JEDNOSTRUKO POVEZANA LISTA pointer sawp
DVOSTRUKO POVEZANA LISTA Data sawp
DVOSTRUKO POVEZANA LISTA pointer sawp


#INSERTION SORT ARR ( + swaps jer nekada na ipsot reče da doodamo u bilo koji algoritam sawpa s arr da nas provijeri)
def insertion_sort(arr):
    swaps = 0  # brojač zamjena (pomaka)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            swaps += 1  # svaki shift računamo kao zamjenu
            j -= 1
        arr[j + 1] = key
        swaps += 1  # umetanje key-a

    return arr, swaps
    
#JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
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

#JEDNOSTRUKO POVEZANA LISTA pointer sawp
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

# DVOSTRUKO POVEZANA LISTA Data sawp
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
   
# DVOSTRUKO POVEZANA LISTA pointer sawp
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
    
