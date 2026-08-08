# LAB 1

class Animal:
    def __init__(self, name, species, arrival_time):
      self.name = name
      self.species = species
      self.arrival_time = arrival_time

    def __str__(self):
      return f"{self.name} ({self.species})"


class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.time = 0

    def enqueue(self, name, species):
        animal = Animal(name, species, self.time)
        self.time += 1

        if species.lower() == "dog":
            self.dogs.append(animal)
        elif species.lower() == "cat":
            self.cats.append(animal)
        else:
            raise ValueError("Invalid species. Must be 'dog' or 'cat'.")


    def dequeue_dog(self):
      if not self.dogs:
        raise ValueError("No dogs in the shelter.")
      return self.dogs.pop(0)

    def dequeue_cat(self):
      if not self.cats:
        raise ValueError("No cats in the shelter.")
      return self.cats.pop(0)

    def dequeue_any(self):
      if not self.dogs and not self.cats:
        raise ValueError("No animals in the shelter.")
      if not self.dogs:
        return self.dequeue_cat()
      if not self.cats:
        return self.dequeue_dog()

      if self.dogs[0].arrival_time < self.cats[0].arrival_time:
        return self.dequeue_dog()
      else:
        return self.dequeue_cat()
    def __str__(self):
        dogs_str = ", ".join(str(dog) for dog in self.dogs) if self.dogs else "No dogs"
        cats_str = ", ".join(str(cat) for cat in self.cats) if self.cats else "No cats"
        return f"Dogs: {dogs_str} Cats: {cats_str}"


# (Bonus) Josephusov problem
# Koristeći CDLL i metodu rotate() iz Zadatka 1., implementirajte funkciju josephus_cdll(n, k) 
# koja simulira opisani postupak i ispisuje redoslijed eliminacije te na kraju vraća poziciju pobjednika.
def josephus_cdll(n,k):
  cdll=CDLL()
  for i in range(1,n+1):
    cdll.add_last(i)
  print("Elimination order:")

  while cdll.size>1:
    cdll.rotate(k-1)
    eliminated = cdll.head.data
    print(eliminated)
    cdll.delete_first()
  winner = cdll.head.data
  print("winner:",winner)
  return winner
josephus_cdll(7,3)




