
class Solution(object):
    def twoSum(self, nums, target):
        # 1. INIT HASH MAP (DICTIONARY)
        # Kreiramo prazan rječnik koji će služiti kao naša brza tablica.
        # Format tablice će biti -> { BROJ : INDEKS }
        seen = {} 
        
        # 2. LOOP THROUGH THE ARRAY
        # Prolazimo kroz cijeli niz brojeva koristeći njihov indeks (i).
        # len(nums) nam daje ukupan broj elemenata.
        for i in range(len(nums)):
            
            # Trenutni broj iz niza na kojem stoji petlja
            current = nums[i]
            
            # Izračunavamo "komplement" - broj koji nam očajnički fali 
            # da bismo s trenutnim brojem dobili traženi target.
            complement = target - current
            
            # 3. CHECK HASH MAP FOR COMPLEMENT
            # Najvažniji dio algoritma! Pitamo rječnik: "Imamo li već zapisan complement?"
            # Ova provjera u rječniku traje nevjerojatno kratko: O(1) vremena.
            if complement in seen:
                # Ako je unutra, našli smo par! 
                # Iz rječnika izvlačimo indeks od complementa pomoću seen[complement],
                # a 'i' je indeks našeg trenutnog broja. Vraćamo ih kao listu.
                return [seen[complement], i]
            
            # 4. UPDATE HASH MAP
            # Ako complement nije u rječniku, moramo trenutni broj spremiti u tablicu.
            # Ključ (Key) je sam broj 'current', a vrijednost (Value) je njegov indeks 'i'.
            seen[current] = i








# brute FORCE
class Solution(object):
    def twoSum(self, nums, target):
        n = len ( nums)
        
        
        for i in range (n):
           for j in range ( i + 1, n):
            if nums[i]+nums[j] == target:
                return  [i, j]
