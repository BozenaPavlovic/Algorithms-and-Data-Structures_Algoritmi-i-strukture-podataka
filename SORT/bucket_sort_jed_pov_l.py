class Node:
    """Čvor jednostruko povezane liste."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Klasa koja upravlja povezanim čvorovima."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Pomoćna metoda za dodavanje elementa na kraj liste."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """Ispisuje listu u čitljivom formatu."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")


def sorted_insert(head, new_node):
    """Pomoćna funkcija: Umeće čvor u već sortiranu listu."""
    # Ako je lista prazna ili novi čvor dolazi na sam početak
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    # Traženje pozicije za umetanje
    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head


def insertion_sort(head):
    """Sortira povezanu listu pomoću Insertion Sort algoritma."""
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head
    
    while current is not None:
        next_node = current.next  # Spremi pokazivač na idući čvor
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node

    return sorted_head


def bucket_sort_linked_list(linked_list, bucket_count=5):
    """Glavna funkcija za Bucket Sort povezane liste."""
    head = linked_list.head
    if head is None or head.next is None:
        return linked_list

    # 1. Pronađi minimalnu i maksimalnu vrijednost u listi
    min_val = head.data
    max_val = head.data
    current = head
    while current:
        if current.data < min_val:
            min_val = current.data
        if current.data > max_val:
            max_val = current.data
        current = current.next

    # Ako su svi elementi u listi isti, ona je već sortirana
    if min_val == max_val:
        return linked_list

    # 2. Inicijaliziraj listu pretinaca (svaki pretinac drži referencu na glavu svoje podliste)
    buckets = [None] * bucket_count

    # 3. Scatter (Razvrstavanje): Raspodijeli čvorove u pretince
    current = head
    while current:
        next_node = current.next  # Spremi idući čvor prije promjene pokazivača
        
        # Izračunaj indeks pretinca na temelju raspona vrijednosti
        bucket_idx = int((current.data - min_val) * (bucket_count - 1) / (max_val - min_val))
        
        # Umetni čvor na početak odgovarajućeg pretinca (efikasno O(1) umetanje)
        current.next = buckets[bucket_idx]
        buckets[bucket_idx] = current
        
        current = next_node

    # 4. Gather (Skupljanje): Sortiraj pretince i spoji ih natrag u jednu listu
    sorted_head = None
    sorted_tail = None

    for i in range(bucket_count):
        if buckets[i] is not None:
            # Sortiraj trenutni pretinac pomoću Insertion Sorta
            buckets[i] = insertion_sort(buckets[i])

            # Ako je ovo prvi pretinac koji spajamo, postavi njegovu glavu kao glavnu glavu
            if sorted_head is None:
                sorted_head = buckets[i]
            else:
                # Inače, nadoveži ga na kraj prethodno spojenih pretinaca
                sorted_tail.next = buckets[i]

            # Pomakni 'tail' pokazivač na kraj novonastale sortirane liste brojeva
            sorted_tail = buckets[i]
            while sorted_tail.next is not None:
                sorted_tail = sorted_tail.next

    # Ažuriraj glavu originalnog objekta liste brojeva
    linked_list.head = sorted_head
    return linked_list


# --- Testiranje algoritma ---
if __name__ == "__main__":
    ll = LinkedList()
    
    # Dodaj elemente u listu
    for val in:
        ll.append(val)

    print("Originalna lista:")
    ll.print_list()

    # Pokretanje Bucket Sorta s 5 pretinaca
    bucket_sort_linked_list(ll, bucket_count=5)

    print("\nSortirana lista:")
    ll.print_list()
