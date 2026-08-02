# ==============================================================================
# VERZIJA 3: DVOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE:
# 1. Čvorovi imaju i '.next' i '.prev' atribute.
# 2. Kod je KOD-ZA-KOD IDENTIČAN verziji 1 (jednostruka lista sa zamjenom podataka).
# 3. Budući da mijenjamo samo '.data', struktura veza u memoriji ostaje netaknuta.
#    To znači da pokazivač '.prev' uopće ne moramo dirati niti koristiti unutar petlje!
# ==============================================================================

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def bubble_sort_double_data(head):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        current = head
        
        while current.next is not None:
            next_node = current.next
            # Silazni poredak: mijenjaju se samo podaci
            if current.data < next_node.data:
                current.data, next_node.data = next_node.data, current.data
                swapped = True
            current = current.next
            
    return head

# ==============================================================================
# VERZIJA 4: DVOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. Mijenjaju se i '.next' i '.prev' pokazivači čvorova kako bi zamijenili mjesta.
# 2. Za razliku od jednostruke liste (Verzija 2), ovdje nam NE TREBA vanjska lokalna varijabla 'prev'.
#    Zašto? Zato što svaki čvor već sam po sebi zna tko mu je prethodnik putem svog atributa 'current.prev'.
# 3. Moramo paziti na rubne slučajeve (ako čvorovi imaju susjede s lijeve ili desne strane).
# ==============================================================================

def bubble_sort_double_pointers(head):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        current = head
        
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
                    head = next_node
                
                # Budući da je current otišao desno, a petlja na kraju kruga radi 'current = current.next',
                # on bi preskočio jedan čvor. Zato ga ovdje ne pomičemo, nego ostaje isti.
            else:
                current = current.next
                
    return head

