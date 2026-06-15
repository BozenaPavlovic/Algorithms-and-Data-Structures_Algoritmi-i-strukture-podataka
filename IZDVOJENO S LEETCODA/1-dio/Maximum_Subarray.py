# ==============================================================================
# ZADATAK: 53. Maximum Subarray (Maksimalni podniz)
#
# KATEGORIJA: LISTE / DINAMIČKO PROGRAMIRANJE (Kadaneov algoritam)
#
# TEKST ZADATKA:
# Zadan je niz cijelih brojeva 'nums'. Potrebno je pronaći uzastopni podniz 
# (koji sadrži barem jedan broj) koji ima najveći zbroj elemenata te vratiti taj zbroj.
#
# PRIMJER:
# Unos: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Izlaz: 6
# Objašnjenje: Uzastopni podniz [4, -1, 2, 1] ima najveći zbroj = 6.
#
# ZAHTJEV NA ISPITU / LEETCODE-u:
# Zadatak se mora riješiti u samo jednom prolazu kroz niz (vremenska složenost O(n)).
# Zamka: Niz može sadržavati isključivo negativne brojeve, zbog čega se varijable 
# za zbroj NE SMIJU inicijalizirati na 0, već na prvi element niza.
# ==============================================================================

def maxSubArray(nums):
    # Inicijaliziramo oba zbroja na prvi element niza.
    # Ako bismo stavili 0, a niz se sastoji samo od npr. [-2, -3], algoritam bi krivo vratio 0.
    current_sum = nums[0]
    max_sum = nums[0]

    # Krećemo od drugog elementa (indeks 1) jer smo prvi već uzeli u obzir
    for i in range(1, len(nums)):
        # KLJUČNA ODLUKA ALGORITMA:
        # Gledamo isplati li nam se nastaviti zbrajati na trenutni podniz (current_sum + nums[i])
        # ili nam taj prethodni dio samo šteti (jer je otišao u minus), pa je bolje da 
        # trenutni broj 'nums[i]' započne potpuno novi podniz.
        current_sum = max(nums[i], current_sum + nums[i])

        # Ako je trenutni lokalni zbroj postao veći od dosadašnjeg povijesnog maksimuma,
        # ažuriramo naš konačni rezultat 'max_sum'
        if current_sum > max_sum:
            max_sum = current_sum

    # Vraćamo najveći pronađeni zbroj podniza
    return max_sum
