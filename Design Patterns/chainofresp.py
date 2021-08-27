class Handler:
    # abstract handler
    def __init__(self, successor):
        self.successor = successor

    def handle(self, request):
        handled = self._handle(request)# if handled, stop
        # otherwise, keep going
        if not handled:
            self.successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")


class ConcreteHandler1(Handler):
    # inherits from abstract handler
    def _handle(self, request):
        if 0 < request <= 10:
            # provide a condition for handling
            print("request {} handled in handler 1".format(request))
            return True # indicates that the request has been handled


class DefaultHandler(Handler):
    # inherits from abstract handler
    def _handle(self, request):
        # if there is no handler available
        print("End of chain, no handler for {}".format(request))
        return True


class Client:
    def __init__(self):
        # create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))
        # Note that the default handler has no successor

    def delegate(self, requests):
        # send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


# create a client
c = Client()
# create requests
requests = [1, 2, 4, 66]

c.delegate(requests)


