# ==============================================================================
# ZADATAK 10: Metoda pretrazivanje() za povezanu listu
#
# TEKST ZADATKA:
# Napišite metodu pretrazivanje() kao implementaciju jednostavnog linearnog 
# pretraživanja za klasu jednostruko povezane liste. Lista ima atribut glava, 
# i sastoji se od čvorova koji imaju atribute podatak i sljedeci. Metoda vraća 
# indeks (poziciju) elementa ako je u listi, a -1 ako element nije u listi.
# ==============================================================================

class JednostrukoPovezanaLista:
    def __init__(self):
        self.glava = None

    def pretrazivanje(self, element):
        curr = self.glava
        indeks = 0
        
        while curr is not None:
            if curr.podatak == element:
                return indeks
            curr = curr.sljedeci  # Napomena: u tekstu piše 'sljedeci'
            indeks += 1
            
        return -1
