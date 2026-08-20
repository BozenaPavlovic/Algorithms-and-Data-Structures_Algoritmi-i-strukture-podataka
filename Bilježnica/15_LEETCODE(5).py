Leetcode – preporučeni zadaci za vježbu
▪ Osnovna primjena
 1. Two Sum — Easy, sporo vs. brzo rješenje pomoću dict-a
• O(N²) → O(N) jer je u pozadini dict-a hash tablica
 242. Valid Anagram — Easy, frequency dict
 383. Ransom Note — Easy, brojanje znakova
▪ Divide & Conquer
 49. Group Anagrams — Medium, izvedeni ključ (sortirani string)
 347. Top K Frequent Elements — Medium, direktan nastavak primjera s predavanja
▪ Obratite pozornost na zadatak 1. koji lijepo pokazuje kako pravi izbor strukture
podataka kvadratno rješenje pretvara u linearno


1. Two Sum — Easy, sporo vs. brzo rješenje pomoću dict-a
• O(N²) → O(N) jer je u pozadini dict-a hash tablica
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            compliment = target - current
            if compliment in seen:
                return [seen[compliment],i]
            seen[current] = i  #ključ = current, a vrijednost = i
 

242. Valid Anagram — Easy, frequency dict
class Solution(object):
    # Input: s = "anagram", t = "nagaram"
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        mapa={}
        for char in s:
            if char in mapa:
                mapa[char] += 1
            else:
                mapa[char] = 1
        for char in t:
            if char not in mapa or mapa[char] == 0:
                return False
            mapa[char] -= 1
        return True
      
383. Ransom Note — Easy, brojanje znakova
▪ Divide & Conquer
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mc={}
        for char in magazine:
            if char in mc:
                mc[char] += 1
            else:
                mc[char] = 1
        for char in ransomNote:
            if char not in mc or mc[char] == 0:
                return False
            mc[char]-=1
        return True 

49. Group Anagrams — Medium, izvedeni ključ (sortirani string)
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution(object):
    def groupAnagrams(self, strs):
        ag={}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in ag:
                ag[sorted_word].append(word)
            else:
                ag[sorted_word] = [word]
        return list(ag.values())


347. Top K Frequent Elements — Medium, direktan nastavak primjera s predavanja
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 3
# Output: [1, 2, 3]
class Solution(object):
    def topKFrequent(self, nums, k):
        mapso = {}
        for num in nums:
            if num in mapso:
                mapso[num] += 1
            else:
                mapso[num] = 1
        sorted_items = sorted(mapso.items(), key=lambda x: x[1], reverse=True)
        result=[]
        for i in range (k):
            result.append(sorted_items[i][0])
        return result
