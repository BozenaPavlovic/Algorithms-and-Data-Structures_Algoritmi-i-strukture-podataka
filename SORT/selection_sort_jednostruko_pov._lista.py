# ovo je jednostviji bez diranja memorije
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def selection_sort(head):
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


# teža verzija koja dira memoriju i pokazivače

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










