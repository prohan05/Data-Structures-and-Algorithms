class Subject(object):
    def __init__(self):
        self._observers = []
        # this is where references to all observers are being kept
        # note that this is a 1 to many relation, there will be 1 subject to be observed by multiple observer

    def attach(self, observer):
        # if obs is not already in the list
        if observer not in self._observers:
            self._observers.append(observer)
        # append the list

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier= None):
        # for all obs in the list
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
                # don't notify obs who is actually updating the temp
                # alert the obs


class Core(Subject):
    # inherits from Subject class
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property # Getter that gets the core temp
    def temp(self):
        return self._temp

    @temp.setter # Setter that sets the core temp
    def temp(self, temp):
        self._temp = temp
        self.notify()
        # notify the observer whenever somebody changes the core temp


class TempViewer:

    def update(self, subject):
        # alert method that is invoked when the notify() method in a concrete subject is invoked
        print("Temp viewer: {} has Temperature {}".format(subject._name, subject._temp))


# create a subject
c1 = Core("C1")
c2 = Core("C2")
# create a observer
v1 = TempViewer()
v2 = TempViewer()

# attach obs to 1st core
c1.attach(v1)
c1.attach(v2)

# change the temp to notify
c1.temp = 80
c1.temp = 93
