def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i





# SINGLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # SAMO next, NEMA prev!

def selection_sort(head):
    if head is None or head.next is None:
        return head

    tail = None          # Zadnji čvor sortiranog dijela
    current = head       # Prvi čvor nesortiranog dijela

    while current is not None:
        # Traži minimum i ZAPAMTI njegovog prethodnika
        small = current
        prev_small = None    # Pomoćna varijabla, NIJE dio čvora
        prev = current       # Pomoćna varijabla
        temp = current.next

        while temp is not None:
            if temp.data < small.data:
                small = temp
                prev_small = prev   # Pamti prethodnika za min
            prev = temp
            temp = temp.next

        # Izbaci minimum iz nesortiranog dijela
        if small == current:
            current = current.next
        else:
            prev_small.next = small.next   # preskoči min

        # Dodaj minimum na kraj sortiranog dijela
        if tail is None:
            head = small
        else:
            tail.next = small

        tail = small

    return head





# DOUBLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def selection_sort(head):
    if head is None or head.next is None:
        return head

    tail = None
    current = head

    while current is not None:
        small = current
        prev_small = None
        prev = current
        temp = current.next

        # Traži minimum (isti kod kao za jednostruku)
        while temp is not None:
            if temp.data < small.data:
                small = temp
                prev_small = prev
            prev = temp
            temp = temp.next

        # Izbaci minimum (isti kod)
        if small == current:
            current = current.next
        else:
            prev_small.next = small.next
            if small.next is not None:
                small.next.prev = prev_small   # 🟢 DODATAK za dvostruku

        # Dodaj minimum na kraj
        if tail is None:
            head = small
            small.prev = None                  # 🟢 DODATAK za dvostruku
        else:
            tail.next = small
            small.prev = tail                  # 🟢 DODATAK za dvostruku

        tail = small

    return head






















