# ==============================================================================
# VERZIJA 1: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA PODATAKA (DATA SWAP)
# 
# PREPOZNAVANJE: 
# 1. Koristi se samo 'current.next' (lista ide samo prema naprijed, nema '.prev').
# 2. Zamjena se vrši isključivo nad '.data' atributima: 
#    'current.data, next_node.data = next_node.data, current.data'
# 3. Pokazivači '.next' se NE MIJENJAJU. Čvorovi ostaju na istim mjestima u memoriji.
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_single_data(head):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        current = head
        
        while current.next is not None:
            next_node = current.next
            # Silazni poredak: ako je trenutni manji od idućeg, mijenjaj podatke
            if current.data < next_node.data:
                current.data, next_node.data = next_node.data, current.data
                swapped = True
            current = current.next
            
    return head


# ==============================================================================
# VERZIJA 2: JEDNOSTRUKO POVEZANA LISTA + ZAMJENA POKAZIVAČA (POINTER SWAP)
# 
# PREPOZNAVANJE:
# 1. Vrijednosti '.data' se nigdje ne prepisuju (zaključane su).
# 2. Moramo imati 'prev' varijablu (to je obična lokalna varijabla u petlji, NIJE atribut čvora!).
#    Ona nam treba jer kad zamijenimo dva čvora, čvor ispred njih mora pokazivati na novi početak tog para.
# 3. Fizički se mijenjaju '.next' pokazivači kako bi čvorovi zamijenili mjesta u memoriji.
# ==============================================================================

def bubble_sort_single_pointers(head):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        current = head
        prev = None  # Prati čvor koji se nalazi ispred 'current'
        
        while current.next is not None:
            next_node = current.next
            
            # Silazni poredak
            if current.data < next_node.data:
                swapped = True
                
                # PRESPOAVANJE POKAZIVAČA:
                current.next = next_node.next
                next_node.next = current
                
                # Ako smo mijenjali prva dva čvora u listi, moramo ažurirati 'head'
                if prev is None:
                    head = next_node
                else:
                    prev.next = next_node
                
                # Nakon zamjene, čvorovi su zamijenili mjesta u memoriji.
                # 'next_node' je sada ispred 'current', pa 'prev' postaje 'next_node'.
                prev = next_node
            else:
                # Ako nije bilo zamjene, samo pomičemo oba pokazivača naprijed
                prev = current
                current = current.next
                
    return head

