Merge - Array
Singly-linked: pointer
Doubly-linked: pointer
Singly-linked: data sawp
Doubly-linked: data sawp

#MERGE SORT 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result += [left[0]]
            left = left[1:]
        else:
            result += [right[0]]
            right = right[1:]

    result += left
    result += right

    return result
  
# MERGE JEDNO - pointer
def split_list_single_pointers(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return mid

def merge_single_pointers(left, right):
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
    if head is None or head.next is None:
        return head
    mid = split_list_single_pointers(head)
    left_sorted = merge_sort_single_pointers(head)
    right_sorted = merge_sort_single_pointers(mid)
    return merge_single_pointers(left_sorted, right_sorted)
    

# MERGE DOUBLE - pointer
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


# JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
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


# DVOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
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
