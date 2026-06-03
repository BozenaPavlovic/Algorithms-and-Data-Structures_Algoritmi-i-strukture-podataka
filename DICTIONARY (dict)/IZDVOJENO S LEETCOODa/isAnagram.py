
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
            
        counter = {}
        
        # Brojimo slova u prvoj riječi
        for slovo in s:
            if slovo in counter:
                counter[slovo] += 1
            else:
                counter[slovo] = 1
                
        # Oduzimamo slova iz druge riječi
        for slovo in t:
            # Ako slova uopće nema u prvoj riječi, ili smo ga već potrošili
            if slovo not in counter or counter[slovo] == 0:
                return False
            counter[slovo] -= 1
            
        return True








#brute force 
class Solution(object):
    def isAnagram(self, s, t):
        # 1. Ako riječi nisu iste duljine, odmah znamo da NISU anagrami
        if len(s) != len(t):
            return False
        
        # 2. Pretvorimo stringove u liste slova (Python magija umjesto for petlje)
        so1 = list(s)
        so2 = list(t)
        
        # 3. Sortiramo ih (tvoja odlična ideja!)
        so1.sort()
        so2.sort()
        
        # 4. Usporedimo ih i vratimo True ako su iste, ili False ako nisu
        return so1 == so2
