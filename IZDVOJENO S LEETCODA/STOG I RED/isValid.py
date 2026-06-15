# ==============================================================================
# ZADATAK: 20. Valid Parentheses (Valjane zagrade)
#
# KATEGORIJA: STRUKTURE PODATAKA / STOG (STACK)
# (Napomena: Koristi LIFO princip - zadnja otvorena zagrada se mora prva zatvoriti)
#
# TEKST ZADATKA:
# Dan je niz znakova 's' koji sadrži samo znakove '(', ')', '{', '}', '[' i ']'.
# Potrebno je odrediti je li ulazni niz valjan.
# Niz je valjan ako:
#   1. Otvorene zagrade moraju biti zatvorene istom vrstom zagrada.
#   2. Otvorene zagrade moraju biti zatvorene ispravnim redoslijedom.
#   3. Svaka zatvorena zagrada ima odgovarajuću otvorenu zagradu iste vrste.
#
# PRIMJERI:
# Unos: s = "()[]{}" -> Izlaz: True
# Unos: s = "(]"     -> Izlaz: False (Zagrade se ne podudaraju)
# Unos: s = "([)]"   -> Izlaz: False (Krivi redoslijed zatvaranja)
# Unos: s = "{[]}"   -> Izlaz: True
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Vremenska složenost mora biti O(n) jer kroz niz znakova prolazimo samo jednom.
# Stog je jedina struktura koja omogućuje prirodno praćenje ugniježđenih zagrada.
# ==============================================================================

def isValid(s):
    # Mapa (rječnik) koja povezuje zatvorene zagrade s njihovim odgovarajućim otvorenim zagradama.
    # Ovo nam omogućuje brzu provjeru parova bez hrpe if-else uvjeta.
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stog koristimo za pamćenje otvorenih zagrada koje tek trebaju biti zatvorene
    stack = Stack()  

    # Prolazimo kroz svaki znak u zadanom nizu
    for char in s:
        # PROVJERA 1: Je li trenutni znak ZATVORENA zagrada?
        # (Gledamo nalazi li se znak među ključevima u našoj bracket_map)
        if char in bracket_map:
            
            # RUBOVNI SLUČAJ: Ako je stog prazan, a naišli smo na zatvorenu zagradu,
            # to znači da ta zagrada nema svoj par na početku (npr. s = "]" ili s = "()]").
            if stack.is_empty():
                return False

            # Skidamo element s vrha stoga (to je zadnja otvorena zagrada na koju smo naišli)
            top_element = stack.pop()
            
            # PROVJERA 2: Odgovara li otvorena zagrada s vrha stoga našoj trenutnoj zatvorenoj zagradi?
            # Npr. ako je char = ']', onda bracket_map[']'] daje '[', pa 'top_element' mora biti '['.
            if bracket_map[char] != top_element:
                return False
                
        # PROVJERA 3: Ako znak NIJE zatvorena zagrada, znači da je OTVORENA zagrada.
        else:
            # Otvorene zagrade samo stavljamo na stog da čekaju svoj par
            stack.push(char)

    # KONAČNA PROVJERA: 
    # Nakon što smo prošli kroz cijeli niz, stog MORA biti potpuno prazan.
    # Ako je ostala ijedna otvorena zagrada na stogu (npr. s = "([]"), niz nije valjan.
    return stack.is_empty()
