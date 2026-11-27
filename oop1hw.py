class Pet:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal
        self.hunger = 5  # 5 means hungry, 0 means full

    def feed(self):
        self.hunger -= 1
        print(f"Yum! {self.name} the {self.animal} ate a snack! Hunger level: {self.hunger}")

# Example usage
my_pet = Pet("Buddy", "dog")
my_pet.feed()
my_pet.feed()
