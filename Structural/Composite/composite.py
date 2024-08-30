class Component(object):
    """ Abstract class"""
    def __init__(self, *args, **kwargs):
        pass

    def component_function(Self):
        pass
    
class Child(Component): # Inherits from the abstract class, Component
    """ Concrete class """
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        # This is where will store the name of your child item!
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here!
        print(f"{self.name}")

class Composite(Component): # Inherits from abstract class component 
    """ Concrete class and contains tree recursive structure """
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where store the name of the composite object
        self.name = args[0]

        # This is where will keep our child item
        self.children = []

    def append_child(self, child):
        """ Method to add new child item"""
        self.children.append(child)


    def remove_child(self, child):
        """ Method to remove a child item """
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print(f"{self.name}")

        # Iterate through the child objects and invoke their component 
        for i in self.children:
            i.component_function()

# Build a composite submenu 1
sub1 = Composite("submenu1")

# Create a new child sub menu 11
sub11 = Child("sub_submenu_11")
# Create a new child sub menu 12
sub12 = Child("sub_submenu_12")


# Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)

# Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite("top_menu")

# Build a submenu 2 that is not composite 
sub2 = Child("submenu2")

# Add the composite submenu 1 to the top level composite menu
top.append_child(sub1)

# Add the composite submenu 2 to the top level composite menu
top.append_child(sub2)

# Let's test our composite pattern works!
top.component_function()