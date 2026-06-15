# ==============================================================================
# ZADATAK: 26. Remove Duplicates from Sorted Array (Uklanjanje duplikata iz sortiranog niza)
#
# KATEGORIJA: LISTE / DVA POKAZIVAČA (Tehnika čitanja i upisa u jednom prolazu)
#
# TEKST ZADATKA:
# Zadan je sortirani niz cijelih brojeva 'nums' u rastućem poretku. Potrebno je
# ukloniti duplikate "u mjestu" (in-place) tako da se svaki jedinstveni element
# pojavi samo jednom. Relativni poredak elemenata treba ostati isti.
# Funkcija treba vratiti broj jedinstvenih elemenata u nizu (neka to bude 'k').
#
# VAŽNA NAPOMENA:
# Ne smiješ stvarati novi niz niti koristiti dodatnu memoriju za kopiranje.
# Prvih 'k' mjesta u početnom nizu 'nums' mora sadržavati jedinstvene brojeve
# onim redoslijedom kojim su dolazili, dok ono što ostane iza njih nije bitno.
#
# PRIMJER:
# Unos: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Izlaz: funkcija vraća 5, a niz 'nums' se mijenja u [0, 1, 2, 3, 4, _, _, _, _, _]
# ==============================================================================

def removeDuplicates(nums):
    # Rubni slučaj: Ako je niz potpuno prazan, odmah vraćamo 0 jedinstvenih elemenata
    if not nums:
        return 0

    # Budući da je niz sortiran, prvi element (na indeksu 0) je UVIJEK jedinstven 
    # sam za sebe. Zato naš pokazivač za UPISIVANJE novih brojeva kreće od indeksa 1.
    write_index = 1

    # Pokazivač za ČITANJE ('read_index') prolazi redom kroz cijeli niz počevši od indeksa 1
    for read_index in range(1, len(nums)):
        # KLJUČNA PROVJERA:
        # Uspoređujemo trenutni broj s brojem koji se nalazi točno ispred njega.
        # Ako su RAZLIČITI, to znači da smo upravo otkrili novi jedinstveni broj!
        if nums[read_index] != nums[read_index - 1]:
            # Zapisujemo taj novi jedinstveni broj na poziciju koju čuva 'write_index'
            nums[write_index] = nums[read_index]
            # Pomičemo pokazivač upisa za jedno mjesto udesno kako bi bio spreman za idući novi broj
            write_index += 1  

    # Na samom kraju, vrijednost u 'write_index' predstavlja točan broj jedinstvenih 
    # elemenata koje smo posložili na početak niza. LeetCode će provjeravati elemente do tog indeksa.
    return write_index  
