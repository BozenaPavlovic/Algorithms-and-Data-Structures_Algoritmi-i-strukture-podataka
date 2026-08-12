# SELECTION SORT (NIZ / ARRAY – standardna verzija)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# slection sinlge pointer-swap
def selection_sort_single_pointers(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    tail = None
    start = head

    while start is not None:
        min_node = start
        prev_min = None
        prev = start
        current = start.next

        while current is not None:
            if current.data < min_node.data:
                min_node = current
                prev_min = prev
            prev = current
            current = current.next

        # remove min_node from unsorted
        if min_node == start:
            start = start.next
        else:
            prev_min.next = min_node.next

        # detach and append to sorted list
        min_node.next = None
        if sorted_head is None:
            sorted_head = min_node
            tail = min_node
        else:
            tail.next = min_node
            tail = min_node

    return sorted_head
    
# SELECTON SINGLE DATA SWAP
def selection_sort_single_data(head):
    if head is None or head.next is None:
        return head
    start = head
    while start is not None and start.next is not None:
        min_node = start
        current = start.next
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        if min_node != start:
            start.data, min_node.data = min_node.data, start.data
        start = start.next
    return head
    
# SELECTION SINGLE linked list
class Node:
    def __init__(self, data):
        self.data = data # Podatke spremamo u čvor
        self.next = None # Inicijaliziramo pokazivač na null (None)

class SLL_class:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, new_data):
        new_node = Node(new_data)   # Kreiramo novi čvor s novim podatkom
        if self.head is None:       # Poseban slučaj ako je lista prazna!
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # Novi čvor pokazuje na trenutni prvi član liste
            self.head = new_node        # Prvi član liste postaje novi čvor
        self.size += 1
    
    def delete_at_position(self, position):
        if position < 0 or position >= self.size:
            print("Invalid position.")
            return
        if position == 0:
            self.delete_first()
        elif position == self.size - 1:
            self.delete_last()
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next       # Pronalazimo prethodni čvor (u odnosu na traženi)
            current.next = current.next.next # Ažuriramo gdje pokazuje (preskačemo traženi čvor)
            self.size -= 1

    def delete_first(self):
    if self.head is None:
        return
    self.head = self.head.next
    self.size -= 1
    if self.head is None:
        self.tail = None

def delete_last(self):
    if self.head is None:
        return
    if self.head.next is None:
        self.head = None
        self.tail = None
        self.size = 0
        return
    cur = self.head
    while cur.next is not self.tail:
        cur = cur.next
    cur.next = None
    self.tail = cur
    self.size -= 1

    def find_max(self):
        if self.head is None:
            print("List is empty.")
            return None, None
        mx_idx = 0
        mx = self.head.data
        current = self.head
        idx = 0
        while current:
            if current.data > mx:
                mx = current.data
                mx_idx = idx
            current = current.next
            idx += 1
        return mx_idx, mx
    
        
    def selection_sort(self):
        sorted_list = SLL_class()
        while self.size > 0:
            mx_idx, mx = self.find_max()
            sorted_list.add_first(mx)
            self.delete_at_position(mx_idx)
        self.head = sorted_list.head
        self.tail = sorted_list.tail
        self.size = sorted_list.size

# SELECTION DOUBLE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL_class:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            # prazna lista
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node.prev = None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    def delete_at_position(self, position):
        if position < 0 or position >= self.size:
            print("Invalid position.")
            return
        if position == 0:
            self.delete_first()
            return
        if position == self.size - 1:
            self.delete_last()
            return
        node = self._node_at(position)
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1


    def find_max(self):
        if self.head is None:
            print("List is empty.")
            return None, None
        mx_idx = 0
        mx = self.head.data
        current = self.head
        idx = 0
        while current:
            if current.data > mx:
                mx = current.data
                mx_idx = idx
            current = current.next
            idx += 1
        return mx_idx, mx

    def selection_sort(self):
        sorted_list = DLL_class()
        while self.size > 0:
            mx_idx, mx = self.find_max()
            # dodamo na početak sortirane liste
            sorted_list.add_first(mx)
            self.delete_at_position(mx_idx)
        # premjestimo pokazivače iz sorted_list u self
        self.head = sorted_list.head
        self.tail = sorted_list.tail
        self.size = sorted_list.size
