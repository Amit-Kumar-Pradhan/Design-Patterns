class Korean:
    """ Korean Speaker """
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """ English Speaker """
    def __init__(self):
        self.name = "British"
    
    """ Note the method name is different here """
    def speak_english(self):
        return "Hello!"

class Adapter:
    """ This changes the generic method name to indivdualized method name """
    def __init__(self, object, **adapted_method):
        """ Change the name of the method """
        self._object = object

        # Add  a new dictionary item that establishes the mapping between the generic method names
        # Foe ex: speak() will be translated to speak_korean() or speak_english()
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """ Simply return the rest of attributes! """
        return getattr(self._object, attr)

# List to store speaker object
objects = []

#  Create an Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f"{obj.name} says {obj.speak()}")