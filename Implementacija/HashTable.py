class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        hash_value = 5381
        
    # Broj 5381 je početni prosti broj iz poznatog 'djb2' algoritma za hashiranje stringova
    # Koristi se zato što prosti brojevi matematički drastično smanjuju šanse za kolizije 
    # (da dva različita stringa dobiju isti indeks) i osiguravaju da se ključevi 
    # ravnomjerno rasporede po cijeloj tablici
        

    # Operacija '<< 5' pomiče bitove broja za 5 mjesta ulijevo, što je u računalnoj matematici 
    # isto što i množenje broja s 32. Dodavanjem 'hash_value' na to zapravo množimo broj s 33
    # To se radi jer je računalima puno brže raditi s bitovima nego klasično množiti, 
    # a broj 33 u kombinaciji s 5381 daje savršeno izmiješane (raspršene) indekse
        
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        # 'bucket' je zapravo podlista na određenom indeksu u kojoj rješavamo kolizije (ulančavanje)
        # Funkciju 'enumerate' koristimo kako bismo istovremeno dobili i indeks (i) i sam par (ključ, vrijednost)
        # Ako u petlji pronađemo da ključ već postoji, odmah ga ažuriramo na tom indeksu 'i' i prekidamo funkciju 
        # s 'return' kako ne bismo bezveze vrtjeli petlju do kraja ili dodali dupli ključ
        
        bucket = self.table[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]
        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return

    def items(self):
        result = []
        for bucket in self.table:
            
            # Umjesto običnog '.append()' koji bi nam u rezultat ubacio cijele podliste (pa bismo dobili listu listi),
        # ovdje koristimo '.extend()'. Ta metoda uzima elemente iz svakog pojedinačnog 'bucketa' (pretinca)
        # i "raspakirava" ih izravno u našu glavnu 'result' listu, stvarajući jedan ravan, čisti popis svih parova
            
            result.extend(bucket)
        return result

    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.table):
            if bucket:
                result += f"{i}: {bucket}\n"
        return result if result else "Empty hash table"

# Primjer korištenja
hash_table = HashTable(size=10)
hash_table.put("apple", 1)
hash_table.put("banana", 2)
hash_table.put("orange", 3)
print(hash_table.get("banana"))  # Output: 2
hash_table.delete("apple")
print(hash_table.items())  # Output: [('banana', 2), ('orange', 3)]
