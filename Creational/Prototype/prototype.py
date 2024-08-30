import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """ Register an Object """
        self._objects[name] = obj

    
    def unregister_object(self, name):
        """ Unregister an Object """
        del self._objects[name]

    def clone(self, name, **attr):
        """ Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "Mustang"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return f"{self.name} | {self.color} | {self.options}"

c = Car()

prototype = Prototype()

prototype.register_object('Mustang', c)

c1 = prototype.clone('Mustang')

print(c1)