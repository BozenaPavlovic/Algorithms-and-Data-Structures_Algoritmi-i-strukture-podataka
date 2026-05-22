class TreeNodeDict:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTDict:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = TreeNodeDict(key, value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left=new_node
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right=new_node
                    break
                current = current.right
            else:
                current.value = value
                break


    def search(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                return value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


    def delete(self, key):
      parent = None
      current = self.root
      
      #pronalazak Node i parenta
      while current is not None and current.key != key:
        parent = current
        if key < current.key:
          current = current.left
        else:
          current = current.right
      if current is None:
        return print("no key")


  
      # Case 1: Node has no children (leaf node)
      if current.left is None and current.right is None:
        if current != self.root:
          if parent.left == current:
            parent.left = None
          else:
            parent.right = None
        else:
          self.root = None
        
      # Case 2: Node has two children
      elif current.left and current.right:
        successor_parent  = current
        successor = current.right
        while successor.left is not None:
          successor_parent = successor
          successor = successor.left
        current

  
      # Case 3: Node has one child


    def in_order_traversal(self, node=None, result=None):

        # Nadopuniti

        return result











# razlike između BSTDict i BinarySearchTree:

# TreeNodeDict umjesto TreeNode - dodan je atribut value za pohranu vrijednosti uz ključ
# Metoda insert(self, key, value) - umjesto samo ključa, prima i vrijednost, te ažurira vrijednost ako ključ već postoji
# Metoda search(self, key) - umjesto da vraća čvor, vraća value pridruženom ključu (ili None)
# Metoda delete(self, key) - prilagođena da radi s čvorovima koji imaju i key i value, te u slučaju brisanja čvora s dva djeteta kopira i ključ i vrijednost iz successora
# Metoda in_order_traversal - nova rekurzivna metoda koja vraća listu tuple-ova (key, value) u rastućem redoslijedu ključeva
