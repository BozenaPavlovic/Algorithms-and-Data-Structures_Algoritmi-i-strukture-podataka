# Zadatak 1: Postotak praznih mjesta nakon umetanja
def empty_percentage(word_list, hash_fn, table_size):
    table = [None] * table_size
    
    for word in word_list:
        index = hash_fn(word) % table_size
        if table[index] is None:
            table[index] = word
    
    empty_count = sum(1 for slot in table if slot is None)
    return (empty_count / table_size) * 100


# Zadatak 2: Prosječna duljina lanca kolizija (lančano rješavanje)
def avg_collision_chain(word_list, hash_fn, table_size):
    table = [[] for _ in range(table_size)]
    
    for word in word_list:
        index = hash_fn(word) % table_size
        table[index].append(word)
    
    non_empty_chains = [chain for chain in table if chain]
    if not non_empty_chains:
        return 0.0
    
    avg_length = sum(len(chain) for chain in non_empty_chains) / len(non_empty_chains)
    return avg_length


# Zadatak 3: Maksimalni broj kolizija na jednom mjestu
def max_collisions(word_list, hash_fn, table_size):
    counts = [0] * table_size
    
    for word in word_list:
        index = hash_fn(word) % table_size
        counts[index] += 1
    
    # Maksimalni broj ključeva na jednom indeksu
    max_count = max(counts) if counts else 0
    # Broj kolizija = (broj_kljuceva - 1) na tom mjestu
    return max(max_count - 1, 0)


# Zadatak 4: Varijanca popunjenosti mjesta
def load_variance(word_list, hash_fn, table_size):
    counts = [0] * table_size
    
    for word in word_list:
        index = hash_fn(word) % table_size
        counts[index] += 1
    
    if table_size == 0:
        return 0.0
    
    mean = sum(counts) / table_size
    variance = sum((c - mean) ** 2 for c in counts) / table_size
    return variance


# Zadatak 5: Usporedba stvarnih i očekivanih kolizija
def expected_vs_actual_collisions(word_list, table_size):
    # Stvarne kolizije
    actual_collisions = 0
    table = [None] * table_size
    
    for word in word_list:
        # Ovdje koristimo jednostavnu hash funkciju za primjer
        index = hash(word) % table_size
        if table[index] is not None:
            actual_collisions += 1
        else:
            table[index] = word
    
    # Očekivane kolizije (rođendanski paradoks)
    n = len(word_list)
    m = table_size
    if m == 0:
        expected = 0
    else:
        expected = n - m * (1 - ((m - 1) / m) ** n)
    
    # Razlika u postotcima
    if expected == 0:
        return 0.0 if actual_collisions == 0 else float('inf')
    
    difference_percent = ((actual_collisions - expected) / expected) * 100
    return difference_percent


# Zadatak 6: Optimalna veličina tablice (lančano rješavanje)
def optimal_table_size(word_list, hash_fn, max_collision_percent):
    for size in range(1, len(word_list) * 2 + 1):
        # Izračunaj postotak kolizija za ovu veličinu
        table = [None] * size
        collisions = 0
        
        for word in word_list:
            index = hash_fn(word) % size
            if table[index] is not None:
                collisions += 1
            else:
                table[index] = word
        
        collision_percent = (collisions / len(word_list)) * 100 if word_list else 0
        
        if collision_percent <= max_collision_percent:
            return size
    
    return len(word_list) * 2  # Ako nema rješenja, vrati maksimum


# Zadatak 7: Usporedba dvije hash funkcije
def better_hash(word_list, hash_fn1, hash_fn2, table_size):
    def collision_percent(hash_fn):
        table = [None] * table_size
        collisions = 0
        
        for word in word_list:
            index = hash_fn(word) % table_size
            if table[index] is not None:
                collisions += 1
            else:
                table[index] = word
        
        return (collisions / len(word_list)) * 100 if word_list else 0
    
    percent1 = collision_percent(hash_fn1)
    percent2 = collision_percent(hash_fn2)
    
    if percent1 < percent2:
        return "first"
    elif percent2 < percent1:
        return "second"
    else:
        return "equal"


# Zadatak 8: Kolizije samo za riječi određene duljine
def collisions_by_length(word_list, hash_fn, table_size, length):
    filtered_words = [word for word in word_list if len(word) == length]
    
    if not filtered_words:
        return 0.0
    
    table = [None] * table_size
    collisions = 0
    
    for word in filtered_words:
        index = hash_fn(word) % table_size
        if table[index] is not None:
            collisions += 1
        else:
            table[index] = word
    
    return (collisions / len(filtered_words)) * 100


# Zadatak 9: Kolizije pri postupnom povećanju tablice
def collisions_growth(word_list, hash_fn, start_size, step, steps):
    results = []
    
    for i in range(steps):
        size = start_size + i * step
        table = [None] * size
        collisions = 0
        
        for word in word_list:
            index = hash_fn(word) % size
            if table[index] is not None:
                collisions += 1
            else:
                table[index] = word
        
        percent = (collisions / len(word_list)) * 100 if word_list else 0
        results.append(percent)
    
    return results


# Zadatak 10: Usporedba linearnog i lančanog rješavanja kolizija
def compare_collision_resolution(word_list, hash_fn, table_size):
    # Linearno istraživanje
    table_linear = [None] * table_size
    linear_collisions = 0
    
    for word in word_list:
        index = hash_fn(word) % table_size
        original_index = index
        
        while table_linear[index] is not None:
            linear_collisions += 1
            index = (index + 1) % table_size
            if index == original_index:  # Tablica je puna
                break
        
        if table_linear[index] is None:
            table_linear[index] = word
    
    linear_percent = (linear_collisions / len(word_list)) * 100 if word_list else 0
    
    # Lančano rješavanje
    table_chaining = [[] for _ in range(table_size)]
    chaining_collisions = 0
    
    for word in word_list:
        index = hash_fn(word) % table_size
        if table_chaining[index]:
            chaining_collisions += 1  # Svaki dodatni element u lancu je kolizija
        table_chaining[index].append(word)
    
    chaining_percent = (chaining_collisions / len(word_list)) * 100 if word_list else 0
    
    return (linear_percent, chaining_percent)


