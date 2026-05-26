class HashTable:
    def __init__(self, size):
        self.size = size #Veličina tablice (broj bucket-a)
        # Kreiramo listu praznih listi za svaki bucket
        # Ovo je osnova za lančano rješavanje kolizija (chaining)
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        hash_value = 5381
        
        # Za svaki znak u ključu:
        # hash = hash * 33 + ASCII vrijednost znaka
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
            # Ovo je isto kao: hash_value * 33 + ord(char)
        
        # Vraćamo indeks modulo veličina tablice
        return hash_value % self.size
    
    def put(self, key, value):
        index = self.hash_function(key)
        
        # Dohvatimo bucket (listu) na izračunatom indeksu
        bucket = self.table[index]
        
        # Provjerimo postoji li već taj ključ u bucketu
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                # Ako ključ već postoji, ažuriramo vrijednost
                bucket[i] = (key, value)
                return
        
        # Ako ključ ne postoji, dodajemo novi par na kraj bucket-a
        bucket.append((key, value))
    
    def get(self, key):
       
        # Izračunamo indeks pomoću hash funkcije
        index = self.hash_function(key)
        
        # Dohvatimo bucket na izračunatom indeksu
        bucket = self.table[index]
        
        # Pretražimo bucket za traženi ključ
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        
        # Ako nismo pronašli ključ, vraćamo None
        return None
    
    def delete(self, key):
    
        # Izračunamo indeks pomoću hash funkcije
        index = self.hash_function(key)
        
        # Dohvatimo bucket na izračunatom indeksu
        bucket = self.table[index]
        
        # Tražimo ključ u bucketu
        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                # Ako pronađemo, brišemo element na poziciji i
                del bucket[i]
                return
        
        # Ako ključ ne postoji, ne radimo ništa (ili možemo podići iznimku)
    
    def items(self):
        
        # Prolazimo kroz sve buckete
        for bucket in self.table:
            # Dodajemo sve parove iz svakog bucketa
            result.extend(bucket)
        
        return result
    
    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.table):
            if bucket:
                result += f"{i}: {bucket}\n"
        return result if result else "Empty hash table"


# Primjer korištenja
if __name__ == "__main__":
    # Kreiramo hash tablicu s 10 bucket-a
    hash_table = HashTable(size=10)
    
    # Umetanje elemenata
    hash_table.put("apple", 1)
    hash_table.put("banana", 2)
    hash_table.put("orange", 3)
    hash_table.put("apple", 5)  # Ažuriranje vrijednosti
    
    # Pretraživanje
    print(hash_table.get("banana"))  # Output: 2
    print(hash_table.get("grape"))   # Output: None
    
    # Ispis svih elemenata
    print(hash_table.items())  # Output: [('apple', 5), ('banana', 2), ('orange', 3)]
    
    # Brisanje elementa
    hash_table.delete("apple")
    print(hash_table.get("apple"))   # Output: None
    print(hash_table.items())        # Output: [('banana', 2), ('orange', 3)]
    
    # Ispis strukture tablice
    print("\nHash table struktura:")
    print(hash_table)
