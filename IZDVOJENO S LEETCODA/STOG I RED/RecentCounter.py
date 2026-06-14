class RecentCounter:
    def __init__(self):
        self.requests = Queue()  # Koristimo našu Queue klasu

    def ping(self, t):
        self.requests.enqueue(t)

        # Ukloni sve zahtjeve koji su stariji od t - 3000
        while self.requests.front() < t - 3000:
            self.requests.dequeue()

        return self.requests.size()