# ODREĐIVANJE SLOŽENOSTI

#%%
def product_and_sum(arr):
    sum_total = 0
    product_total = 1
    for i in arr:
        sum_total += i
    for i in arr:
        product_total *= i

    # O(N)

#%%
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(str(i) + ", " + str(j))

    # O(N^2)

#%%
def print_pairs_2(arr):
    for i in arr:
        j = 1
        while j<len(arr):
            print(str(i) + ", " + str(j))
            j *= 2

    # O(N*log(N))


#%%
def print_unordered_pairs(arr): # Prebrojavanje ili prosječni slučaj!
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            print(str(i) + ", " + str(j))

    # O(N^2)

#%%
def print_unordered_pairs_2(arr1,arr2): # Dva različita ulaza!
    for i in arr1:
        for j in arr2:
            if i <= j:
                print(str(i) + ", " + str(j))

    # O(N*M)
Vrijeme: O(N·M), gdje je N = len(arr1), M = len(arr2).
Obrazloženje: vanjska petlja radi N puta, za svaki element izvodi se unutarnja petlja M puta → ukupno ≈ N×M operacija.
Posebno: ako M = N → O(N^2).


#%%
def print_unordered_pairs_3(arr1,arr2):
    for i in arr1:
        for j in arr1:
            for k in range(10000):
                if i <= j:
                    print(str(i) + ", " + str(j))

    # O(N^2)
Vrijeme: O(N^2), gdje je N = len(arr1).
Obrazloženje: dvije ugniježdene petlje preko arr1 daju ≈ N×N iteracija; unutarnja for k in range(10000) je konstanta (10000) → konstanta se zanemaruje u Big‑O.
Posebno: ako bi konstanta išla ovisno o N, utjecala bi na složenost; ovako ne utječe.




Uobičajeni složenosti i tipični primjeri
O(1) — konstanta: pristup elementu po indeksu, aritmetička operacija.
O(log n) — logaritamsko: binarno pretraživanje.
O(n) — linearno: jedan prolaz kroz niz.
O(n log n) — n puta log n: sortiranje uspoređivanjem (merge, quick average).
O(n^2) — kvadratno: dvije ugniježdene petlje (bubble sort worst).
O(n^3) — kubno: tri potpuno ugniježdene petlje.
O(2^n), O(n!) — eksponencijalno/faktorialno: brute‑force kombinatorni problemi.







