# Bubble sort za jednostruko povezanu listu (data-swap verzija)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Dodaj vrijednost na kraj liste."""
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    @classmethod
    def from_list(cls, values):
        ll = cls()
        for v in values:
            ll.append(v)
        return ll

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def bubble_sort(self):
        """
        Bubble sort koji radi samo zamjenu polja `data` između čvorova.
        Efikasnija varijanta: prekidamo ako u prolazu nema zamjena i
        sužavamo opseg pomoću end markera.
        Sortira rastuće.
        """
        if self.head is None or self.head.next is None:
            return

        end = None
        while end != self.head:
            swapped = False
            cur = self.head
            while cur.next != end:
                if cur.data > cur.next.data:
                    # zamijeni samo podatke (data swap)
                    cur.data, cur.next.data = cur.next.data, cur.data
                    swapped = True
                cur = cur.next
            end = cur  # posljednji element je sada na svom mjestu
            if not swapped:
                break

# Primjer upotrebe
if __name__ == "__main__":
    values = [3, 1, 4, 2, 5]
    ll = LinkedList.from_list(values)
    print("Prije:", ll.to_list())
    ll.bubble_sort()
    print("Poslije:", ll.to_list())
