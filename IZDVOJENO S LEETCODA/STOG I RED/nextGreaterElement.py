# ==============================================================================
# ZADATAK: 496. Next Greater Element I (Sljedeći veći element I)
#
# KATEGORIJA: STRUKTURE PODATAKA / STOG (STACK) / MONOTONI STOG + HASH MAP
#
# TEKST ZADATKA:
# Zadana su dva niza 'nums1' i 'nums2' bez duplikata, gdje je 'nums1' podniz od 'nums2'.
# Za svaki element u 'nums1', potrebno je pronaći njegov "sljedeći veći element" u 'nums2'.
# Sljedeći veći element nekog broja 'x' u 'nums2' je PRVI veći broj koji se nalazi 
# DESNO od 'x' u tom istom nizu. Ako takav broj ne postoji, vrati -1 za taj element.
# Rezultat treba vratiti u obliku niza koji odgovara poretku elemenata u 'nums1'.
#
# PRIMJER:
# Unos: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
# Izlaz: [-1, 3, -1]
# Objašnjenje: 
#   - Za broj 4 u nums2: desno od njega je 2. Nema većeg broja, pa pišemo -1.
#   - Za broj 1 u nums2: desno od njega prva veća vrijednost je 3, pa pišemo 3.
#   - Za broj 2 u nums2: desno od njega nema elemenata, pa pišemo -1.
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Optimalno rješenje mora imati vremensku složenost O(n + m), gdje je n duljina 
# niza nums1, a m duljina niza nums2. To postižemo upotrebom monotonog stoga.
# ==============================================================================

def nextGreaterElement(nums1, nums2):
    # 'greater_map' (rječnik) će čuvati parove {broj: njegov_sljedeći_veći_broj}
    greater_map = {}
    # Stog koji koristimo radi po principu monotonog stoga (brojevi na njemu padaju)
    stack = Stack()

    # KORAK 1: Prolazimo kroz cijeli niz 'nums2' kako bismo svima našli sljedeći veći broj
    for num in nums2:
        # Dokle god stog nije prazan I trenutni broj 'num' je veći od broja na vrhu stoga:
        # To znači da je 'num' upravo postao PRVI veći element za sve te brojeve sa stoga.
        while not stack.is_empty() and num > stack.top():
            # Skidamo broj sa stoga jer smo mu uspješno našli par
            popped_num = stack.pop()
            # Bilježimo u mapu da je za 'popped_num' sljedeći veći upravo 'num'
            greater_map[popped_num] = num  

        # Nakon što smo skinuli sve manje brojeve, trenutni broj stavljamo na stog
        # jer on sada čeka da se u budućnosti pojavi netko veći od njega
        stack.push(num)

    # KORAK 2: Izgradnja konačnog rezultata za elemente iz niza 'nums1'
    result = []
    for num in nums1:
        # Ako za traženi broj imamo zapisan veći broj u mapi, dodajemo ga u rezultat
        if num in greater_map:
            result.append(greater_map[num])
        # Ako broja nema u mapi, znači da na stogu nikad nije dočekao veći broj od sebe, pa je rezultat -1
        else:
            result.append(-1)

    return result
