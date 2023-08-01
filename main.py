class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"

doggo = Labrador()
print(f"A dog is {doggo.temperament}")


