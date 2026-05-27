def max_depth(root):
    # Ako je stablo prazno, po tekstu zadatka vraćamo 0
    if root is None:
        return 0
    
    # Rekurzivno nađi dubinu lijeve i desne strane
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Vrati 1 (trenutni čvor) + veću dubinu od te dvije strane
    return 1 + max(left_depth, right_depth)

# Dubina stabla definira se kao broj čvorova na najdužem putu od korijena do nekog lista.
# Primjeri: Prazno stablo (root = None) ima dubinu 0. Stablo s jednim čvorom ima dubinu 1.
# Hint: Koristite rekurziju. Za svaki čvor izračunajte dubinu lijevog i desnog podstabla.
