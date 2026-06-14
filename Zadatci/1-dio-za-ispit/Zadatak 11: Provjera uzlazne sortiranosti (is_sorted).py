# ==============================================================================
# ZADATAK 11: Metoda is_sorted() za povezanu listu
#
# TEKST ZADATKA:
# Napišite metodu is_sorted() za klasu jednostruko povezane liste (iste kao 
# u 10. zadatku) koja provjerava je li lista uzlazno sortirana. Metoda vraća 
# True ako je lista sortirana ili ako sadrži samo jedan element, a False ako 
# je prazna ili ako nije sortirana.
# ==============================================================================

    def is_sorted(self):
        # Ako je lista prazna, po tekstu zadatka vraća False
        if self.glava is None:
            return False
            
        # Ako sadrži samo jedan element, sortirana je (vraća True)
        if self.glava.sljedeci is None:
            return True
            
        curr = self.glava
        # Uspoređujemo trenutni čvor s njegovim sljedbenikom
        while curr.sljedeci is not None:
            if curr.podatak > curr.sljedeci.podatak:
                return False  # Čim nađemo element veći od idućeg, nije sortirano
            curr = curr.sljedeci
            
        return True
