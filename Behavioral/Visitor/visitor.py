class House(object): # the class being visited
    def accept(self, visitor):
        """ Interface to accept a visitor """
        visitor.visit(self) #  Triggers the visiting operation!

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        # note that we now have a reference to the electrician object 
        print(self, "worked on by", electrician)

    def __str__(self):
        """ Simply return classname when the house object is printed"""
        return self.__class__.__name__

class Visitor(object):
    """ Abstract visitor """
    def __str__(self):
        """ simply returns the classname when the vistor object is printed """
        return self.__class__.__name__

class HvacSpecialist(Visitor): # Inherit from the parent class, Visitor
    """ Concrete Visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self) # Note that the visitor now has a reference

class Electrician(Visitor): # Inherit from the parent class, Visitor
    """ Concrete Visitor: Electrician"""
    def visit(self, house):
        house.work_on_electricity(self) # Note that the visitor now has a reference

# Create HVAC specialist
hv = HvacSpecialist()

# Create an electrician
e = Electrician()

# Create a house
home = House()

# let the house accept the HVAC specialist and work on the house by invoking
home.accept(hv)

# let the house accept the electrician and work on the house by invoking
home.accept(e)