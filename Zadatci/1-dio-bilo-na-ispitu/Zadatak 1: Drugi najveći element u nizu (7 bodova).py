# ==============================================================================
# ZADATAK 1: Drugi najveći element u nizu (7 bodova)
#
# TEKST ZADATKA:
# Napišite funkciju find_second_max(arr) koja u jednom prolasku kroz niz (Python 
# list) pronalazi drugi najveći element u nizu i vraća vrijednost elementa. 
# Pretpostavka je da niz može biti ili prazan ili sadržavati brojeve. Nije 
# dozvoljeno korištenje ugrađenih Python metoda za strukturu podataka list, 
# te ugrađenih Python funkcija max() i min().
# ==============================================================================

def find_second_max(arr):
    # Provjera duljine niza pomoću ugrađene len funkcije (jer ona smije)
    if len(arr) < 2:
        return None  # Barem 2 elementa su potrebna za drugi najveći
        
    # Inicijalizacija prva dva elementa na papiru
    if arr[0] > arr[1]:
        mx = arr[0]
        second_mx = arr[1]
    else:
        mx = arr[1]
        second_mx = arr[0]
        
    # Iteracija kroz ostatak niza od indeksa 2 nadalje (jedan jedini prolaz)
    for i in range(2, len(arr)):
        if arr[i] > mx:
            # Ako je trenutni veći od najvećeg, stari najveći postaje drugi najveći
            second_mx = mx
            mx = arr[i]
        elif arr[i] > second_mx:
            # Ispravljen bug iz tvog koda (pisalo je second_max umjesto second_mx)
            second_mx = arr[i]
            
    return second_mx
