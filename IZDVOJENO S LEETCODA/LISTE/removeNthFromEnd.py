# ==============================================================================
# ZADATAK: 19. Remove Nth Node From End of List
#
# TEKST ZADATKA:
# Zadan je početak (head) verižne liste. Potrebno je ukloniti N-ti čvor 
# brojeći od kraja liste i vratiti početak (head) tako modificirane liste.
#
# PRIMJER:
# Unos: head = [1, 2, 3, 4, 5], n = 2
# Izlaz: [1, 2, 3, 5] (uklonjen je broj 4 jer je on drugi odozdo)
#
# ZAHTJEV NA ISPITU:
# Zadatak treba riješiti u samo jednom prolazu kroz listu (vremenska složenost O(n))
# i bez korištenja dodatne memorije (prostorna složenost O(1)).
# ==============================================================================

def removeNthFromEnd(head, n):
    # Stvaramo lažni (dummy) čvor koji pokazuje na head. 
    # Ovo nas spašava od 'if' uvjeta u slučaju da moramo obrisati baš prvi čvor u listi.
    dummy = ListNode(0, head)  
    slow = dummy
    fast = dummy

    # 1. KORAK: Pomakni 'fast' pokazivač za 'n' koraka unaprijed.
    # Time stvaramo fiksni razmak (prozor) između 'slow' i 'fast' pokazivača.
    for i in range(n):
        fast = fast.next

    # 2. KORAK: Pomiči oba pokazivača istovremeno za jedno mjesto.
    # Kada 'fast' dođe do zadnjeg čvora u listi (jer mu je .next None),
    # naš 'slow' pokazivač će stajati TOČNO ISPRED čvora kojeg moramo obrisati.
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # 3. KORAK: Brisanje čvora.
    # Samo preusmjerimo .next pokazivač od 'slow' čvora da preskoči idući čvor.
    slow.next = slow.next.next

    # Vraćamo stvarni početak liste (ono što je iza lažnog dummy čvora)
    return dummy.next
