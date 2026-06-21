# =============================================================================
# ISPITNI ZADATAK: Merge Sort na jednostruko povezanoj listi
#
# TEKST ZADATKA:
# Zadana je struktura čvora jednostruko povezane liste Node i pomoćna funkcija 
# merge(left, right) koja prima dvije već sortirane povezane liste i spaja ih 
# u jednu jedinstvenu sortiranu listu u vremenskoj složenosti O(n).
#
# Vaš zadatak je implementirati funkciju merge_sort(head) koja prima glavu 
# nesortirane povezane liste, rekurzivno je dijeli na pola tehnikom 
# Fast & Slow pokazivača (Zec i Kornjača), te vraća glavu potpuno sortirane 
# liste koristeći strategiju Podijeli pa vladaj (Divide and Conquer).
# =============================================================================

# =============================================================================
# Zadane strukture i pomoćne funkcije (NE MIJENJATI):
# =============================================================================

class Node:
    """Struktura čvora jednostruko povezane liste"""
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(left, right):
    """Pomoćna funkcija koja spaja dvije već sortirane liste"""
    dummy = Node(0)
    tail = dummy
    
    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
        
    tail.next = left if left else right
    return dummy.next

# =============================================================================
# MJESTO ZA VAŠE RJEŠENJE:
# =============================================================================

def merge_sort(head):
    # 1. BAZNI SLUČAJ: Ako je lista prazna ili ima 1 element, već je sortirana
    if not head or not head.next:
        return head
    
    # 2. PRONALAŽENJE SREDINE: Pokazivači 'slow' (1 korak) i 'fast' (2 koraka)
    slow = head
    fast = head.next  # 'fast' kreće korak ispred da se izbjegne beskonačna rekurzija
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 'slow' je sada na zadnjem čvoru prve polovice, a 'mid' je početak druge polovice
    mid = slow.next
    
    # 3. CIJEPANJE LISTE: Fizički prekidamo vezu između prve i druge polovice
    slow.next = None
    
    # 4. PODIJELI PA VLADAJ: Rekurzivno sortiramo obje polovice liste
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(mid)
    
    # 5. SPAJANJE: Koristimo zadanu 'merge' funkciju za spajanje rezultata
    return merge(left_sorted, right_sorted)
