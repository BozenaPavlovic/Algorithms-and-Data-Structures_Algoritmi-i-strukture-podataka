# ==============================================================================
# ZADATAK 15: Proširivanje liste sumom susjednih čvorova
#
# TEKST ZADATKA:
# Napišite metodu prosiri koja će jednostruko povezanu linearnu listu proširiti 
# novim elementima na način da između svaka dva čvora liste doda novi čvor 
# čija će vrijednost biti jednaka sumi vrijednosti čvorova između kojih se dodaje.
#
# PRIMJER:
# Originalna lista: 2 8 12 9 7
# Proširena lista:  2 10 8 20 12 21 9 16 7
# ==============================================================================

    def prosiri(self):
        # Ako je lista prazna ili ima samo 1 element, nema se između čega zbrajati
        if self.glava is None or self.glava.sljedeci is None:
            return
            
        curr = self.glava
        
        # Petlja radi dok god postoji desni susjed
        while curr.sljedeci is not None:
            lijeva_vrijednost = curr.podatak
            desna_vrijednost = curr.sljedeci.podatak
            suma = lijeva_vrijednost + desna_vrijednost
            
            # Stvaramo novi čvor koji već pokazuje na desnog susjeda
            novi_cvor = Cvor(suma, curr.sljedeci)
            
            # Lijevi čvor sada usmjeravamo na naš novi čvor
            curr.sljedeci = novi_cvor
            
            # Pomakni curr na desnog susjeda (preskačemo novi čvor)
            curr = novi_cvor.sljedeci
