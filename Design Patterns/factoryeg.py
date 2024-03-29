class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof!"


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow!"


def get_pet(pet="dog"):
    # factory method
    pets = dict(dog=Dog("Lalya"), cat=Cat("Margo"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())

