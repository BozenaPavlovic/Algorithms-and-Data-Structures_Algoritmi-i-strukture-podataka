class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item) # Dodajemo elemente na indeks 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop() # Vadimo posljednji element (koji je prvi bio dodan)
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values) # space used as separator for join
