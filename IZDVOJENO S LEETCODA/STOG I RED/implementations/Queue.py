class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Dodaje na kraj reda

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Uzima s početka reda (FIFO)
        else:
            raise IndexError("Dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)