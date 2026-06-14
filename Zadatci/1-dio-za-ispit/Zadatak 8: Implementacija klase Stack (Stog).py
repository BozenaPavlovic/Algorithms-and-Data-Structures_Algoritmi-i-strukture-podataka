# ==============================================================================
# ZADATAK 8: Klasa Stack (Stog)
#
# TEKST ZADATKA:
# Koristeći Python strukturu list (s pripadajućim ugrađenim funkcijama i operatorima)
# implementirajte stog (čija se veličina može dinamički mijenjati) kao klasu Stack 
# s metodama __init__, push, pop, peek i size.
# ==============================================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Pop iz praznog stoga")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
