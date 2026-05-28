def selection_sort(self):
    current = self.head

    while current:
        min_node = current
        temp = current.next

        while temp:
            if temp.data < min_node.data:
                min_node = temp
            temp = temp.next

        current.data, min_node.data = min_node.data, current.data
        current = current.next
