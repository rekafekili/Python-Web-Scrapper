class Puppy:
    def __init__(self, name, breed):
        # print("Puppy is born")
        self.name = name
        self.age = 6
        self.breed = breed

    def __str__(self):
        return f"{self.breed} puppy named {self.name}."


ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = Puppy(name="Bibi", breed="Dalmatian")

print(bibi, ruffus)
