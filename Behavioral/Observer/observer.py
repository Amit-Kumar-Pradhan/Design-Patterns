class Subject(object): # Represents: what is being observed
    def __init__(self):
        self._observers = [] # This is where all the references to all the observer
                             # Note that this is one to many relation

    def attach(self, observer):
        # If observer is not already in the observer list \
        # Append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # For all the observer in the observers list
        # Don't notify the observer who is actually updating the temp
        #  Alert the observer
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name # Set the name of the core
        self._temp = 0 # Initialize the temperature of the core

    @property #Getter that gets core temperature
    def temp(self):
        return self._temp

    @temp.setter # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify observer whenver somebody change the core temperature
        self.notify()

class TempViewer:
    """ This is the observer class """
    def update(self, subject): # Alert method which get invoked when the temp changes
        print(f"Temperature viewer: {subject._name} has Temperature = {subject._temp}")

# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temp of our first core
c1.temp = 80
c1.temp =90
