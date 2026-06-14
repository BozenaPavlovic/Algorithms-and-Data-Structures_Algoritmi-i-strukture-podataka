# ==============================================================================
# ZADATAK: 876. Middle of the Linked List
#
# TEKST ZADATKA:
# Zadan je početak (head) jednostruko verižne liste. Potrebno je pronaći
# i vratiti srednji čvor te liste. Ako lista ima paran broj elemenata (pa
# postoje dvije sredine), potrebno je vratiti drugu sredinu.
#
# PRIMJER 1 (Neparan broj elemenata):
# Unos: head = [1, 2, 3, 4, 5]
# Izlaz: [3, 4, 5] (čvor s vrijednošću 3 je točna sredina)
#
# PRIMJER 2 (Paran broj elemenata):
# Unos: head = [1, 2, 3, 4, 5, 6]
# Izlaz: [4, 5, 6] (sredine su 3 i 4, zadatak traži da vratimo drugu, tj. 4)
#
# ZAHTJEV NA ISPITU:
# Najefikasnije rješenje koristi tehniku dva pokazivača (Zec i Kornjača).
# Vremenska složenost je O(n) jer kroz listu prolazimo samo jednom, a 
# prostorna složenost je O(1) jer ne trošimo nikakvu dodatnu memoriju.
# ==============================================================================

def middleNode(head):
    # Inicijaliziramo oba pokazivača na početak liste
    slow = head
    fast = head

    # Petlja radi dok god 'fast' (Zec) ne dođe do kraja liste (None)
    # ili do zadnjeg čvora (čiji je .next jednak None)
    while fast is not None and fast.next is not None:
        slow = slow.next        # Kornjača: pomiče se za 1 korak naprijed
        fast = fast.next.next   # Zec: pomiče se za 2 koraka naprijed

    # Budući da Zec trči duplo brže od Kornjače, u trenutku kada Zec
    # stigne na sam kraj liste, Kornjača će se nalaziti točno na sredini!
    return slow
