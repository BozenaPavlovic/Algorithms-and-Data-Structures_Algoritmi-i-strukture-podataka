# ==============================================================================
# ZADATAK: 933. Number of Recent Calls (Broj nedavnih poziva)
#
# KATEGORIJA: STRUKTURE PODATAKA / RED (QUEUE)
# (Napomena: Koristi FIFO princip - First In, First Out)
#
# TEKST ZADATKA:
# Potrebno je napisati klasu 'RecentCounter' koja broji nedavne zahtjeve (pingove)
# unutar određenog vremenskog prozora. Klasa ima jednu metodu 'ping(int t)'.
# Svaki poziv metode 'ping' bilježi novi zahtjev u trenutku 't' (u milisekundama)
# i vraća broj zahtjeva koji su se dogodili u zadnjih 3000 milisekundi 
# (uključujući i trenutni zahtjev), odnosno u vremenskom intervalu [t - 3000, t].
#
# VAŽNA NAPOMENA:
# Svaki idući poziv metode 'ping' zajamčeno ima veći 't' od prethodnog 
# (vrijeme strogo raste: t1 < t2 < t3...).
#
# PRIMJER:
# RecentCounter counter = RecentCounter()
# counter.ping(1)    -> vraća 1  (interval [-2999, 1], unutra je [1])
# counter.ping(100)  -> vraća 2  (interval [-2900, 100], unutra su [1, 100])
# counter.ping(3001) -> vraća 3  (interval [1, 3001], unutra su [1, 100, 3001])
# counter.ping(3002) -> vraća 3  (interval [2, 3002], broj 1 ispada jer je stariji od 2)
# ==============================================================================

class RecentCounter:
    def __init__(self):
        # Inicijaliziramo prazan red (Queue) koji će čuvati vremenske oznake (t)
        # Red je savršen jer najstariji pozivi uvijek stoje na samom početku (front)
        self.requests = Queue()  

    def ping(self, t):
        # Korak 1: Svaki novi ping odmah dodajemo na kraj našeg reda
        self.requests.enqueue(t)

        # Korak 2: Čišćenje reda od "zastarjelih" zahtjeva.
        # Sve dok je element na početku reda (najstariji ping) izvan našeg prozora,
        # odnosno strogo manji od donje granice (t - 3000), izbacujemo ga van.
        while self.requests.front() < t - 3000:
            self.requests.dequeue()

        # Korak 3: Nakon što smo očistili sve stare pingove, preostala veličina reda
        # predstavlja točan broj zahtjeva unutar zadnje 3 sekunde.
        return self.requests.size()
