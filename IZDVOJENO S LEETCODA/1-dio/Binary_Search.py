# ==============================================================================
# ZADATAK: 1. Binary Search (Binarno pretraživanje)
#
# KATEGORIJA: BINARNO PRETRAŽIVANJE (BINARY SEARCH)
# (Napomena: Radi se na sortiranim LISTAMA/NIZOVIMA, koristi tehniku dva pokazivača)
#
# TEKST ZADATKA:
# Zadan je sortirani niz cijelih brojeva 'nums' u rastućem poretku i cijeli broj 'target'.
# Potrebno je napisati funkciju koja pretražuje 'target' unutar niza 'nums'.
# Ako 'target' postoji u nizu, vrati njegov indeks. U suprotnom, vrati -1.
#
# PRIMJER:
# Unos: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Izlaz: 4
# Objašnjenje: Broj 9 se nalazi na indeksu 4 u zadanom nizu.
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Niz MORA biti unaprijed sortiran. 
# Algoritam mora imati vremensku složenost O(log n), što znači da u svakom koraku
# prepolovimo prostor pretraživanja (zato ne smijemo koristiti klasičnu for petlju).
# ==============================================================================

def search(nums, target):
    # Postavljamo dva pokazivača na krajnje granice niza
    # 'left' kreće od prvog elementa (indeks 0)
    left = 0
    # 'right' kreće od zadnjeg elementa (indeks duljina niza - 1)
    right = len(nums) - 1

    # Petlja se izvršava sve dok se pokazivači ne susretnu ili mimoiđu
    while left <= right:
        # Pronalazimo indeks točno u sredini trenutnog raspona pretraživanja
        # Koristimo cjelobrojno dijeljenje (//) kako bismo dobili cijeli broj za indeks
        mid = (left + right) // 2  

        # SLUČAJ 1: Broj na sredini je točno onaj koji tražimo
        if nums[mid] == target:
            return mid  # Broj je pronađen, odmah vraćamo njegov indeks
            
        # SLUČAJ 2: Trenutni broj na sredini je MANJI od onog koji tražimo
        # Budući da je niz sortiran, to znači da se 'target' sigurno nalazi desno od 'mid'
        elif nums[mid] < target:
            left = mid + 1  # Odbacujemo lijevu polovicu, pomičemo lijevu granicu udesno
            
        # SLUČAJ 3: Trenutni broj na sredini je VEĆI od onog koji tražimo
        # Budući da je niz sortiran, to znači da se 'target' sigurno nalazi lijevo od 'mid'
        else:
            right = mid - 1  # Odbacujemo desnu polovicu, pomičemo desnu granicu ulijevo

    # Ako petlja završi, a nismo izvršili 'return mid', znači da su se granice 
    # mimoišle (left > right) i da traženi broj uopće ne postoji u nizu
    return -1  
