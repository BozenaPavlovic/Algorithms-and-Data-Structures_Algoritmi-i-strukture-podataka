# ==============================================================================
# ZADATAK: 88. Merge Sorted Array (Spajanje sortiranih nizova)
#
# KATEGORIJA: LISTE / DVA POKAZIVAČA (Tehnika tri pokazivača s kraja)
#
# TEKST ZADATKA:
# Zadana su dva sortirana niza cijelih brojeva, 'nums1' i 'nums2', u rastućem poretku.
# Također su zadana dva cijela broja, 'm' i 'n', koji predstavljaju broj stvarnih 
# elemenata u 'nums1' i 'nums2'.
# Potrebno je spojiti 'nums2' unutar 'nums1' tako da konačni niz bude sortiran.
#
# VAŽNA NAPOMENA:
# Spajanje se radi "u mjestu" (in-place). To znači da NE smiješ stvarati novi niz,
# već modificiraš postojeći 'nums1'. Zato 'nums1' ima duljinu m + n, gdje su zadnjih 
# 'n' elemenata inicijalno postavljeni na 0 i služe kao prazan prostor za upis.
#
# PRIMJER:
# Unos: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
# Izlaz: nums1 se mijenja u [1, 2, 2, 3, 5, 6]
# ==============================================================================

def merge(nums1, m, nums2, n):
    # Postavljanje pokazivača na krajeve (idemo s desna na lijevo da ne prebrišemo podatke)
    p1 = m - 1      # Pokazivač na zadnji STVARNI element u nums1 (npr. broj 3)
    p2 = n - 1      # Pokazivač na zadnji element u nums2 (npr. broj 6)
    p = m + n - 1   # Pokazivač na zadnju skroz slobodnu poziciju na samom kraju nums1

    # Spajaj elemente dok god ima brojeva za usporedbu u OBA niza
    while p1 >= 0 and p2 >= 0:
        # Uspoređujemo koji je broj veći na trenutnim pozicijama p1 i p2.
        # Veći broj stavljamo na samo dno (kraj) niza nums1 jer tamo idu najveći brojevi.
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]  # Upisujemo veći broj iz nums1
            p1 -= 1               # Pomičemo pokazivač u nums1 ulijevo
        else:
            nums1[p] = nums2[p2]  # Upisujemo veći broj iz nums2
            p2 -= 1               # Pomičemo pokazivač u nums2 ulijevo
        p -= 1                    # U svakom slučaju, pomičemo pokazivač za upis ulijevo

    # RUBOVNI SLUČAJ: Što ako je u nums1 ponestalo elemenata (p1 < 0), a u nums2 još ima brojeva?
    # Budući da su ti preostali brojevi u nums2 manji od svih koje smo već posložili,
    # i već su sortirani, samo ih prebacimo (kopiramo) na preostala prazna mjesta na početku nums1.
    # (Napomena: Ako p2 prvi dođe do nule, elemente iz nums1 ne moramo micati jer su već na svom mjestu).
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
