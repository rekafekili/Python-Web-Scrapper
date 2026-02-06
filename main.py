class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f"{self.breed} / {self.name} / {self.age}"


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, 5, breed)
        self.aggresive = True

    def rrrr(self):
        print("Stay Away!")


class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, 2, breed)
        self.spoiled = True

    def woof_woof(self):
        print("Woof Woof!")


ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = GuardDog(name="Bibi", breed="Dalmatian")

print(ruffus, "//", bibi)
