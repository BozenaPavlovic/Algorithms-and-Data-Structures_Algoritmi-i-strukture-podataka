# ==============================================================================
# ZADATAK: 21. Merge Two Sorted Lists
#
# TEKST ZADATKA:
# Zadana su dva početka (list1 i list2) dviju već sortiranih verižnih lista.
# Potrebno je spojiti te dvije liste u jednu novu, jedinstvenu sortiranu listu.
# Nova lista mora nastati prespajanjem čvorova iz prve dvije liste (in-place).
#
# PRIMJER:
# Unos: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Izlaz: [1, 1, 2, 3, 4, 4]
#
# ZAHTJEV NA ISPITU:
# Zadatak se rješava u jednom prolazu kroz obje liste (vremenska složenost O(n + m)).
# Najvažniji trik je korištenje lažnog početnog čvora (Dummy Node) kako bismo
# izbjegli komplicirane provjere koji je čvor prvi na samom početku spajanja.
# ==============================================================================

def mergeTwoLists(list1, list2):
    # Stvaramo lažni (dummy) početni čvor. On služi kao fiksno sidro nove liste.
    dummy = ListNode()  
    # 'tail' (rep) je pokazivač koji uvijek pokazuje na zadnji čvor u novoj listi
    tail = dummy  

    # Petlja radi dok god u OBJE liste imamo elemenata za usporedbu
    while list1 is not None and list2 is not None:
        # Uspoređujemo vrijednosti na trenutnim čvorovima obiju lista
        if list1.val < list2.val:
            # Ako je vrijednost u prvoj listi manja, nadoveži taj čvor na novu listu
            tail.next = list1
            # Pomakni pokazivač prve liste na njezin idući čvor
            list1 = list1.next
        else:
            # Ako je vrijednost u drugoj listi manja ili jednaka, nadoveži taj čvor
            tail.next = list2
            # Pomakni pokazivač druge liste na njezin idući čvor
            list2 = list2.next
            
        # Bez obzira s koje smo liste uzeli čvor, pomičemo rep nove liste korak naprijed
        tail = tail.next  

    # Kada se petlja prekine, to znači da je jedna od lista potpuno ispražnjena.
    # Sve preostale čvorove iz liste koja NIJE prazna samo nadovežemo na kraj (tail).
    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    # Vraćamo stvarni početak nove spojene liste.
    # 'dummy' je bio samo lažni čvor (pokretač), pa je stvarna glava na 'dummy.next'.
    return dummy.next
