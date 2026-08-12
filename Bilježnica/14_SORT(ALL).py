CONTAINS:
BUBBLE - ARR - SINGLE - DOUBLE
MERGE - ARR - SINGLE - DOUBLE
SELECTION - ARR - SINGLE - DOUBLE 

#BUBBLE SORT
# Normalno (niz / array)

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1] # zamjena elemenata
                swapped = True
        if not swapped:
            break
    return arr
  
# BUBBLE SINGLE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def bubble_sort_data_swap(self):
        """Sortira listu silazno koristeći zamjenu podataka (data swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                # Silazni poredak: ako je trenutni manji od idućeg, mijenjaj podatke
                if current.data < next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next

#BUBBLE DOUBLE
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def bubble_sort_data_swap(self):
        """Sortira dvostruko povezanu listu silazno koristeći zamjenu podataka (data swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                # Silazni poredak: ako je trenutni manji od idućeg, mijenjaj podatke
                if current.data < next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next


#MERGE SORT 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result += [left[0]]
            left = left[1:]
        else:
            result += [right[0]]
            right = right[1:]

    result += left
    result += right

    return result
  
# MERGE JEDNO
  class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def split_list_single_pointers(head):
    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None  # Fizički rez veze između polovica
    return mid

def merge_single_pointers(left, right):
    if left is None: return right
    if right is None: return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_single_pointers(left.next, right)
    else:
        result = right
        result.next = merge_single_pointers(left, right.next)
    return result

def merge_sort_single_pointers(head):
    # Bazni slučaj
    if head is None or head.next is None:
        return head
        
    # 1. Split cjelina
    mid = split_list_single_pointers(head)
    
    # 2. Rekurzivni pozivi
    left_sorted = merge_sort_single_pointers(head)


# MERGE DOUBLE
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def split_list_double_pointers(head):
    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None  # Prekid prednje veze
    if mid is not None:
        mid.prev = None  # 🟢 DODATAK ZA DVOSTRUKU: Prekid stražnje veze
    return mid

def merge_double_pointers(left, right):
    """Spaja dvije sortirane dvostruke liste i obnavlja .prev veze."""
    if left is None: return right
    if right is None: return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_double_pointers(left.next, right)
        if result.next is not None:
            result.next.prev = result  # 🟢 DODATAK ZA DVOSTRUKU (veza unazad)
        result.prev = None
    else:
        result = right
        result.next = merge_double_pointers(left, right.next)
        if result.next is not None:
            result.next.prev = result  # 🟢 DODATAK ZA DVOSTRUKU (veza unazad)
        result.prev = None
    return result

def merge_sort_double_pointers(head):
    if head is None or head.next is None:
        return head
        
    mid = split_list_double_pointers(head)
    
    left_sorted = merge_sort_double_pointers(head)
    right_sorted = merge_sort_double_pointers(mid)
    
    return merge_double_pointers(left_sorted, right_sorted)


# SELECTION SORT (NIZ / ARRAY – standardna verzija)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

  
    right_sorted = merge_sort_single_pointers(mid)
    
    # 3. Merge cjelina
    return merge_single_pointers(left_sorted, right_sorted)


# SELECTION SINGLE
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
