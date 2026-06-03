class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. BROJANJE: Kreiramo rječnik i izbrojimo frekvenciju svakog broja
        # Format -> { broj : koliko_puta_se_pojavljuje }
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
                
        # 2. SORTIRANJE: Pretvaramo rječnik u listu parova i sortiramo je.
        # count_map.items() nam daje listu torki, npr. [(broj, frekvencija)]
        # lambda x: x[1] govori Pythonu da sortira prema frekvenciji (vrijednosti).
        # reverse=True osigurava da najčešći brojevi budu na samom početku liste.
        sorted_items = sorted(count_map.items(), key=lambda x: x[1], reverse=True)
        
        # 3. SAKUPLJANJE REZULTATA: Uzimamo samo top K brojeva
        result = []
        for i in range(k):
            # sorted_items[i][0] uzima prvu stvar iz torke, a to je sam broj (ključ)
            result.append(sorted_items[i][0])
            
        return result
