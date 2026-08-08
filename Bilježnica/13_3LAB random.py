    def in_order_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node is None:
            return result

        if node.left is not None:
            self.in_order_traversal(node.left, result)

        result.append((node.key, node.value))

        if node.right is not None:
            self.in_order_traversal(node.right, result)

        return result

    def max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def max_value_leaf(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None or current.right is not None:
            if current.right is not None:
                current = current.right
            else:
                current = current.left
        return current.key





#%%
def word_frequency_BST(text):
    word_freq = BSTDict()
    words = text.split()

    for word in words:
        # Čistimo riječ od interpunkcije i pretvaramo u mala slova
        cleaned_word = word.strip('.,?!_-"()').lower()

        if cleaned_word:  # Preskačemo ako je ostao prazan string
            # Tražimo postoji li već ta riječ u BST-u pomoću tvoje metode 'search'
            current_count = word_freq.search(cleaned_word)

            if current_count is not None:
                # Ako postoji, ažuriramo je sa starom vrijednošću + 1 pomoću 'insert'
                word_freq.insert(cleaned_word, current_count + 1)
            else:
                # Ako ne postoji, ubacujemo je prvi put s vrijednošću 1
                word_freq.insert(cleaned_word, 1)

    return word_freq


def word_frequency_HT(text):
    word_freq = HashTable(size=1000)
    words = text.split()

    for word in words:
        # Isti postupak čišćenja riječi kao i za BST radi poštene usporedbe
        cleaned_word = word.strip('.,?!_-"()').lower()

        if cleaned_word:
            # Tražimo riječ u našoj Hash tablici pomoću njezine metode 'get'
            current_count = word_freq.get(cleaned_word)

            if current_count is not None:
                # Ako ključ već postoji, povećavamo brojač pomoću 'put'
                word_freq.put(cleaned_word, current_count + 1)
            else:
                # Ako je riječ nova, upisujemo 1
                word_freq.put(cleaned_word, 1)

    return word_freq
