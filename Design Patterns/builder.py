class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_newcar()
        self._builder.add_model()
        self._builder.add_engine()
        self._builder.add_tyres()

    def get_car(self):
        return self._builder.car


class Builder():
    # abstract builder
    def __init__(self):
        self.car = None

    def create_newcar(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    # concrete builder --> provides parts and tools to the work
    def add_model(self):
        self.car.model = "SkyLark"

    def add_tyres(self):
        self.car.tyres = "Regular Tyres"

    def add_engine(self):
        self.car.engine = "Turbo Engine"


class Car():
    # Product
    def __init__(self):
        self.model = None
        self.tyres = None
        self.engine = None

    def __str__(self):
        return "{}, {}, {}".format(self.model, self.tyres, self.engine)


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)