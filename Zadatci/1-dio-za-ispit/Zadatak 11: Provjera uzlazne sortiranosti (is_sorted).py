# ==============================================================================
# ZADATAK 11: Metoda is_sorted() za povezanu listu
#
# TEKST ZADATKA:
# Napišite metodu is_sorted() za klasu jednostruko povezane liste (iste kao 
# u 10. zadatku) koja provjerava je li lista uzlazno sortirana. Metoda vraća 
# True ako je lista sortirana ili ako sadrži samo jedan element, a False ako 
# je prazna ili ako nije sortirana.
# ==============================================================================

def is_sorted(self):
    # empty list -> False
    if self.head is None:
        return False

    # one element -> True
    if self.head.next_node is None:
        return True

    curr = self.head

    while curr.next_node is not None:
        if curr.data > curr.next_node.data:
            return False

        curr = curr.next_node

    return True
