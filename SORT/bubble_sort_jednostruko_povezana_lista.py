# ==============================================================================
# VERZIJA 1: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# ==============================================================================
# Opis:
# Ova metoda sortira jednostruko povezanu listu silaznim redoslijedom (od najvećeg 
# prema najmanjem) koristeći bubble sort algoritam. Sortiranje se postiže isključivo 
# zamjenom podataka (.data) između čvorova, dok pokazivači (.next) ostaju nepromijenjeni.
# Čvorovi fizički ostaju na istim mjestima u memoriji, samo im se mijenjaju vrijednosti.
#
# Prepoznavanje:
# 1. Koristi se samo 'current.next' (lista ide samo prema naprijed, nema '.prev').
# 2. Zamjena se vrši isključivo nad '.data' atributima: 
#    'current.data, next_node.data = next_node.data, current.data'
# 3. Pokazivači '.next' se NE MIJENJAJU.
# 4. Metoda radi na principu dvije ugnježđene while petlje (bubble sort).
#
# Vremenska složenost: O(N²) u najgorem slučaju
# Prostorna složenost: O(1) - sortiranje na mjestu
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def bubble_sort_data_swap(self):
        """Sortira listu silazno koristeći zamjenu podataka (data swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                # Silazni poredak: ako je trenutni manji od idućeg, mijenjaj podatke
                if current.data < next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next


# ==============================================================================
# VERZIJA 2: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# ==============================================================================
# Opis:
# Ova metoda također sortira jednostruko povezanu listu silaznim redoslijedom, 
# ali za razliku od prve verzije, ovdje se ne mijenjaju podaci unutar čvorova 
# već se fizički mijenjaju pokazivači (.next) kako bi čvorovi zamijenili mjesta 
# u memoriji. Ova metoda zahtijeva praćenje prethodnog čvora ('prev') kako bi 
# se ispravno ažurirale veze prilikom zamjene.
#
# Prepoznavanje:
# 1. Vrijednosti '.data' se nigdje ne prepisuju (zaključane su).
# 2. Moramo imati 'prev' varijablu (to je obična lokalna varijabla u petlji, 
#    NIJE atribut čvora!). Ona nam treba jer kad zamijenimo dva čvora, čvor ispred 
#    njih mora pokazivati na novi početak tog para.
# 3. Fizički se mijenjaju '.next' pokazivači kako bi čvorovi zamijenili mjesta 
#    u memoriji.
# 4. Posebna pažnja se vodi na ažuriranje 'self.head' kada se mijenjaju prva 
#    dva čvora u listi.
#
# Vremenska složenost: O(N²) u najgorem slučaju
# Prostorna složenost: O(1) - sortiranje na mjestu
# ==============================================================================

    def bubble_sort_pointer_swap(self):
        """Sortira listu silazno koristeći zamjenu pokazivača (pointer swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            prev = None  # Prati čvor koji se nalazi ispred 'current'
            
            while current.next is not None:
                next_node = current.next
                
                # Silazni poredak
                if current.data < next_node.data:
                    swapped = True
                    
                    # PRESPOJAVANJE POKAZIVAČA:
                    current.next = next_node.next
                    next_node.next = current
                    
                    # Ako smo mijenjali prva dva čvora u listi, moramo ažurirati 'self.head'
                    if prev is None:
                        self.head = next_node
                    else:
                        prev.next = next_node
                    
                    # Nakon zamjene, čvorovi su zamijenili mjesta u memoriji.
                    # 'next_node' je sada ispred 'current', pa 'prev' postaje 'next_node'.
                    prev = next_node
                    # current ostaje isti (sada je iza next_node)
                else:
                    # Ako nije bilo zamjene, samo pomičemo oba pokazivača naprijed
                    prev = current
                    current = current.next


# ==============================================================================
# TABLICA ZA USPOREDBU DVIJU VERZIJA
# ==============================================================================
# | Karakteristika          | Data Swap (Verzija 1) | Pointer Swap (Verzija 2) |
# |-------------------------|-----------------------|--------------------------|
# | Mijenja .data?         | DA                    | NE                       |
# | Mijenja .next?         | NE                    | DA                       |
# | Težina implementacije  | Jednostavna           | Kompleksna               |
# | Potreban 'prev'?       | NE                    | DA                       |
# | Ažuriranje self.head?  | NE                    | DA (kod zamjene prva 2)  |
# | Brzina (mali podaci)   | Ista (O(N²))          | Ista (O(N²))             |
# | Brzina (veliki podaci) | Sporije (kopiranje)   | Brže (samo pokazivači)   |
# | Pogodnost za tipove    | int, float, bool      | string, list, dict       |
# | Čitljivost koda        | Visoka                | Srednja                  |
# | Vjerojatnost greške    | Mala                  | Veća (zbog pokazivača)   |
# ==============================================================================

# ==============================================================================
# NAPOMENA:
# Obje verzije imaju ISTU vremensku složenost O(N²) u najgorem slučaju, ali se
# razlikuju u performansama kada su podaci unutar čvorova veliki (npr. dugi 
# stringovi, velike liste, rječnici). Pointer swap je tada efikasniji jer ne 
# kopira podatke već samo premješta pokazivače.
# 
# U najboljem slučaju (već sortirana lista), obje verzije imaju složenost O(N)
# jer se zaustavljaju nakon jednog prolaza kada 'swapped' ostane False.
# ==============================================================================
