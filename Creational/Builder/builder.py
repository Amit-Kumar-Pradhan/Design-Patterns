class Director:
    """ Director """
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder:
    """ Abstract builder """
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    """ Concrete Builder --> Provides parts and tools to work """
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular Tires"
    
    def add_engine(self):
        self.car.engine = "Turbo Engine"

class Car:
    """ Product """
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f"{self.model} | {self.tires} | {self.engine} "


# COncrete builder
builder = SkyLarkBuilder()

# Create Director object
director = Director(builder)

# Create the car
director.construct_car()

# Get the car object
car = director.get_car()

print(car)
