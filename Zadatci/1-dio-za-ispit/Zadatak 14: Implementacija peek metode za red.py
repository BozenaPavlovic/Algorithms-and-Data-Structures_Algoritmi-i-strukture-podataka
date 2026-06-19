# ==============================================================================
# ZADATAK 14: Prvi član na izlazu iz reda (peek metoda)
#
# TEKST ZADATKA:
# Napišite funkciju koja vraća prvi član na izlazu iz reda iz klase Red, 
# ali tako da nakon izlaska iz funkcije taj član ostane na redu (tzv. peek metoda). 
# Smiju se koristiti samo osnovne funkcije za rad s redovima: dodaj i skini.
# ==============================================================================

def peek_queue(queue):
    if len(queue) == 0:
        return None

    front = queue.dequeue()
    queue.enqueue(front)

    for _ in range(len(queue) - 1):
        queue.enqueue(queue.dequeue())

    return front
