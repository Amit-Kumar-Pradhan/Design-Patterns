import types # Import the types module

class Strategy:
    """ The strategy pattern class """
    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If reference to a function is provided, replace the execute function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self): # This gets replaced by another version if function name is provided
        """ the default method that prints the name of the strategy method being provided """
        print(f"{self.name} is used !")

# Replacement method 1
def strategy_one(self):
    print(f"{self.name} is used to execute method 1")

# Replacement method 2
def strategy_two(self):
    print(f"{self.name} is used to execute method 2")

# let's create our default strategy
s0 = Strategy()

# Let's create sour default strategy
s0.execute()

# Let's create our first variation of our default strategy by providing a function as an arg
s1 = Strategy(strategy_one)

# Let's set it's name
s1.name = "Strategy One"

# Let's execute the strategy
s1.execute()

# Let's create our first variation of our default strategy by providing a function as an arg
s2 = Strategy(strategy_two)

# Let's set it's name
s2.name = "Strategy Two"

# Let's execute the strategy
s2.execute()