# ==============================================================================
# BUCKET SORT - DVOSTRUKO POVEZANA LISTA (DATA SWAP)
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


# ==============================================================================
# POMOĆNA FUNKCIJA: INSERTION SORT NA POVEZANOJ LISTI (DATA SWAP)
# ==============================================================================

def insertion_sort(head):
    """
    Insertion sort na povezanoj listi (DATA SWAP).
    Mijenja se samo .data, pokazivači ostaju isti.
    """
    if head is None or head.next is None:
        return head
    
    # Uzmi podatke u pomoćnu listu (ovo je data swap)
    data_list = []
    current = head
    while current is not None:
        data_list.append(current.data)
        current = current.next
    
    # Insertion sort na listi podataka
    for i in range(1, len(data_list)):
        key = data_list[i]
        j = i - 1
        while j >= 0 and data_list[j] > key:
            data_list[j + 1] = data_list[j]
            j -= 1
        data_list[j + 1] = key
    
    # Vrati podatke natrag u čvorove (DATA SWAP)
    current = head
    for val in data_list:
        current.data = val
        current = current.next
    
    return head


# ==============================================================================
# POMOĆNA FUNKCIJA: PRONALAŽENJE MIN I MAX
# ==============================================================================

def find_min_max(head):
    """Pronalazi min i max u listi."""
    if head is None:
        return None, None
    
    min_val = head.data
    max_val = head.data
    current = head
    
    while current is not None:
        if current.data < min_val:
            min_val = current.data
        if current.data > max_val:
            max_val = current.data
        current = current.next
    
    return min_val, max_val


# ==============================================================================
# GLAVNA FUNKCIJA: BUCKET SORT
# ==============================================================================

def bucket_sort(head, bucket_count):
    """
    Bucket sort na dvostruko povezanoj listi (DATA SWAP).
    """
    if head is None or head.next is None:
        return head
    
    # 1. Pronađi min i max
    min_val, max_val = find_min_max(head)
    
    if min_val == max_val:
        return head
    
    # 2. Kreiraj pretince (svaki pretinac je glava povezane liste)
    buckets = [None] * bucket_count
    
    # 3. Raspodijeli čvorove u pretince
    current = head
    while current is not None:
        next_node = current.next
        
        # Izračunaj indeks pretinca
        bucket_idx = int((current.data - min_val) * (bucket_count - 1) / (max_val - min_val))
        
        # Umetni na početak pretinca
        current.next = buckets[bucket_idx]
        if buckets[bucket_idx] is not None:
            buckets[bucket_idx].prev = current
        current.prev = None
        buckets[bucket_idx] = current
        
        current = next_node
    
    # 4. Sortiraj svaki pretinac (Insertion Sort - DATA SWAP)
    for i in range(bucket_count):
        if buckets[i] is not None:
            buckets[i] = insertion_sort(buckets[i])
    
    # 5. Spoji sve pretince
    sorted_head = None
    sorted_tail = None
    
    for i in range(bucket_count):
        if buckets[i] is not None:
            if sorted_head is None:
                sorted_head = buckets[i]
            else:
                sorted_tail.next = buckets[i]
                buckets[i].prev = sorted_tail
            
            # Pronađi kraj
            sorted_tail = buckets[i]
            while sorted_tail.next is not None:
                sorted_tail = sorted_tail.next
    
    return sorted_head


# ==============================================================================
# METODA UNUTAR KLASE
# ==============================================================================

class DoublyLinkedList:
    def bucket_sort(self, bucket_count):
        """Sortira listu Bucket Sort algoritmom (DATA SWAP)."""
        self.head = bucket_sort(self.head, bucket_count)
