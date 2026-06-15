# ==============================================================================
# ZADATAK: 35. Search Insert Position (Pronađi poziciju za umetanje)
#
# KATEGORIJA: BINARNO PRETRAŽIVANJE (BINARY SEARCH)
#
# TEKST ZADATKA:
# Zadan je sortirani niz jedinstvenih cijelih brojeva 'nums' i ciljana vrijednost 'target'.
# Potrebno je vratiti indeks ako je 'target' pronađen. Ako nije, vrati indeks 
# na koji bi 'target' trebao biti umetnut tako da niz i dalje ostane sortiran.
#
# PRIMJER 1 (Broj postoji):
# Unos: nums = [1, 3, 5, 6], target = 5
# Izlaz: 2
#
# PRIMJER 2 (Broj NE postoji):
# Unos: nums = [1, 3, 5, 6], target = 2
# Izlaz: 1 (Broj 2 bi trebao doći između 1 i 3, što je indeks 1)
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Morate napisati algoritam s vremenskom složenošću O(log n).
# Ključno je razumjeti zašto pokazivač 'left' na samom kraju označava točno mjesto umetanja.
# ==============================================================================

def searchInsert(nums, target):
    # Postavljamo početne granice pretraživanja
    left = 0
    right = len(nums) - 1

    # Standardna petlja za binarno pretraživanje
    while left <= right:
        mid = (left + right) // 2

        # SLUČAJ 1: Pogodili smo točan broj, odmah vraćamo njegov indeks
        if nums[mid] == target:
            return mid  
            
        # SLUČAJ 2: Broj na sredini je manji od targeta, tražimo u desnoj polovici
        elif nums[mid] < target:
            left = mid + 1
            
        # SLUČAJ 3: Broj na sredini je veći od targeta, tražimo u lijevoj polovici
        else:
            right = mid - 1

    # MAGIČNI DIO ALGORITMA:
    # Ako petlja završi (što znači da broj NE postoji u nizu), pokazivači 'left' i 'right' 
    # će se mimoići. Zbog načina na koji pomičemo granice, pokazivač 'left' će se 
    # zaustaviti TOČNO na onom indeksu na koji bi 'target' trebao biti umetnut.
    return left
