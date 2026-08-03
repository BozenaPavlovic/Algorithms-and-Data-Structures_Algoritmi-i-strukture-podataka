# DATA SAWP

# ==============================================================================
# BUCKET SORT - JEDNOSTRUKO POVEZANA LISTA
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


# ==============================================================================
# POMOĆNA FUNKCIJA 1: INSERTION SORT
# ==============================================================================

def insertion_sort(head):
    """Sortira povezanu listu Insertion Sortom (rastući poredak)."""
    if head is None or head.next is None:
        return head
    
    sorted_head = None
    current = head
    
    while current is not None:
        next_node = current.next
        
        # Umetanje na početak
        if sorted_head is None or sorted_head.data >= current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            # Traženje pozicije
            temp = sorted_head
            while temp.next is not None and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        
        current = next_node
    
    return sorted_head


# ==============================================================================
# POMOĆNA FUNKCIJA 2: PRONALAŽENJE MIN I MAX
# ==============================================================================

def find_min_max(head):
    """Pronalazi minimalnu i maksimalnu vrijednost u listi."""
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
# POMOĆNA FUNKCIJA 3: SPOJANJE PRETINACA
# ==============================================================================

def concatenate_buckets(buckets, bucket_count):
    """Spaja sve pretince u jednu listu."""
    sorted_head = None
    sorted_tail = None
    
    for i in range(bucket_count):
        if buckets[i] is not None:
            if sorted_head is None:
                sorted_head = buckets[i]
            else:
                sorted_tail.next = buckets[i]
            
            sorted_tail = buckets[i]
            while sorted_tail.next is not None:
                sorted_tail = sorted_tail.next
    
    return sorted_head


# ==============================================================================
# GLAVNA FUNKCIJA: BUCKET SORT
# ==============================================================================

def bucket_sort(head, bucket_count):
    """
    Sortira povezanu listu Bucket Sort algoritmom (rastući poredak).
    
    Argumenti:
        head - glava liste
        bucket_count - broj pretinaca
    
    Vraća:
        Glavu sortirane liste
    """
    if head is None or head.next is None:
        return head
    
    # 1. Pronađi min i max
    min_val, max_val = find_min_max(head)
    
    # Ako su svi elementi isti
    if min_val == max_val:
        return head
    
    # 2. Kreiraj pretince
    buckets = [None] * bucket_count
    
    # 3. Raspodijeli čvorove u pretince
    current = head
    while current is not None:
        next_node = current.next
        
        # Izračunaj indeks pretinca
        bucket_idx = int((current.data - min_val) * (bucket_count - 1) / (max_val - min_val))
        
        # Umetni na početak pretinca
        current.next = buckets[bucket_idx]
        buckets[bucket_idx] = current
        
        current = next_node
    
    # 4. Sortiraj svaki pretinac
    for i in range(bucket_count):
        if buckets[i] is not None:
            buckets[i] = insertion_sort(buckets[i])
    
    # 5. Spoji sve pretince
    return concatenate_buckets(buckets, bucket_count)


# ==============================================================================
# METODA UNUTAR KLASE
# ==============================================================================

class LinkedList:
    def bucket_sort(self, bucket_count):
        """Sortira listu Bucket Sort algoritmom (rastući poredak)."""
        self.head = bucket_sort(self.head, bucket_count)
