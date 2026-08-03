# ==============================================================================
# BUCKET SORT - JEDNOSTRUKO POVEZANA LISTA
# ==============================================================================
# Opis:
# Bucket sort raspoređuje elemente u više "pretinaca" (bucket-a), zatim svaki
# pretinac sortira zasebno (pomoću Insertion Sorta), i na kraju spaja sve 
# pretince u jednu sortiranu listu.
#
# Vremenska složenost:
# - Najbolji slučaj: O(N + K) gdje je K broj pretinaca
# - Prosječni slučaj: O(N + K) ako su podaci ravnomjerno raspoređeni
# - Najgori slučaj: O(N²) ako svi podaci završe u jednom pretincu
#
# Prostorna složenost: O(N + K) - dodatni prostor za pretince
# ==============================================================================

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
        """Pomoćna metoda za dodavanje elementa na kraj liste (samo za testiranje)."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


# ==============================================================================
# INSERTION SORT (METODA UNUTAR KLASE)
# ==============================================================================
# Opis:
# Insertion sort za povezanu listu radi na principu da se lista dijeli na 
# sortirani i nesortirani dio. Svaki element iz nesortiranog dijela se 
# umeće na odgovarajuće mjesto u sortirani dio.
#
# Prepoznavanje:
# 1. Koristi se pomoćna funkcija 'sorted_insert' za umetanje u sortiranu listu.
# 2. Radi na principu "gradi sortiranu listu od nule" - uzima čvor po čvor 
#    iz originalne liste i umeće ih u novu sortiranu listu.
# 3. Ovo je STANDARDNA implementacija insertion sorta za povezane liste.
#
# Vremenska složenost: O(N²) u najgorem slučaju
# Prostorna složenost: O(1) - sortiranje na mjestu
# ==============================================================================

    def _sorted_insert(self, head, new_node):
        """
        Pomoćna metoda: Umeće čvor u već sortiranu listu (rastući poredak).
        
        Argumenti:
            head - glava sortirane liste
            new_node - čvor koji treba umetnuti
        
        Vraća:
            Novu glavu liste nakon umetanja
        """
        # Ako je lista prazna ili novi čvor dolazi na sam početak
        if head is None or head.data >= new_node.data:
            new_node.next = head
            return new_node

        # Traženje pozicije za umetanje
        current = head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next

        # Umetanje čvora
        new_node.next = current.next
        current.next = new_node
        return head

    def insertion_sort(self):
        """
        Sortira listu pomoću Insertion Sort algoritma (rastući poredak).
        
        Vraća:
            None - sortira listu na mjestu (in-place)
        """
        head = self.head
        if head is None or head.next is None:
            return

        sorted_head = None
        current = head
        
        while current is not None:
            next_node = current.next  # Spremi pokazivač na idući čvor
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head


# ==============================================================================
# BUCKET SORT (METODA UNUTAR KLASE)
# ==============================================================================
# Opis:
# Bucket sort za povezanu listu prolazi kroz 3 faze:
# 1. Scatter (razbacivanje) - raspoređuje čvorove u pretince po vrijednosti
# 2. Sortiranje pretinaca - svaki pretinac se sortira insertion sortom
# 3. Gather (skupljanje) - spaja sve pretince u jednu sortiranu listu
#
# Prepoznavanje:
# 1. Prvo se pronalaze min i max vrijednost (za normalizaciju)
# 2. Svaki čvor se dodjeljuje pretincu prema formuli:
#    idx = (vrijednost - min) * (broj_pretinaca - 1) / (max - min)
# 3. Svaki pretinac je zasebna povezana lista (head pokazivač)
# 4. Čvorovi se umetnu na POČETAK pretinca (O(1) operacija)
# 5. Nakon sortiranja pretinaca, spajaju se u jednu listu
# ==============================================================================

    def bucket_sort(self, bucket_count=5):
        """
        Sortira listu koristeći Bucket Sort algoritam (rastući poredak).
        
        Argumenti:
            bucket_count - broj pretinaca (zadano 5)
        
        Vraća:
            None - sortira listu na mjestu (in-place)
        """
        head = self.head
        if head is None or head.next is None:
            return

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
            return

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
                # (koristimo isti insertion_sort ali na head-u pretinca)
                buckets[i] = self._insertion_sort_on_head(buckets[i])

                # Ako je ovo prvi pretinac koji spajamo, postavi njegovu glavu kao glavnu glavu
                if sorted_head is None:
                    sorted_head = buckets[i]
                else:
                    # Inače, nadoveži ga na kraj prethodno spojenih pretinaca
                    sorted_tail.next = buckets[i]

                # Pomakni 'tail' pokazivač na kraj novonastale sortirane liste
                sorted_tail = buckets[i]
                while sorted_tail.next is not None:
                    sorted_tail = sorted_tail.next

        # Ažuriraj glavu originalnog objekta liste
        self.head = sorted_head

    def _insertion_sort_on_head(self, head):
        """
        Pomoćna metoda: Sortira povezanu listu na temelju glave (head) pomoću Insertion Sorta.
        Koristi se za sortiranje pojedinačnih pretinaca u Bucket Sortu.
        
        Argumenti:
            head - glava liste koju treba sortirati
        
        Vraća:
            Novu glavu sortirane liste
        """
        if head is None or head.next is None:
            return head

        sorted_head = None
        current = head
        
        while current is not None:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        return sorted_head
