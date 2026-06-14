class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # 1. Kreiramo prazan rječnik koji će služiti kao naše skladište slova
        magazine_letters = {}
        
        # 2. PUNJENJE SKLADIŠTA: Prolazimo kroz časopis (magazine) i brojimo slova
        for char in magazine:
            if char in magazine_letters:
                magazine_letters[char] += 1 # Ako slovo već postoji, povećaj brojač
            else:
                magazine_letters[char] = 1  # Ako je slovo novo, postavi ga na 1
                
        # 3. TROŠENJE SLOVA: Prolazimo kroz pismo (ransomNote) koje želimo sastaviti
        for char in ransomNote:
            # PROVJERA: Ako tog slova uopće nema u časopisu ILI smo ga već potrošili (brojač je 0)
            if char not in magazine_letters or magazine_letters[char] == 0:
                return False # Nemoguće je sastaviti pismo!
                
            # Ako slovo postoji i imamo zaliha, uzmi jedno (smanji brojač za 1)
            magazine_letters[char] -= 1
            
        # 4. Ako smo uspješno prošli kroz cijelo pismo, znači da smo imali dovoljno slova
        return True
