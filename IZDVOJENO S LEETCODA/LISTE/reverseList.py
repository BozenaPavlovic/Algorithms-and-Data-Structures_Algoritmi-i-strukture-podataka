# ==============================================================================
# ZADATAK: 206. Reverse Linked List
#
# TEKST ZADATKA:
# Zadan je početak (head) jednostruko verižne liste. Potrebno je okrenuti
# listu naopako (tako da zadnji čvor postane prvi, a prvi zadnji) i vratiti
# početak (head) nove, okrenute liste.
#
# PRIMJER:
# Unos: head = [1, 2, 3, 4, 5]
# Izlaz: [5, 4, 3, 2, 1]
#
# ZAHTJEV NA ISPITU:
# Zadatak se najčešće traži riješiti iterativno u jednom prolazu kroz listu
# s vremenskom složenošću O(n) i prostornom složenošću O(1) (in-place),
# što znači da se ne smije stvarati nova lista, već se samo prepravljaju veze.
# ==============================================================================

def reverseList(head):
    # Pokazivač na prethodni čvor (na početku je None jer prvi čvor postaje zadnji)
    prev = None
    # Pokazivač na trenutni čvor s kojim radimo
    curr = head

    while curr is not None:
        # 1. KORAK: Privremeno spremi ostatak liste da ne izgubiš vezu
        next_node = curr.next  
        
        # 2. KORAK: Okreni pokazivač trenutnog čvora unazad (prema 'prev')
        curr.next = prev  
        
        # 3. KORAK: Pomakni 'prev' pokazivač naprijed na trenutni čvor
        prev = curr  
        
        # 4. KORAK: Pomakni 'curr' pokazivač naprijed na sljedeći spremljeni čvor
        curr = next_node  

    # Kada 'curr' postane None (dođemo do kraja), 'prev' stoji na zadnjem čvoru
    # koji je sada postao nova glava (head) okrenute liste.
    return prev  
glava okrenute liste
