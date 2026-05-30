class TreeNode: 
  def __init__(self, key): 
    self.key = key 
    self.left = None 
    self.right = None

def update_tree(node): 
    # 1. BAZNI SLUČAJ (Gdje rekurzija prestaje)
    # Ako si došla do kraja grane (dijete ne postoji), vrati 0 natrag roditelju.
    if node is None: 
        return 0 
    
    # 2. PAMĆENJE ORIGINALNE VRIJEDNOSTI
    # Moramo odmah spremiti trenutni key (npr. 3), jer ćemo ga kasnije 
    # prepisati s 0 ili 1, a trebat će nam njegova originalna vrijednost za roditelja.
    original_key = node.key 
    
    # 3. REKURZIVNI KORAK (Idemo u dubinu)
    # Funkcija samu sebe poziva za lijevo i desno dijete.
    # Ona čeka da se ti pozivi izvrše i vrate joj rezultate (sume).
    sum_left = update_tree(node.left) 
    sum_right = update_tree(node.right) 
    
    # 4. RAČUNANJE SUME POTOMAKA
    # Kad su se djeca vratila s odgovorima, zbrojimo ih.
    total_sum = sum_left + sum_right 
    
    # 5. TRENUTAK PROMJENE (Ovdje se upisuje 0 ili 1)
    # Profesor je iskoristio "ternarni operator" (skraćeni if-else u jednom retku).
    # Znači: node.key postaje 0 AKO je total_sum paran, INAČE postaje 1.
    node.key = 0 if total_sum % 2 == 0 else 1 
    
    # 6. SLANJE ODGOVORA GORE (Return)
    # Na samom kraju, ovaj čvor vraća roditelju iznad sebe ukupnu sumu:
    # zbroj svih svojih potomaka + svoju vlastitu originalnu vrijednost.
    return total_sum + original_key
