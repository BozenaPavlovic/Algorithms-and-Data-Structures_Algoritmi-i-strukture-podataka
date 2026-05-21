```
def nesto(node):
    if node is None:
        return pocetna_vrijednost
    
    l = nesto(node.left)
    d = nesto(node.right)
    
    # ovdje radiš nesto s l i d
    return rezultat

```

- Post-order se najčešće koristi kad trebaš nešto izračunati iz djece

- BinarySearchTree klasa ima self.root - korijen stabla

- TreeNode ima key, left, right

