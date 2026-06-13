class Queue:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.size = 0

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("The queue is full")
        else:
            if self.front == -1:  # in case the queue was empty
                self.front = 0
            self.items[(self.front + self.size) % self.max_size] = item
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        else:
            first_element = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.max_size  # update front
            self.size -= 1
            if self.size == 0:  # if queue becomes empty
                self.front = -1
            return first_element

    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        else:
            return self.items[self.front]

    def delete(self):
        self.items = [None] * self.max_size
        self.front = -1
        self.size = 0

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values) # space used as separator for join
