# ==============================================================================
# 1. SLL - VERZIJA A: ZAMJENA PODATAKA (DATA SWAP) - PRVI ELEMENT JE PIVOT
# Uvjet: Čvorovi ostaju fiksni u memoriji, mijenjaju se samo vrijednosti (.data).
# Prepoznavanje: Profesor ne brani izmjenu podataka unutar čvorova.
# ==============================================================================


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
def partition_sll_data_swap(head, tail):
    # Prvi element podliste se uzima kao pivot
    pivot = head
    pre = head
    curr = head

    # Prolazak kroz podlistu od glave do repa
    while curr != tail.next:
        if curr.data < pivot.data:
            # Zamjena podataka između trenutnog čvora i čvora nakon 'pre'
            curr.data, pre.next.data = pre.next.data, curr.data
            pre = pre.next
        curr = curr.next

    # Postavljanje pivot podataka na pravo mjesto u sredini
    pivot.data, pre.data = pre.data, pivot.data
    return pre

def quick_sort_sll_data_swap_helper(head, tail):
    if head is None or head == tail:
        return
    
    # Pronalaženje novog pivota nakon particioniranja
    pivot = partition_sll_data_swap(head, tail)

    # Rekurzija za lijevu i desnu stranu
    quick_sort_sll_data_swap_helper(head, pivot)
    quick_sort_sll_data_swap_helper(pivot.next, tail)

def quick_sort_sll_data_swap(head):
    if not head:
        return head
    
    # Pronalaženje kraja liste (tail)
    tail = head
    while tail.next:
        tail = tail.next
        
    quick_sort_sll_data_swap_helper(head, tail)
    return head



# ==============================================================================
# 2. SLL - VERZIJA B: ZAMJENA POKAZIVAČA (POINTER SWAP) - PRVI ELEMENT JE PIVOT
# Uvjet: Strogo zabranjeno mijenjati .data. Fizički otspajamo i spajamo .next.
# Prepoznavanje: "Sortirati preusmjeravanjem pokazivača, a ne zamjenom podataka".
# ==============================================================================
def quick_sort_sll_pointer_swap(head):
    # Bazni slučaj: ako je lista prazna ili ima samo jedan element
    if head is None or head.next is None:
        return head

    # Prvi element je pivot, izoliramo ga iz ostatka liste
    pivot = head
    curr = head.next
    pivot.next = None

    # Glave i repovi dviju novih podlista
    less_head, less_tail = None, None
    greater_head, greater_tail = None

    # Particioniranje preusmjeravanjem .next pokazivača
    while curr is not None:
        next_node = curr.next
        curr.next = None  # Otspajanje čvora

        if curr.data < pivot.data:
            if less_head is None:
                less_head = less_tail = curr
            else:
                less_tail.next = curr
                less_tail = curr
        else:
            if greater_head is None:
                greater_head = greater_tail = curr
            else:
                greater_tail.next = curr
                greater_tail = curr
        curr = next_node

    # Rekurzivni pozivi helpera kroz funkciju
    less_sorted = quick_sort_sll_pointer_swap(less_head)
    greater_sorted = quick_sort_sll_pointer_swap(greater_head)

    # Spajanje: Sortirana manja lista + Pivot + Sortirana veća lista
    if less_sorted is not None:
        new_head = less_sorted
        tail = less_sorted
        while tail.next is not None:
            tail = tail.next
        tail.next = pivot
    else:
        new_head = pivot

    pivot.next = greater_sorted
    return new_head
