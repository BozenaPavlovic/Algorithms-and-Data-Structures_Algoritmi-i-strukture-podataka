class Stack:
    def __init__(self):
        self.SLL = SLL_simple()

    def is_empty(self):
        return self.SLL.head == None

    def push(self, item):
        self.SLL.add_first(item)

    def pop(self):
        if not self.is_empty():
            item = self.SLL.head.data
            self.SLL.delete_first()
            return item
        else:
            raise IndexError("Pop from an empty stack")

    def top(self):
        if not self.is_empty():
            return self.SLL.head.data
        else:
            return None

    def delete(self):
        self.SLL = SLL_simple()

    def __str__(self):
        temp = self.SLL.head  # Započinjemo ispis stoga s vrha
        out = ''
        while temp:
            if temp.next:
                out = out + str(temp.data) + '\n'
            else:
                out = out + str(temp.data)
            temp = temp.next  # Prijeđi na sljedeći čvor
        return out
