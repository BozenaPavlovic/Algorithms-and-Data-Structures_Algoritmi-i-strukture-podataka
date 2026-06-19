# ==============================================================================
# ZADATAK 15: Proširivanje liste sumom susjednih čvorova
#
# TEKST ZADATKA:
# Napišite metodu prosiri koja će jednostruko povezanu linearnu listu proširiti 
# novim elementima na način da između svaka dva čvora liste doda novi čvor 
# čija će vrijednost biti jednaka sumi vrijednosti čvorova između kojih se dodaje.
#
# PRIMJER:
# Originalna lista: 2 8 12 9 7
# Proširena lista:  2 10 8 20 12 21 9 16 7
# ==============================================================================


def expand(self):
    if self.head is None or self.head.next_node is None:
        return

    curr = self.head

    while curr.next_node is not None:
        left_value = curr.data
        right_value = curr.next_node.data
        total = left_value + right_value

        new_node = Node(total, curr.next_node)

        curr.next_node = new_node

        curr = new_node.next_node
