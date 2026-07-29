class Node:
    """Čvor dvostruko povezane liste."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Dodan pokazivač na prethodni čvor


class DoublyLinkedList:
    """Klasa koja upravlja dvostruko povezanim čvorovima."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Dodavanje elementa na kraj dvostruko povezane liste."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last  # Postavljanje povratne veze

    def print_forward(self):
        """Ispisuje listu od početka prema kraju."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Naprijed: " + " <-> ".join(elements) + " -> None")

    def print_backward(self):
        """Ispisuje listu od kraja prema početku (provjera ispravnosti 'prev' veza)."""
        if not self.head:
            print("Natrag: None")
            return
        last = self.head
        while last.next:
            last = last.next
        
        elements = []
        while last:
            elements.append(str(last.data))
            last = last.prev
        print("Natrag:   " + " <-> ".join(elements) + " -> None")


def sorted_insert(head, new_node):
    """Pomoćna funkcija: Umeće čvor u već sortiranu dvostruku listu."""
    # Resetiramo veze novog čvora za svaki slučaj
    new_node.next = None
    new_node.prev = None

    # Slučaj 1: Lista je prazna ili novi čvor dolazi na sam početak
    if head is None:
        return new_node
    
    if head.data >= new_node.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    # Slučaj 2: Traženje pozicije unutar ili na kraju liste
    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    # Umetanje čvora nakon 'current' čvora
    new_node.next = current.next
    if current.next is not None:
        current.next.prev = new_node
        
    current.next = new_node
    new_node.prev = current
    
    return head


def insertion_sort(head):
    """Sortira dvostruko povezanu listu pomoću Insertion Sorta."""
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head
    
    while current is not None:
        next_node = current.next  # Spremi referencu prije nego što izmijenimo veze
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node

    return sorted_head


def bucket_sort_doubly_linked_list(dll, bucket_count=5):
    """Glavna funkcija za Bucket Sort dvostruko povezane liste."""
    head = dll.head
    if head is None or head.next is None:
        return dll

    # 1. Pronalaženje minimalne i maksimalne vrijednosti
    min_val = head.data
    max_val = head.data
    current = head
    while current:
        if current.data < min_val:
            min_val = current.data
        if current.data > max_val:
            max_val = current.data
        current = current.next

    if min_val == max_val:
        return dll

    # 2. Inicijalizacija pretinaca (svaki pretinac sadrži glavu podliste)
    buckets = [None] * bucket_count

    # 3. Scatter (Razvrstavanje) čvorova u pretince
    current = head
    while current:
        next_node = current.next  # Spremi idući čvor
        
        # Izračun indeksa pretinca
        bucket_idx = int((current.data - min_val) * (bucket_count - 1) / (max_val - min_val))
        
        # Umetanje čvora na početak podliste u pretincu (O(1) operacija)
        current.next = buckets[bucket_idx]
        current.prev = None  # Budući da ide na početak pretinca, nema prethodnika
        
        if buckets[bucket_idx] is not None:
            buckets[bucket_idx].prev = current
            
        buckets[bucket_idx] = current
        current = next_node

    # 4. Gather (Skupljanje) i spajanje pretinaca
    sorted_head = None
    sorted_tail = None

    for i in range(bucket_count):
        if buckets[i] is not None:
            # Sortiraj trenutni pretinac
            buckets[i] = insertion_sort(buckets[i])

            # Ako je ovo prvi neprazni pretinac, postavi ga kao početak glavne liste
            if sorted_head is None:
                sorted_head = buckets[i]
            else:
                # Spajanje trenutnog pretinca na kraj prethodnog (dvosmjerno povezivanje)
                sorted_tail.next = buckets[i]
                buckets[i].prev = sorted_tail

            # Pomakni 'sorted_tail' na kraj trenutno spojenog pretinca
            sorted_tail = buckets[i]
            while sorted_tail.next is not None:
                sorted_tail = sorted_tail.next

    # Ažuriraj glavu originalne liste u objektu
    dll.head = sorted_head
    return dll


# --- Testiranje algoritma ---
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Dodavanje nesortiranih elemenata
    test_data = [42, 11, 33, 11, 8, 55, 22]
    for val in test_data:
        dll.append(val)

    print("--- Prije sortiranja ---")
    dll.print_forward()
    dll.print_backward()

    # Pokretanje Bucket Sorta
    bucket_sort_doubly_linked_list(dll, bucket_count=5)

    print("\n--- Nakon sortiranja ---")
    dll.print_forward()
    dll.print_backward()  # Ako se ispravno ispiše unatrag, sve 'prev' veze rade!
