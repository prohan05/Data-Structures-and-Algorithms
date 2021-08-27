class Korean:
    # korean lang
    def __init__(self):
        self.name = "Korean"

    def speak_kor(self):
        return "An-neyong?"


class British:
    # english lang
    def __init__(self):
        self.name = "British"

    def speak_eng(self):
        return "Hello!"


class Adapter:
    # this changes generic method name to individualized method names
    def __init__(self, object, **adapted_method):
        # change the name of method
        self.object = object

        # add a new dictionary item that establishes the mapping between both with speak()
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        # return the rest attribution
        return getattr(self.object, attr)


# list of the objects
objects = []

# create a korean objects
korean = Korean()
# create british objects
british = British()
# appending the objects
objects.append(Adapter(korean, speak=korean.speak_kor))
objects.append(Adapter(british, speak=british.speak_eng))

for obj in objects:
    print("'{}' says '{}' \n".format(obj.name, obj.speak()))
