# ==============================================================================
# ZADATAK 10: Metoda pretrazivanje() za povezanu listu
#
# TEKST ZADATKA:
# Napišite metodu pretrazivanje() kao implementaciju jednostavnog linearnog 
# pretraživanja za klasu jednostruko povezane liste. Lista ima atribut glava, 
# i sastoji se od čvorova koji imaju atribute podatak i sljedeci. Metoda vraća 
# indeks (poziciju) elementa ako je u listi, a -1 ako element nije u listi.
# ==============================================================================

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def pretrazivanje(self, element):
        current = self.head
        index = 0

        while current is not None:
            if current.data == element:
                return index

            current = current.next_node
            index += 1

        return -1
