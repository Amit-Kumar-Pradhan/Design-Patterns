class Dog:
    """ one of the Object to be returned"""
    def speak(self):
        return 'Woof!'
    
    def __str__(self):
        return 'Dog'

class DogFactory:
    """ Concrete factory"""
    def get_pet(self):
        """ returns a dog object"""
        return Dog()
    
    def get_food(self):
        """ returns  a dog food """
        return "Dog Food!"

class Cat:
    """ one of the Object to be returned"""
    def speak(self):
        return 'Meow!'
    
    def __str__(self):
        return 'Cat'

class CatFactory:
    """ Concrete factory"""
    def get_pet(self):
        """ returns a Cat object"""
        return Cat()
    
    def get_food(self):
        """ returns  a Cat food """
        return "Cat Food!"


class PetStore:
    def __init__(self, pet_factory=None):
        """ pet_factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method which will display al;l the details of the object"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}")
        print(f"Our pet food is = {pet_food}")
        print(f"Our pet says hello by = {pet.speak()}")

# Create a concreate factory
dog_factory = DogFactory()
cat_factory = CatFactory()

# Create a pet store housing our abstract factory
shop1 = PetStore(dog_factory)
shop = PetStore(cat_factory)
# Invoke utility method to show details
shop.show_pet()
shop1.show_pet()