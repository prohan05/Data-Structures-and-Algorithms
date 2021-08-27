class Borg:
    # borge class making class attribute global
    _shared_state = {}# attribute dict

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    # inherits from borge class
    # this class shares all attributes among its various instances
    # this essentially makes the singleton objects an object oriented global variable
    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the attri dict by inserting new k-v pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # return the attri dict for printing
        return str(self._shared_state)


x = Singleton(HTTP='Hyper Text Transfer Protocol')
print(x)
y = Singleton(SIMP='Squirrel in my pants')
print(y)
