class CustomDict:
    def __init__(self):
        self.keys = []      # niz za ključeve (npr. ['a', 'b'])
        self.values = []    # paralelni niz za vrijednosti (npr. [1, 2])

    def set(self, key, value):
        if key in self.keys:              # 1. PROVJERA: Postoji li već taj ključ?
            index = self.keys.index(key)  # 2. MOST: Saznaj na kojem je indeksu
            self.values[index] = value    # 3. IZMJENA: Na tom istom indeksu pregazi vrijednost
        else:
            self.keys.append(key)         # 4. DODAVANJE: Ako ne postoji, stavi ključ na kraj
            self.values.append(value)     # 5. SINKRONIZACIJA: Stavi vrijednost na isti taj kraj

    def get(self, key):                   
        if key in self.keys:              # 1. PROVJERA: Je li ključ uopće unutra?
            index = self.keys.index(key)  # 2. MOST: Saznaj njegov (indeks)
            return self.values[index]     # 3. DOHVAT: Vrati vrijednost s tog istog indeksa
        else:
            raise KeyError(f'Key {key} not found.') # 4. IZUZETAK: baci grešku

    def delete(self, key):
        if key in self.keys:              # 1. PROVJERA: Ima li tog ključa za brisanje?
            index = self.keys.index(key)  # 2. MOST: Saznaj točan indeks elementa
            del self.keys[index]          # 3. BRISANJE: Makni ključ s tog indeksa
            del self.values[index]        # 4. OBAVEZNO: Makni i vrijednost da se nizovi ne pomaknu!
        else:
            raise KeyError(f'Key {key} not found.') # 5. IZUZETAK: baci grešku

    def contains(self, key):
        return key in self.keys # Vraća True ako postoji, inače False

    def __len__(self):
        return len(self.keys) # Duljina liste ključeva je duljina mape

    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in zip(self.keys, self.values)) + "}"
        # Spaja ključeve i vrijednosti u parove "ključ: vrijednost" i stavlja ih u {}

