class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
    # Broj 5381 je početni prosti broj iz poznatog 'djb2' algoritma za hashiranje stringova
    # Koristi se zato što prosti brojevi matematički drastično smanjuju šanse za kolizije 
    # (da dva različita stringa dobiju isti indeks) i osiguravaju da se ključevi 
    # ravnomjerno rasporede po cijeloj tablici
        hash_value = 5381
        
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def put(self, key, value):
        index = self.hash_function(key)
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
