# ==============================================================================
# ZADATAK 7: Metoda indeks(n) s keširanjem
#
# TEKST ZADATKA:
# Implementirajte metodu indeks(n) koja vraća element na indeksu n jednostruko 
# povezane liste. Nadalje, s obzirom da je indeksiranje neefikasno kod povezanih 
# lista neka metoda indeks „kešira“ (sprema) zadnju dohvaćenu vrijednost i indeks 
# tako da ako se od te metode traži element na ponovljenom indeksu onda ona treba 
# samo vratiti prethodno spremljeni element (bez da ponovo prolazi kroz listu).
# ==============================================================================

class LinkedList:
    def __init__(self):
        self.head = None
        self.node = None
        self.index_value = -1

    def index(self, n):
        if n == self.index_value:
            return self.node

        current = self.head
        i = 0

        while current is not None:
            if i == n:
                self.index_value = n
                self.node = current
                return current

            current = current.next_node
            i += 1

        return None
