
class Solution(object):
    def groupAnagrams(self, strs):
        # 1. Kreiramo prazan rječnik za grupiranje
        # Format će biti -> { "sortirana_riječ" : [lista_originalnih_riječi] }
        anagram_groups = {}
        
        # 2. Prolazimo kroz svaku riječ u zadanom nizu
        for word in strs:
            # Magični trik: sortiramo slova u riječi i spajamo ih natrag u string.
            # Npr. "tea" postaje "aet". To je naš zajednički ključ!
            sorted_word = "".join(sorted(word))
            
            # 3. Ako taj sortirani ključ već postoji u rječniku,
            # samo dodajemo originalnu riječ u njegovu listu.
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            # Ako ključ ne postoji, kreiramo novu listu s tom trenutnom riječi.
            else:
                anagram_groups[sorted_word] = [word]
                
        # 4. Zadatak traži da vratimo samo grupe (liste riječi).
        # .values() iz rječnika izvlači točno ono što nam treba: sve liste bez njihovih ključeva.
        return list(anagram_groups.values())
