# ==============================================================================
# ZADATAK: 83. Remove Duplicates from Sorted List
#
# TEKST ZADATKA:
# Zadan je početak (head) sortirane verižne liste. Potrebno je ukloniti sve
# duplikate tako da se svaki jedinstveni element pojavi samo jednom. 
# Lista nakon modifikacije mora ostati sortirana, a funkcija vraća njezin početak.
#
# PRIMJER:
# Unos: head = [1, 1, 2, 3, 3]
# Izlaz: [1, 2, 3]
#
# ZAHTJEV NA ISPITU:
# Budući da je lista već sortirana, svi duplikati se nalaze odmah jedan pored drugog.
# Zadatak se rješava *in-place* (prespajanjem veza) u jednom jedinom prolazu kroz listu.
# Vremenska složenost je O(n), a prostorna složenost je O(1).
# ==============================================================================

def deleteDuplicates(head):
    # Pokazivač s kojim prolazimo kroz listu, kreće od glave (head)
    curr = head

    # Petlja radi sve dok imamo trenutni čvor I čvor nakon njega.
    # Ako je lista prazna ili ima samo 1 element, petlja se uopće neće pokrenuti.
    while curr is not None and curr.next is not None:
        # Uspoređujemo vrijednost trenutnog čvora s vrijednošću idućeg čvora
        if curr.val == curr.next.val:
            # Ako su vrijednosti iste, pronašli smo duplikat!
            # Preskačemo idući čvor tako da .next pokazivač trenutnog čvora 
            # preusmjerimo na čvor koji se nalazi TEK NAKON idućeg čvora.
            curr.next = curr.next.next  
        else:
            # Ako vrijednosti nisu iste, trenutačni čvor je jedinstven.
            # Tek tada se smijemo sigurno pomaknuti na sljedeći čvor u listi.
            curr = curr.next  

    # Vraćamo početak liste koji je ostao isti, ali su iz niza izbačeni duplikati
    return head
