# ==============================================================================
# VERZIJA 1: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE: 
# 1. Funkcija 'split_list' koristi 'slow' i 'fast' pokazivače i postavlja 'slow.next = None'.
# 2. Funkcija 'merge' prima dvije glave i prespaja njihove '.next' pokazivače.
# 3. Podaci ('.data') se nigdje ne prepisuju, čvorovi fizički mijenjaju mjesta.
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def split_list_single_pointers(head):
    """Pronalazi sredinu, reže listu na pola i vraća početak desne polovice."""
    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None  # Fizički rez veze između polovica
    return mid

def merge_single_pointers(left, right):
    """Pomoćna funkcija koja spaja dvije sortirane jednostruke liste."""
    if left is None: return right
    if right is None: return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_single_pointers(left.next, right)
    else:
        result = right
        result.next = merge_single_pointers(left, right.next)
    return result

def merge_sort_single_pointers(head):
    # Bazni slučaj
    if head is None or head.next is None:
        return head
        
    # 1. Split cjelina
    mid = split_list_single_pointers(head)
    
    # 2. Rekurzivni pozivi
    left_sorted = merge_sort_single_pointers(head)
    right_sorted = merge_sort_single_pointers(mid)
    
    # 3. Merge cjelina
    return merge_single_pointers(left_sorted, right_sorted)





# ==============================================================================
# VERZIJA 2: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE:
# 1. Podaci se preko 'current.data' izvuku u običan Python niz (array/list).
# 2. Nad tim nizom se izvrši Merge Sort (split i merge rade s indeksima niza).
# 3. Na kraju se sortirane vrijednosti samo prepišu natrag u '.data' fiksnih čvorova.
# ==============================================================================

def split_array_and_merge(arr):
    """Merge sort nad običnim poljem (nizom)."""
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = split_array_and_merge(arr[:mid])
    right = split_array_and_merge(arr[mid:])
    
    # Spajanje (merge) dva niza
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_single_data(head):
    if head is None or head.next is None:
        return head
        
    # 1. Izvlačenje podataka iz liste u polje
    data_list = []
    current = head
    while current is not None:
        data_list.append(current.data)
        current = current.next
        
    # 2. Sortiranje polja Merge Sort algoritmom
    sorted_data = split_array_and_merge(data_list)
    
    # 3. Vraćanje sortiranih podataka u čvorove (data swap)
    current = head
    idx = 0
    while current is not None:
        current.data = sorted_data[idx]
        idx += 1
        current = current.next
        
    return head


