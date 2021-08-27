class House(object):
    # main class
    def accept(self, visitor):
        # interface to accpet visi
        # triggers the visiting oper
        visitor.visit(self)

    def work_on_hvac(self, hvac_spec):
        print(self, "worked on by ", hvac_spec)

    def work_on_elec(self, elec_spec):
        print(self, "worked on by ", elec_spec)

    def __str__(self):
        # simply return the class name when the house object is printed
        return self.__class__.__name__


class Visitor(object):
    # abstract visitor
    def __str__(self):
        # simply return the class name when the visitor obj is printed
        return self.__class__.__name__


class HvacSpec(Visitor):
    # concrete visi
    def visit(self, house):
        house.work_on_hvac(self)
        # this is ref to house obj


class ElecSpec(Visitor):
    # concrete visi
    def visit(self, house):
        house.work_on_elec(self)


# create an hvac spec
hvac = HvacSpec()
# create an elec spec
elec = ElecSpec()
# create a house
home = House()
# let the house accept the visitors
home.accept(hvac)
home.accept(elec)