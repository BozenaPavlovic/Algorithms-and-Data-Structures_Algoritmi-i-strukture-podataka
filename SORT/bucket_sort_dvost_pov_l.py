# Bucket sort with doubly linked list buckets and data-swapping insertion sort

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = DNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def is_empty(self):
        return self.head is None

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def insertion_sort_by_data_swap(self):
        """
        Insertion sort on a doubly linked list using only data swaps.
        Because nodes have prev pointers, možemo učinkovito pomicati element
        ulijevo zamjenom podataka bez traženja prethodnika.
        """
        if self.head is None or self.head.next is None:
            return

        current = self.head.next
        while current:
            j = current
            # pomakni j ulijevo dok prethodni element ima veći podatak
            while j.prev and j.prev.data > j.data:
                j.prev.data, j.data = j.data, j.prev.data
                j = j.prev
            current = current.next

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return

    # Kreiramo n bucketa (doubly linked lists)
    buckets = [DoublyLinkedList() for _ in range(n)]

    # Distribuiraj elemente u buckete; osiguraj da bi < n
    for num in arr:
        bi = int(n * num)
        if bi >= n:  # u slučaju num == 1.0
            bi = n - 1
        buckets[bi].append(num)

    # Sortiraj svaki bucket koristeći insertion sort sa zamjenom podataka
    for b in buckets:
        b.insertion_sort_by_data_swap()

    # Konkateniraj rezultate natrag u arr
    idx = 0
    for b in buckets:
        cur = b.head
        while cur:
            arr[idx] = cur.data
            idx += 1
            cur = cur.next

# Primjer upotrebe
if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    bucket_sort(arr)
    print("Sorted array is:")
    print(" ".join(map(str, arr)))
