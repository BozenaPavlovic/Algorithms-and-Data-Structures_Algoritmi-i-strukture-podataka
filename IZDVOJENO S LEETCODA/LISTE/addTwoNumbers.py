# ==============================================================================
# ZADATAK: 2. Add Two Numbers
#
# TEKST ZADATKA:
# Zadane su dvije neprazne verižne liste koje predstavljaju dva nenegativna cijela
# broja. Znamenke su spremljene u obrnutom redoslijedu (glava liste je znamenka
# jedinice, pa desetice, itd.), a svaki čvor sadrži jednu znamenku.
# Potrebno je zbrojiti ta dva broja i vratiti rezultat u obliku verižne liste.
#
# PRIMJER:
# Unos: l1 = [2, 4, 3] (broj 342), l2 = [5, 6, 4] (broj 465)
# Izlaz: [7, 0, 8] (broj 807)
# Objašnjenje: 2+5=7, 4+6=10 (pišemo 0, 1 prenosimo), 3+4+1(prijenos)=8
#
# ZAHTJEV NA ISPITU:
# Liste mogu biti različitih duljina (npr. zbrajamo dvoznamenkasti i peteroznamenkasti broj).
# Algoritam mora proći kroz liste paralelno u jednom prolazu (vremenska složenost O(max(n, m))).
# Obavezno se koristi 'carry' varijabla za prijenos (ostatak) i Dummy čvor za gradnju rezultata.
# ==============================================================================

def addTwoNumbers(l1, l2):
    # Stvaramo lažni (dummy) početni čvor koji služi kao sidro za novu listu rezultata
    dummy = ListNode()
    # 'curr' je pokazivač s kojim gradimo listu i pomičemo se naprijed kako dodajemo znamenke
    curr = dummy
    # Varijabla za prijenos (kada je zbroj znamenki veći ili jednak 10, ovdje pamtimo 1)
    carry = 0  

    # Petlja radi dok god ima elemenata u l1 ILI u l2 ILI imamo preostali prijenos (carry > 0)
    # na samom kraju (npr. ako je zadnji zbroj bio 5 + 5 = 10, moramo stvoriti još jedan čvor za tu 1)
    while l1 is not None or l2 is not None or carry > 0:
        # Ako je jedna lista kraća i došla je do kraja (None), njezina vrijednost u zbroju je 0
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        # Izračunaj ukupan zbroj za trenutnu poziciju (uključujući i prijenos iz prethodnog koraka)
        total = val1 + val2 + carry
        
        # Cjelobrojno dijeljenje s 10 nam daje novi prijenos (npr. 13 // 10 = 1)
        carry = total // 10  
        
        # Ostatak dijeljenja s 10 nam daje znamenku koju upisujemo u čvor (npr. 13 % 10 = 3)
        digit = total % 10  

        # Stvori novi čvor s izračunatom znamenkom i nadoveži ga na rezultat
        curr.next = ListNode(digit)
        # Pomakni pokazivač rezultata na taj novoizgrađeni čvor
        curr = curr.next

        # Pomakni ulazne liste na njihove sljedeće čvorove, ali samo ako ti čvorovi postoje
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    # Vraćamo stvarni početak rezultata (preskačemo lažni dummy čvor na indeksu 0)
    return dummy.next
