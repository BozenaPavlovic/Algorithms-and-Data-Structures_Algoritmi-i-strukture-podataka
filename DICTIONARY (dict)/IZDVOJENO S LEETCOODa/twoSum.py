
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        podsjetnik = {} # Prazna tablica za pamćenje brojeva i njihovih indeksa
        
        for i in range(n):
            trenutni_broj = nums[i]
            fali_mi = target - trenutni_broj
            
            # Umjesto druge for petlje, samo pitamo rječnik:
            if fali_mi in podsjetnik:
                return [podsjetnik[fali_mi], i] # Vraćamo indeks nađenog para i trenutni indeks i
            
            # Ako ga nema, zapišemo trenutni broj i njegov indeks u tablicu
            podsjetnik[trenutni_broj] = i








# brute FORCE
class Solution(object):
    def twoSum(self, nums, target):
        n = len ( nums)
        
        
        for i in range (n):
           for j in range ( i + 1, n):
            if nums[i]+nums[j] == target:
                return  [i, j]
