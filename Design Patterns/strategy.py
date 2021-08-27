import types


class Strategy:
    def __init__(self, function=None):
        self.name = "default Strategy"
        # if a ref to a func is provided, replace execute() method with the given func
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        # this gets replaced by another version if another strategy is provided
        # this prints the strategy used
        print("{} is used".format(self.name))


# replacement method
def strat1(self):
    print("{} is used to execute method 1".format(self.name))


def strat2(self):
    print("{} is used to execute method 2".format(self.name))


# creating def strat
s0 = Strategy()
s0.execute()
# creating 1st variation
s1 = Strategy(strat1)
s1.name = "Startegy One"
# executing it
s1.execute()

s2 = Strategy(strat2)
s2.name = "Strategy Two"
s2.execute()