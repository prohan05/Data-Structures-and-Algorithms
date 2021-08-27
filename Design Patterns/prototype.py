import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def reg_obj(self, name, obj):
        # register a object
        self._objects[name] = obj

    def unreg_obj(self, name):
        # un register a object
        del self._objects[name]

    def clone(self, name, **attr):
        # clone a registered object and update its attribute
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "SkyLark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.options, self.color)


c = Car()
prototype = Prototype()
prototype.reg_obj("SkyLark", c)

c1 = prototype.clone("SkyLark")

print(c1)
