class Handler:
    """ Abstract Handler """
    def __init__(self, successor):
        # Define who is the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request) #@ If handled stop here
        # Otherwise keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation is subclass")


class ConcreteHandler1(Handler): # Inherits from abstract handler
    """ Concrete Handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: # Provide condition for handling
            print(f"Request {request} handled in handler 1.")

            return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from abstract handler
    """ Default Handler """
    def _handle(self, request):
        """ If there is no handler available """
        # No condition checking since there is no handler
        print(f"End of chain, no handler for {request}")
        return True # Indicates that the request has been handled

class Client: # Using handlers
    def __init__(self):
        # Create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests): # Send your request one at a time
        for request in requests:
            self.handler.handle(request)

    
# Create a client
c = Client()

# Create requests
requests = [2, 5, 30, 9]

# Send Requests
c.delegate(requests)
