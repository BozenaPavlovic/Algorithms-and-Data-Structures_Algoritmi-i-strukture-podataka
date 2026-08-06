#%%
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

    def add_last(self, new_data):
        new_node = Node(new_data)
        if self.tail is None:
            # prazna lista
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node.prev = None
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            print("List is already empty.")
            return
        if self.head == self.tail:
            # samo jedan element
            self.head = None
            self.tail = None
            self.size -= 1
            return
        # više elemenata
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def delete_last(self):
        if self.tail is None:
            print("List is already empty.")
            return
        if self.head == self.tail:
            # samo jedan element
            self.head = None
            self.tail = None
            self.size -= 1
            return
        # više elemenata
        self.tail = self.tail.prev
        self.tail.next = None
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
        node = self._node_at(position)
        node.data = value

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

    def insert_at_position(self, value, position):
        if position < 0 or position > self.size:
            print("Invalid position.")
            return
        if position == 0:
            self.add_first(value)
            return
        if position == self.size:
            self.add_last(value)
            return
        next_node = self._node_at(position)
        prev_node = next_node.prev
        new_node = Node(value)
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
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

    def print_list(self):
        temp = self.head
        print('[', end='')
        while temp:
            if temp.next:
                print(temp.data, end=', ')
            else:
                print(temp.data, end='')
            temp = temp.next
        print(']')
        print()

    def __str__(self):
        temp = self.head
        out = '['
        while temp:
            if temp.next:
                out = out + str(temp.data) + ', '
            else:
                out = out + str(temp.data) + ']'
            temp = temp.next
        return out

    def _node_at(self, position):
        # validacija pozicije preduvjet je van ili ovdje
        if position < 0 or position >= self.size:
            raise IndexError("position out of range")
        # efikasna traversala: od head naprijed ili od tail unazad
        if position <= self.size // 2:
            node = self.head
            for _ in range(position):
                node = node.next
            return node
        else:
            node = self.tail
            for _ in range(self.size - 1 - position):
                node = node.prev
            return node
