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
    
    def add_last(self, new_data):
        new_node = Node(new_data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   # Posljednji čvor liste pokazuje na novi čvor
            self.tail = new_node        # Novi čvor postaje posljednji čvor liste
        self.size += 1

    def delete_first(self):
        if self.head is None:
            print("List is already empty.")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.size -= 1
        
    def delete_last(self):
        if self.head is None:
            print("List is already empty.")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.size -= 1

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        print("Item not in list!")
        return -1

    def update_at_position(self, value, position):
        if position < 0 or position >= self.size:
            print("Invalid position.")
            return
        current = self.head
        for _ in range(position):
            current = current.next 
        current.data = value      # Pronalazimo traženi čvor i ažuriramo vrijednost

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

    def insert_at_position(self, value, position):
        if position < 0 or position > self.size:
            print("Invalid position.")
            return
        if position == 0:
            self.add_first(value)
        elif position == self.size:
            self.add_last(value)
        else:
            new_node = Node(value)           # Kreiramo novi čvor
            current = self.head
            for _ in range(position - 1):
                current = current.next       # Pronalazimo prethodni čvor (u odnosu na traženi)
            new_node.next = current.next     # Naš novi čvor pokazuje na traženi čvor
            current.next = new_node          # Prethodni čvor pokazuje na novi čvor
            self.size += 1

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

   
    
