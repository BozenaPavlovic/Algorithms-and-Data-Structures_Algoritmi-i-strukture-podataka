class MinStack:
    def __init__(self):
        self.items = Stack()  # Glavni stog za elemente
        self.min_items = Stack()  # Pomoćni stog koji prati minimum

    def push(self, val):
        self.items.push(val)

        # Ako je min_stog prazan ili je novi broj manji/jednak trenutnom minimumu
        if self.min_items.is_empty() or val <= self.min_items.top():
            self.min_items.push(val)
        else:
            # Inače ponovimo trenutni minimum na vrhu min_stoga
            self.min_items.push(self.min_items.top())

    def pop(self):
        if not self.items.is_empty():
            self.items.pop()
            self.min_items.pop()

    def top(self):
        return self.items.top()

    def getMin(self):
        return self.min_items.top()


    # Zadatak traži stog koji u svakom trenutku pamti i minimalni element. Trik za papir je da unutar klase imamo dva tvoja stoga: jedan za prave podatke (self.items), a drugi koji pamti povijest minimuma (self.min_items)