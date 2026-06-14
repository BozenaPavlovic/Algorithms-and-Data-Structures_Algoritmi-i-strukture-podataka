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

class PovezanaListaSKešom:
    def __init__(self):
        self.glava = None
        # Atributi za spremanje zadnjeg upita (keš)
        self.zadnji_indeks = None
        self.zadnji_podatak = None

    def indeks(self, n):
        # Ako se traži ponovljeni indeks, odmah vrati keširanu vrijednost
        if self.zadnji_indeks == n and self.zadnji_indeks is not None:
            return self.zadnji_podatak
            
        curr = self.glava
        brojac = 0
        
        while curr is not None:
            if brojac == n:
                # Prije nego što vratimo vrijednost, spremamo je u keš
                self.zadnji_indeks = n
                self.zadnji_podatak = curr.podatak
                return curr.podatak
            curr = curr.sljedeci
            brojac += 1
            
        raise IndexError("Indeks izvan granica liste")
