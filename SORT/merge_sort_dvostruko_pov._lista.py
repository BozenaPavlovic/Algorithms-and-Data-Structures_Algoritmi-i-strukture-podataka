# ==============================================================================
# VERZIJA 3: DVOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. 'split_list' uz 'slow.next = None' mora postaviti i 'mid.prev = None'.
# 2. Funkcija 'merge' nakon svakog spajanja mora osigurati vezu unazad: 
#    'result.next.prev = result'.
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def split_list_double_pointers(head):
    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None  # Prekid prednje veze
    if mid is not None:
        mid.prev = None  # 🟢 DODATAK ZA DVOSTRUKU: Prekid stražnje veze
    return mid

def merge_double_pointers(left, right):
    """Spaja dvije sortirane dvostruke liste i obnavlja .prev veze."""
    if left is None: return right
    if right is None: return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_double_pointers(left.next, right)
        if result.next is not None:
            result.next.prev = result  # 🟢 DODATAK ZA DVOSTRUKU (veza unazad)
        result.prev = None
    else:
        result = right
        result.next = merge_double_pointers(left, right.next)
        if result.next is not None:
            result.next.prev = result  # 🟢 DODATAK ZA DVOSTRUKU (veza unazad)
        result.prev = None
    return result

def merge_sort_double_pointers(head):
    if head is None or head.next is None:
        return head
        
    mid = split_list_double_pointers(head)
    
    left_sorted = merge_sort_double_pointers(head)
    right_sorted = merge_sort_double_pointers(mid)
    
    return merge_double_pointers(left_sorted, right_sorted)




# ==============================================================================
# VERZIJA 4: DVOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE:
# 1. Čvorovi imaju i '.next' i '.prev' atribute koji se uopće ne modificiraju.
# 2. Svi podaci se izvuku u pomoćno polje 'data_list'.
# 3. Pomoćna funkcija 'merge_sort_array_logic' rekurzivno sortira to polje.
# 4. Na kraju se sortirane vrijednosti prepisuju natrag u fiksne čvorove liste.
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def merge_sort_array_logic(arr):
    """Kompletna i raspisana logika Merge Sorta nad običnim poljem."""
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    # Dijeljenje polja na lijevu i desnu polovicu
    left = merge_sort_array_logic(arr[:mid])
    right = merge_sort_array_logic(arr[mid:])
    
    # Spajanje (merge) dvaju sortiranih polja
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Dodavanje preostalih elemenata
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_double_data(head):
    if head is None or head.next is None:
        return head
        
    # 1. Korak: Izvlačenje svih podataka iz dvostruke liste u polje
    data_list = []
    current = head
    while current is not None:
        data_list.append(current.data)
        current = current.next
        
    # 2. Korak: Sortiranje tog polja pomoću raspisanog Merge Sorta
    sorted_data = merge_sort_array_logic(data_list)
    
    # 3. Korak: Vraćanje sortiranih vrijednosti natrag u čvorove (Data Swap)
    current = head
    idx = 0
    while current is not None:
        current.data = sorted_data[idx]
        idx += 1
        current = current.next
        
    return head


