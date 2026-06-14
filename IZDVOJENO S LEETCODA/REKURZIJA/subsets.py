# ==============================================================================
# ZADATAK: 78. Subsets (Backtracking / Generiranje svih podskupova)
#
# TEKST ZADATKA:
# Zadan je niz jedinstvenih cijelih brojeva 'nums'. Potrebno je vratiti sve 
# moguće podskupove (tzv. partitivni skup). Rezultat ne smije sadržavati 
# duplikate podskupova, a redoslijed nije bitan.
#
# PRIMJER:
# Unos: nums = [1, 2, 3]
# Izlaz: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
#
# ZAHTJEV NA ISPITU:
# Zadatak se rješava izgradnjom stabla odluka (State Space Tree). Za svaki broj 
# u nizu imamo točno dvije opcije: ili ćemo ga ubaciti u trenutni podskup 
# ili ćemo ga preskočiti. Vremenska složenost je O(2^n) jer se broj podskupova 
# dupla sa svakim novim elementom.
# ==============================================================================

def subsets(nums):
    result = []

    def backtrack(index, current_subset):
        # 1. BAZNI SLUČAJ: Kad indeks dođe do kraja niza (prošli smo sve brojeve)
        # To znači da smo donijeli odluku za svaki element i podskup je spreman.
        if index == len(nums):
            # KLJUČNO ZA ISPIT: Moramo napraviti plitku kopiju pomoću list()!
            # Ako bismo samo dodali 'current_subset', u rezultatu bismo dobili
            # prazne liste jer se originalna lista kroz rekurziju stalno mijenja.
            result.append(list(current_subset))  
            return

        # ODLUKA 1: Uključi trenutni broj (nums[index]) u naš podskup
        current_subset.append(nums[index])
        
        # Idemo dublje u rekurziju na idući broj s uključenim trenutnim brojem
        backtrack(index + 1, current_subset)

        # BACKTRACK KORAK (Povratak): Izbaci zadnji dodani broj van!
        # Ovo radimo jer se vraćamo korak unatrag u stablu odluka i čistimo 
        # listu kako bismo je pripremili za drugu opciju (opciju bez tog broja).
        current_subset.pop()

        # ODLUKA 2: Preskoči trenutni broj
        # Idemo dublje u rekurziju na idući broj, ali ovaj put bez tog broja u listi
        backtrack(index + 1, current_subset)

    # Algoritam pokrećemo od prvog elementa (indeks 0) i s praznom početnom listom
    backtrack(0, [])
    return result
