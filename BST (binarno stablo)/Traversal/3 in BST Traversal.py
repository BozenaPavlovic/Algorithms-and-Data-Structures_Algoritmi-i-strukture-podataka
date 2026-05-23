def traverse(self, node=None, result=None, traversal_type='in'):
    if result is None:
        result = []
    
    if node is None:
        node = self.root
    
    if traversal_type == 'pre':
        result.append(node.key)
    
    if node.left:
        self.traverse(node.left, result, traversal_type)
    
    if traversal_type == 'in':
        result.append(node.key)
    
    if node.right:
        self.traverse(node.right, result, traversal_type)
    
    if traversal_type == 'post':
        result.append(node.key)
    
    return result




# TEST
if __name__ == "__main__":
    bst = BST()
    # Dodajemo čvorove (primjer stabla)
    for broj in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(broj)
    
    print("In-order (uzlazno):", bst.traverse(traversal_type='in'))     # [20, 30, 40, 50, 60, 70, 80]
    print("Pre-order:", bst.traverse(traversal_type='pre'))             # [50, 30, 20, 40, 70, 60, 80]
    print("Post-order:", bst.traverse(traversal_type='post'))           # [20, 40, 30, 60, 80, 70, 50]



# Napišite rekurzivnu metodu traverse koja će zadano binarno stablo ispisati in-order, 
# pre-order, ili post-order postupkom, ovisno o ulaznom argumentu traversal_type, koji može 
# imati vrijednosti 'in', 'pre' ili 'post'. Pretpostavite da funkcija nikad neće primiti preko 
# argumenta traversal_type neku drugu vrijednost osim ove 3 navedene. Metoda treba imati 
# prototip: 
# def traverse(self, node=None, result=None, traversal_type='in'): 
