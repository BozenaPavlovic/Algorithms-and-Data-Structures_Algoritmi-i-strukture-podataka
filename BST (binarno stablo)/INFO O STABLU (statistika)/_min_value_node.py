def _min_value_node(self, node): # Returns left-most node
        current = node
        while current.left is not None:
            current = current.left
        return current
