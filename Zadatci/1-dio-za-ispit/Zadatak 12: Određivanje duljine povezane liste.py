# ==============================================================================
# ZADATAK 12: Duljina povezane liste bez atributa veličine
#
# TEKST ZADATKA:
# Napišite metodu koja određuje i vraća duljinu jednostruko povezane liste, 
# pod pretpostavkom da ne postoji atribut u kojem je spremljen taj podatak.
# ==============================================================================

def length(self):
    count = 0
    curr = self.head

    while curr is not None:
        count += 1
        curr = curr.next_node

    return count
