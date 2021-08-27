class Dog:
    # one of the objects to be returned
    def speak(self):
        return "woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    # concrete factory
    def get_pet(self):
        # return a dog object
        return Dog()

    def get_food(self):
        # return a dog food object
        return "Dog Food"


class PetStore:
    # petstore is a abstract factory
    def __init__(self, pet_factory = None):
        # pet factory is abs fact
        self._pet_factory = pet_factory

    def show_pet(self):
        # utility method to display the details of th objects returned by Dog Factory
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("our pet is '{}'".format(pet))
        print("our pet speaks '{}'".format(pet.speak()))
        print("its food is {}".format(pet_food))


# concrete factory
factory = DogFactory()
shop = PetStore(factory)

shop.show_pet()



