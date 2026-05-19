class Queue:
    def __init__(self, max_size):
        self.items = [None] * max_size  # Kreira fiksni niz pun None vrijednosti (npr. [None, None, None])
        self.max_size = max_size        # Maksimalni kapacitet reda (koliko elemenata stane)
        self.front = -1                 # Indeks prvog elementa (početak reda), kreće od -1 jer je red prazan
        self.size = 0                   # Trenutni broj elemenata u redu (trenutna popunjenost)

    def is_full(self):
        return self.size == self.max_size  # Vraća True ako je trenutna veličina dosegla maksimum, inače False

    def is_empty(self):
        return self.size == 0              # Vraća True ako u redu nema niti jednog elementa, inače False

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("The queue is full")  # 1. PROVJERA: Ako je red pun, baci grešku jer nema mjesta
        else:
            if self.front == -1:  # 2. BAZNI SLUČAJ: Ako je red bio potpuno prazan...
                self.front = 0    # ...postavi pokazivač 'front' na nulu jer tu stiže prvi element

            # 3. CIRKULARNI INDEKS: Računa točnu poziciju za novi element (kraj reda) pomoću ostatka dijeljenja (%)
            # Formula (self.front + self.size) % self.max_size omogućuje da se red "zamota" natrag na početak ako ima mjesta
            back_index = (self.front + self.size) % self.max_size
            
            self.items[back_index] = item  # 4. DODAVANJE: Stavi element na izračunatu poziciju
            self.size += 1                 # 5. SINKRONIZACIJA: Povećaj brojač elemenata za 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")  # 1. PROVJERA: Ako je red prazan, nema se što maknuti, baci grešku
        else:
            first_element = self.items[self.front]  # 2. POHRANA: Uzmi element koji je trenutno na redu za izlaz
            self.items[self.front] = None           # 3. BRISANJE: Oslobodi to mjesto (postavi na None)
            
            # 4. POMAK: Pomakni 'front' na idući element. % osigurava da skočimo na indeks 0 ako pređemo kraj niza
            self.front = (self.front + 1) % self.max_size  
            
            self.size -= 1  # 5. SINKRONIZACIJA: Smanji trenutni broj elemenata za 1
            
            if self.size == 0:    # 6. RESET: Ako je red nakon ovoga ostao potpuno prazan...
                self.front = -1   # ...vrati 'front' na početnih -1 radi urednosti
                
            return first_element  # 7. REZULTAT: Vrati izbrisani element korisniku

    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is empty")  # 1. PROVJERA: Ako je prazno, nema se što vidjeti
        else:
            return self.items[self.front]           # 2. POGLED: Vrati element s početka reda bez da ga brišeš

    def delete(self):
        self.items = [None] * self.max_size  # 1. ČIŠĆENJE: Pregazi cijeli niz novim, praznim None vrijednostima
        self.front = -1                      # 2. RESET: Vrati pokazivač početka na početno stanje
        self.size = 0                        # 3. RESET: Postavi trenutni broj elemenata natrag na 0

    def __str__(self):
        values = [str(x) for x in self.items]  # Pretvara svaki element iz niza (uključujući i None) u tekst
        return ' '.join(values)                # Spaja sve elemente u jedan tekstualni niz odvojen razmacima
