class Solution(object):
    def isAnagram(self, s, t):
        # 1. PROVJERA DULJINE
        # Ako riječi nemaju isti broj slova, ne mogu biti anagrami. Odmah kraj.
        if len(s) != len(t):
            return False
            
        # 2. INICIJALIZACIJA BROJAČA
        # 'count_map' će čuvati informaciju: { SLOVO : KOLIKO_PUTA_SE_POJAVLJUJE }
        mapa = {}
        
        # 3. PUNJENJE RJEČNIKA (Prva riječ 's')
        for char in s:
            if char in mapa:
                # Ako je slovo već u tablici, samo povećaj brojač za 1
                mapa[char] += 1
            else:
                # Ako je slovo novo, postavi brojač na 1
                mapa[char] = 1
                
        # 4. PRAŽNJENJE RJEČNIKA I PROVJERA (Druga riječ 't')
        for char in t:
            # KLJUČNA PROVJERA:
            # Ako slova uopće nema u tablici ILI smo ga već potrošili (brojač je 0)
            if char not in mapa or mapa[char] == 0:
                # To znači da 't' ima neko slovo viška ili slovo koje 's' nema
                return False
                
            # Ako je slovo tu, smanji mu broj dostupnih kopija za 1
            mapa[char] -= 1
            
        # 5. KRAJ
        # Ako smo prošli cijelu riječ 't' bez greške, znači da su slova identična
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
