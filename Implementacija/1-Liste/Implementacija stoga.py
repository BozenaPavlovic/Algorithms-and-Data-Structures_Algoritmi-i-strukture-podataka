class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def top(self): # sometimes called "peek" method
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def delete(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        values.reverse()
        return '\n'.join(values) # new line used as separator for join



# Implementirajte strukturu podataka stog u Pythonu, naziva `Stack`, 
# korištenjem ugrađene Python strukture podataka `list` i **pripadajućih ugrađenih metoda** (https://docs.python.org/3/tutorial/datastructures.html). 
# Stog je struktura podataka koja funkcionira po principu LIFO (*Last In, First Out*), 
# što znači da će posljednji element koji je dodan u stog, prvi biti izbačen
