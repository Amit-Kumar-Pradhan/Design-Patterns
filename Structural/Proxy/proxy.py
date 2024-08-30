import time

class Producer:
    """ Define the 'resourse-intensive' object to instantiated"""
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now")

class Proxy:
    """Define the 'relative less resourse intensive' proxy to instantiated """
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """ Check if producer available """
        print("Artist checking if producer is available ...")

        if self.occupied == 'NO':
            # If producer is available create a producer object
            self.producer = Producer()
            time.sleep(2)

            # make the producer meet the guest
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2) 
            print("Producer is busy!")

# instatiate Proxy
p = Proxy()

# make the proxy: Artist produce untill procer available
p.produce()

# Change the state to occupied
p.occupied = 'Yes'

# Make producer produce
p.produce()