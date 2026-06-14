# ==============================================================================
# ZADATAK 9: Klasa Queue (Red)
#
# TEKST ZADATKA:
# Koristeći Python strukturu list (s pripadajućim ugrađenim funkcijama i operatorima) 
# implementirajte red (čija se veličina može dinamički mijenjati) kao klasu Queue 
# s metodama __init__, enqueue, dequeue, peek i size.
# ==============================================================================

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("Dequeue iz praznog reda")
        return self.items.pop(0)  # FIFO princip - skida s početka liste

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)
