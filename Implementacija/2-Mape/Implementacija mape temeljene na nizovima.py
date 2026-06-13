class CustomDict:
    def __init__(self):
        self.keys = []      # Niz za ključeve (npr. ['a', 'b'])
        self.values = []    # Paralelni niz za vrijednosti (npr. [1, 2])

    def set(self, key, value):
        if key in self.keys:    # 1. PROVJERA: Postoji li već taj ključ?
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyError(f'Key {key} not found.') # f-string

    def delete(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            del self.keys[index]
            del self.values[index]
        else:
            raise KeyError(f'Key {key} not found.') # f-string

    def contains(self, key):
        return key in self.keys

    def __len__(self):
        return len(self.keys)

    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in zip(self.keys, self.values)) + "}"

# Example usage
custom_dict = CustomDict()
custom_dict.set("a", 1)
custom_dict.set("b", 2)
print(custom_dict.get("a"))  # Output: 1
print(custom_dict)           # Output: {a: 1, b: 2}

custom_dict.set("a", 3)
print(custom_dict.get("a"))  # Output: 3
print(custom_dict)           # Output: {a: 3, b: 2}

print(custom_dict.contains("b"))  # Output: True
print(custom_dict.contains("c"))  # Output: False

custom_dict.delete("a")
print(custom_dict)  # Output: {b: 2}

try:
    custom_dict.get("a")
except KeyError as e:
    print(e)  # Output: Key a not found.
