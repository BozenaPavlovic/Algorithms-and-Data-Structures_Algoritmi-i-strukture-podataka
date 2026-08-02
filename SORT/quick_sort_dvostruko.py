class DLLNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

# ==============================================================================
# 3. DLL - VERZIJA A: ZAMJENA PODATAKA (DATA SWAP) - PRVI ELEMENT JE PIVOT
# Uvjet: Mijenjaju se samo vrijednosti unutar .data, čvorovi su nepomični.
# Prednost: .prev i .next omogućuju precizno definiranje granica podliste.
# ==============================================================================
def partition_dll_data_swap(head, tail):
    pivot = head
    pre = head
    curr = head

    while curr != tail.next:
        if curr.data < pivot.data:
            curr.data, pre.next.data = pre.next.data, curr.data
            pre = pre.next
        curr = curr.next

    pivot.data, pre.data = pre.data, pivot.data
    return pre

def quick_sort_dll_data_swap_helper(head, tail):
    # Provjera valjanosti granica za dvostruku listu
    if head is None or tail is None or head == tail or head == tail.next:
        return
    
    pivot = partition_dll_data_swap(head, tail)

    # Kod DLL-a možemo precizno ići do pivot.prev i od pivot.next
    quick_sort_dll_data_swap_helper(head, pivot.prev)
    quick_sort_dll_data_swap_helper(pivot.next, tail)

def quick_sort_dll_data_swap(head):
    if not head:
        return head
    
    tail = head
    while tail.next:
        tail = tail.next
        
    quick_sort_dll_data_swap_helper(head, tail)
    return head





# ==============================================================================
# 4. DLL - VERZIJA B: ZAMJENA POKAZIVAČA (POINTER SWAP) - PRVI ELEMENT JE PIVOT
# Uvjet: Zabranjeno mijenjati .data. Moraju se ažurirati i .next i .prev veze.
# Napomena: Pivot se potpuno izolira postavljanjem .next i .prev na None.
# ==============================================================================
def quick_sort_dll_pointer_swap(head):
    if head is None or head.next is None:
        return head

    # Prvi element je pivot, čistimo mu veze s obje strane
    pivot = head
    curr = head.next
    pivot.next = None
    pivot.prev = None

    less_head, less_tail = None, None
    greater_head, greater_tail = None

    # Razvrstavanje čvorova uz održavanje dvosmjernih (.next i .prev) veza
    while curr is not None:
        next_node = curr.next
        curr.next = None
        curr.prev = None

        if curr.data < pivot.data:
            if less_head is None:
                less_head = less_tail = curr
            else:
                less_tail.next = curr
                curr.prev = less_tail
                less_tail = curr
        else:
            if greater_head is None:
                greater_head = greater_tail = curr
            else:
                greater_tail.next = curr
                curr.prev = greater_tail
                greater_tail = curr
        curr = next_node

    # Rekurzivno sortiraj podliste
    less_sorted = quick_sort_dll_pointer_swap(less_head)
    greater_sorted = quick_sort_dll_pointer_swap(greater_head)

    # Spajanje: Manja lista + Pivot + Veća lista
    if less_sorted is not None:
        new_head = less_sorted
        tail = less_sorted
        while tail.next is not None:
            tail = tail.next
        
        # Spajanje repa manje liste s pivotom
        tail.next = pivot
        pivot.prev = tail
    else:
        new_head = pivot

    # Spajanje pivota s glavom veće liste
    if greater_sorted is not None:
        pivot.next = greater_sorted
        greater_sorted.prev = pivot

    return new_head

