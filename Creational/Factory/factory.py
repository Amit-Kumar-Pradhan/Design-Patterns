class Dog:
    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Woof!"
class Cat:
    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog('Tommy'), cat=Cat('Selly'))
    return pets[pet]

d = get_pet('dog')
print(d.speak())

c = get_pet('cat')
print(c.speak())