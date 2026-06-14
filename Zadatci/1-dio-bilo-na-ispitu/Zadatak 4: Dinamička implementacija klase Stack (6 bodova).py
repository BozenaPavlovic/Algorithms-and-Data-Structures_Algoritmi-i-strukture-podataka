# ==============================================================================
# ZADATAK 4: Implementacija klase Stack (6 bodova)
#
# TEKST ZADATKA:
# Koristeći Python strukturu list (s pripadajućim ugrađenim funkcijama i operatorima) 
# implementirajte stog (čija se veličina može dinamički mijenjati) kao klasu Stack 
# s metodama __init__, push, pop, peek i size. Metode pop i peek podižu 
# IndexError ako je stog prazan.
# ==============================================================================

class Stack:
    def __init__(self):
        # Inicijaliziramo praznu ugrađenu listu
        self.items = []
        
    def push(self, item):
        # Dodavanje elementa na vrh stoga
        self.items.append(item)
        
    def pop(self):
        # Skidanje elementa s vrha stoga uz obaveznu provjeru praznine
        if len(self.items) > 0:
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")
            
    def peek(self):
        # Vraćanje elementa s vrha stoga bez skidanja, uz provjeru praznine
        if len(self.items) > 0:
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
            
    def size(self):
        # Vraća trenutni broj elemenata na stogu
        return len(self.items)
