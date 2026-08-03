# ==============================================================================
# VERZIJA 3: DVOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# ==============================================================================
# Opis:
# Ova metoda sortira dvostruko povezanu listu silaznim redoslijedom (od najvećeg 
# prema najmanjem) koristeći bubble sort algoritam. Sortiranje se postiže isključivo 
# zamjenom podataka (.data) između čvorova, dok pokazivači (.next i .prev) ostaju 
# nepromijenjeni. Čvorovi fizički ostaju na istim mjestima u memoriji, samo im se 
# mijenjaju vrijednosti.
#
# Prepoznavanje:
# 1. Čvorovi imaju i '.next' i '.prev' atribute (dvostruko povezana lista).
# 2. Kod je KOD-ZA-KOD IDENTIČAN verziji 1 (jednostruka lista sa zamjenom podataka).
# 3. Budući da mijenjamo samo '.data', struktura veza u memoriji ostaje netaknuta.
#    To znači da pokazivač '.prev' uopće ne moramo dirati niti koristiti unutar petlje!
# 4. Metoda radi na principu dvije ugnježđene while petlje (bubble sort).
#
# Vremenska složenost: O(N²) u najgorem slučaju
# Prostorna složenost: O(1) - sortiranje na mjestu
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def bubble_sort_data_swap(self):
        """Sortira dvostruko povezanu listu silazno koristeći zamjenu podataka (data swap)."""
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
# VERZIJA 4: DVOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# ==============================================================================
# Opis:
# Ova metoda također sortira dvostruko povezanu listu silaznim redoslijedom, 
# ali za razliku od verzije 3, ovdje se ne mijenjaju podaci unutar čvorova 
# već se fizički mijenjaju pokazivači (.next i .prev) kako bi čvorovi zamijenili 
# mjesta u memoriji. Zbog dvostrukih pokazivača, implementacija je složenija 
# jer treba ažurirati oba smjera veza.
#
# Prepoznavanje:
# 1. Mijenjaju se i '.next' i '.prev' pokazivači čvorova kako bi zamijenili mjesta.
# 2. Za razliku od jednostruke liste (Verzija 2), ovdje nam NE TREBA vanjska 
#    lokalna varijabla 'prev'. Zašto? Zato što svaki čvor već sam po sebi zna 
#    tko mu je prethodnik putem svog atributa 'current.prev'.
# 3. Moramo paziti na rubne slučajeve (ako čvorovi imaju susjede s lijeve ili 
#    desne strane).
# 4. Posebna pažnja se vodi na ažuriranje 'self.head' kada se mijenjaju prva 
#    dva čvora u listi.
#
# Vremenska složenost: O(N²) u najgorem slučaju
# Prostorna složenost: O(1) - sortiranje na mjestu
# ==============================================================================

    def bubble_sort_pointer_swap(self):
        """Sortira dvostruko povezanu listu silazno koristeći zamjenu pokazivača (pointer swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                
                # Silazni poredak
                if current.data < next_node.data:
                    swapped = True
                    
                    # 1. Spremamo vanjske susjede ovog para (ako postoje)
                    lijevi_susjed = current.prev
                    desni_susjed = next_node.next
                    
                    # 2. Međusobno prespajamo naša dva čvora (mijenjaju mjesta)
                    next_node.next = current
                    current.prev = next_node
                    
                    # 3. Spajamo ih s ostatkom liste (lijevo i desno)
                    current.next = desni_susjed
                    if desni_susjed is not None:
                        desni_susjed.prev = current
                        
                    next_node.prev = lijevi_susjed
                    if lijevi_susjed is not None:
                        lijevi_susjed.next = next_node
                    else:
                        # Ako s lijeve strane nema nikoga, 'next_node' je postao novi početak liste!
                        self.head = next_node
                    
                    # Budući da je current otišao desno, a petlja na kraju kruga radi 'current = current.next',
                    # on bi preskočio jedan čvor. Zato ga ovdje ne pomičemo, nego ostaje isti.
                else:
                    current = current.next


# ==============================================================================
# TABLICA ZA USPOREDBU SVE 4 VERZIJE
# ==============================================================================
# | Karakteristika          | Verzija 1          | Verzija 2          | Verzija 3          | Verzija 4          |
# |-------------------------|--------------------|--------------------|--------------------|--------------------|
# | Tip liste              | Jednostruka        | Jednostruka        | Dvostruka          | Dvostruka          |
# | Mijenja .data?         | DA                 | NE                 | DA                 | NE                 |
# | Mijenja .next?         | NE                 | DA                 | NE                 | DA                 |
# | Mijenja .prev?         | N/A                | N/A                | NE                 | DA                 |
# | Težina implementacije  | Jednostavna        | Kompleksna         | Jednostavna        | Vrlo kompleksna    |
# | Potreban 'prev'?       | NE                 | DA                 | NE                 | NE (ima .prev)     |
# | Ažuriranje head?       | NE                 | DA                 | NE                 | DA                 |
# | Brzina (mali podaci)   | Ista (O(N²))       | Ista (O(N²))       | Ista (O(N²))       | Ista (O(N²))       |
# | Brzina (veliki podaci) | Sporije (kopiranje)| Brže (pokazivači)  | Sporije (kopiranje)| Brže (pokazivači)  |
# | Pogodnost za tipove    | int, float, bool   | string, list, dict | int, float, bool   | string, list, dict |
# | Čitljivost koda        | Visoka             | Srednja            | Visoka             | Niska              |
# | Vjerojatnost greške    | Mala               | Veća               | Mala               | Vrlo velika        |
# | Prednost               | Jednostavan        | Brži za velike podatke | Jednostavan, radi i na dvostrukoj | Brži za velike podatke, radi na dvostrukoj |
# | Nedostatak             | Kopira podatke     | Kompleksan         | Kopira podatke     | Vrlo kompleksan, lako za pogriješiti |
# ==============================================================================

# ==============================================================================
# NAPOMENA:
# Sve 4 verzije imaju ISTU vremensku složenost O(N²) u najgorem slučaju, ali se 
# razlikuju u performansama i kompleksnosti implementacije.
#
# Preporuka za korištenje:
# - Verzija 1: Preporuča se za jednostruke liste s malim podacima (int, float).
# - Verzija 2: Preporuča se za jednostruke liste s velikim podacima (stringovi, liste).
# - Verzija 3: Preporuča se za dvostruke liste s malim podacima.
# - Verzija 4: Preporuča se za dvostruke liste s velikim podacima (ali uz oprez!).
#
# U najboljem slučaju (već sortirana lista), sve verzije imaju složenost O(N)
# jer se zaustavljaju nakon jednog prolaza kada 'swapped' ostane False.
#
# VAŽNO: Verzije 3 i 4 (dvostruko povezane liste) imaju smisla samo ako nam 
# trebaju .prev pokazivači za druge operacije (npr. brisanje, umetanje s lijeva).
# Ako nam .prev ne treba, jednostruka lista (Verzija 1 ili 2) je bolji izbor 
# jer troši manje memorije i jednostavnija je za održavanje.
# ==============================================================================
