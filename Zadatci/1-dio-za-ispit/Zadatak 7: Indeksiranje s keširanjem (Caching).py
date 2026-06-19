# ==============================================================================
# ZADATAK 7: Metoda indeks(n) s keširanjem
#
# TEKST ZADATKA:
# Implementirajte metodu indeks(n) koja vraća element na indeksu n jednostruko 
# povezane liste. Nadalje, s obzirom da je indeksiranje neefikasno kod povezanih 
# lista neka metoda indeks „kešira“ (sprema) zadnju dohvaćenu vrijednost i indeks 
# tako da ako se od te metode traži element na ponovljenom indeksu onda ona treba 
# samo vratiti prethodno spremljeni element (bez da ponovo prolazi kroz listu).
# ==============================================================================

class Node:
    def __init__(self, data=None, next_node=None):
        # Čvor jednostruko povezane liste prema tvojoj sintaksi
        self.data = data
        self.next_node = next_node


def remove_nth_from_end(head, n):
    # Stvaramo lažni (dummy) čvor koji pokazuje na head. 
    # Ovo nas spašava od 'if' uvjeta u slučaju da moramo obrisati baš prvi čvor u listi.
    dummy = Node(0, head)  
    slow = dummy
    fast = dummy

    # 1. KORAK: Pomakni 'fast' pokazivač za 'n' koraka unaprijed.
    # Time stvaramo fiksni razmak (prozor) između 'slow' i 'fast' pokazivača.
    for i in range(n):
        fast = fast.next_node

    # 2. KORAK: Pomiči oba pokazivača istovremeno za jedno mjesto.
    # Kada 'fast' dođe do zadnjeg čvora u listi (jer mu je .next_node None),
    # naš 'slow' pokazivač će stajati TOČNO ISPRED čvora kojeg moramo obrisati.
    while fast.next_node is not None:
        slow = slow.next_node
        fast = fast.next_node

    # 3. KORAK: Brisanje čvora.
    # Samo preusmjerimo .next_node pokazivač od 'slow' čvora da preskoči idući čvor.
    slow.next_node = slow.next_node.next_node

    # Vraćamo stvarni početak liste (ono što je iza lažnog dummy čvora)
    return dummy.next_node
