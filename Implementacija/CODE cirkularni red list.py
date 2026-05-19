class Queue:
    def __init__(self, max_size):
        self.items = [None] * max_size  # Kreira fiksni niz pun None vrijednosti (npr. [None, None, None])
        self.max_size = max_size        # Maksimalni kapacitet reda (koliko elemenata stane)
        self.front = -1                 # Indeks prvog elementa, kreće od -1 jer je red prazan
        self.size = 0                   # Trenutni broj elemenata u redu

    def is_full(self):
        return self.size == self.max_size  # Vraća True ako je red pun, inače False

    def is_empty(self):
        return self.size == 0              # Vraća True ako je red prazan, inače False

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("The queue is full")  # 1. PROVJERA: Ako je pun, baci grešku
        else:
            if self.front == -1:  # in case the queue was empty
                self.front = 0    # 2. POSTAVLJANJE: Ako je bio prazan, postavi početak na indeks 0
            self.items[(self.front + self.size) % self.max_size] = item  # 3. DODAVANJE: Izračunaj kružni indeks kraja i stavi element
            self.size += 1        # 4. SINKRONIZACIJA: Povećaj brojač elemenata za 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")  # 1. PROVJERA: Ako je prazan, baci grešku
        else:
            first_element = self.items[self.front]  # 2. POHRANA: Uzmi element koji je na redu za izlaz
            self.items[self.front] = None           # 3. BRISANJE: Isprazni to mjesto (postavi na None)
            self.front = (self.front + 1) % self.max_size  # update front # 4. POMAK: Pomakni 'front' na idući kružni indeks
            self.size -= 1                          # 5. SINKRONIZACIJA: Smanji broj elemenata za 1
            if self.size == 0:  # if queue becomes empty
                self.front = -1                     # 6. RESET: Ako je red sada prazan, vrati front na -1
            return first_element                    # 7. REZULTAT: Vrati izbrisani element

    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty")  # 1. PROVJERA: Ako je prazno, nema se što vidjeti
        else:
            return self.items[self.front]           # 2. POGLED: Vrati element s početka bez brisanja

    def delete(self):
        self.items = [None] * self.max_size  # 1. ČIŠĆENJE: Ponovno napuni niz s None vrijednostima
        self.front = -1                      # 2. RESET: Vrati pokazivač početka na -1
        self.size = 0                        # 3. RESET: Postavi broj elemenata na 0

    def __str__(self):
        values = [str(x) for x in self.items]  # Pretvara sve elemente iz niza u tekst
        return ' '.join(values) # space used as separator for join # Spaja ih u jedan tekst odvojen razmacima
