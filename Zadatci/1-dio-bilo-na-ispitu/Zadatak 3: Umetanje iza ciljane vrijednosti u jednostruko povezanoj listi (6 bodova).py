# ==============================================================================
# ZADATAK 3: Umetanje iza zadanog elementa (6 bodova)
#
# TEKST ZADATKA:
# Implementirajte metodu insert_at_target(self, value, target) za strukturu 
# jednostruko povezane liste koja odrađuje umetanje novog čvora s vrijednosti 
# value iza čvora koji sadrži vrijednost target (ako takav čvor postoji). Ako 
# takav čvor ne postoji, funkcija ispisuje odgovarajuću poruku. Lista je 
# definirana atributom head (glava liste) i ima atribut size u kojem se prati 
# veličina liste, a čvorovi su iz klase Node.
# ==============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Ova metoda se piše unutar klase jednostruko povezane liste
def insert_at_target(self, value, target):
    current = self.head
    
    # Prolazimo kroz listu i tražimo target vrijednost
    while current is not None:
        if current.data == target:
            # Našli smo target čvor! Stvaramo novi čvor
            new_node = Node(value)
            # Novi čvor preuzima ono što je bilo iza trenutnog čvora
            new_node.next = current.next
            # Trenutni čvor sada usmjeravamo na novi čvor
            current.next = new_node
            
            # Ne zaboravi povećati veličinu liste i prekinuti funkciju
            self.size += 1
            return
            
        current = current.next
        
    # Ako je petlja završila, znači da target element ne postoji u listi
    print("Target not found in the list.")
