def in_order_traversal(self, node=None, result=None):
    # Definiramo metodu koja prima: 
    # - self: referenca na instancu klase
    # - node: trenutni čvor (zadano None, znači kreni od korijena)
    # - result: lista za prikupljanje rezultata (zadano None, inicijalizira se unutar metode)
  
  if result is None:
    # Ako result nije proslijeđen (prvi poziv metode)
    # kreiramo novu praznu listu za prikupljanje parova (ključ, vrijednost)
    result=[]
    
  if node is None:
    # Ako node nije proslijeđen (prvi poziv metode)
    # postavljamo node na korijen stabla (self.root)
    node=self.root
    
  if node is not None:
     # Provjeravamo postoji li trenutni čvor (nije None)
     # Ovo je uvjet za rekurziju - ako je čvor None, prekidamo grananje
    
    if node.left:
      # Ako trenutni čvor ima lijevo dijete (node.left nije None)
      # Rekurzivno pozivamo metodu na lijevom djetetu
      # Lijevo podstablo sadrži sve MANJE ključeve od trenutnog
      self.in_order_traversal(node.left,result)
      # Nakon što obradimo cijelo lijevo podstablo (sve manje ključeve)
      # Dodajemo T R E N U T N I čvor u rezultat
      # Dodajemo ga kao TUPLE (par): (ključ, vrijednost)
      # Ovo je "posjet" čvoru u in-order obilasku
    result.append((node.key,node.value))

    if node.right:
      # Ako trenutni čvor ima desno dijete (node.right nije None)
      # Rekurzivno pozivamo metodu na desnom djetetu
      # Desno podstablo sadrži sve VEĆE ključeve od trenutnog
      self.in_order_traversal(node.right,result)


    # Vraćamo listu rezultata koja sadrži sve (ključ, vrijednost) parove
    # Lista je sortirana prema ključevima (jer je in-order obilazak)
  return result




#------------------------- TO JEST KRAĆE ZA NOTES  BEZ KOMENTARA

def in_order_traversal(self, node=None, result=None):
    # Inicijalizacija liste rezultata (samo pri prvom pozivu)
    if result is None:
        result = []
    
    # Ako node nije zadan, kreni od korijena
    if node is None:
        node = self.root
    
    # Ako trenutni čvor postoji (nije None)
    if node is not None:
        # 1. REKURZIJA: obiđi LIJEVO podstablo (svi manji ključevi)
        if node.left:
            self.in_order_traversal(node.left, result)
        
        # 2. POSJET: dodaj TRENUTNI čvor (ključ, vrijednost) u rezultat
        result.append((node.key, node.value))
        
        # 3. REKURZIJA: obiđi DESNO podstablo (svi veći ključevi)
        if node.right:
            self.in_order_traversal(node.right, result)
    
    # Vrati popunjeni rezultat
    return result
