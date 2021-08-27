class Component:
    # abstract class
    def __init__(self, *args, **kwargs):
        pass

    def component_fun(self):
        pass


class Child():
    # inherits from abstract class, Component
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # this is where we store the name of child item
        self.name = args[0]

    def component_fun(self):
        # print the name of your child here
        print("{}".format(self.name))


class Composite(Component):
    # inherits from component class i.e. abstract
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        # this is where we store the name of the composite object
        self.name = args[0]
        # this is where we keep our child item
        self.children = []

    def append_child(self, child):
        # adds a new child item
        self.children.append(child)

    def remove_child(self, child):
        # removes a child item
        self.children.remove(child)

    def component_fun(self):
        # print the name of the composite function
        print("{}".format(self.name))
        # iterate through the child objects and invoke their component func printing their names
        for i in self.children:
            i.component_fun()


# build composite sub-menu
sub1 = Composite("submenu1")
sub11 = Child("sub-submenu 11")
sub12 = Child("sub-submenu 12")

# adding submenus
sub1.append_child(sub11)
sub1.append_child(sub12)

# build a top level composite menu
top = Composite("Top-Menu")
# build a submenu 2 that  is not a composite
sub2 = Child("Sub Menu 2")
# add the composite submenu to the top level comp menu
top.append_child(sub1)
top.append_child(sub2)
# test the pattern
top.component_fun()
